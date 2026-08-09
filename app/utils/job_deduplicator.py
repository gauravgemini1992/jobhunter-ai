"""
=============================================================
JobHunter AI
Production Job Deduplicator v3.0
=============================================================

Responsibilities
----------------
✓ Remove duplicate jobs
✓ Keep the highest quality listing
✓ Normalize titles and URLs
✓ Compare descriptions intelligently
✓ Collect deduplication statistics
"""

import re

from dataclasses import dataclass
from difflib import SequenceMatcher
from typing import Dict
from typing import List

from app.models.job_listing import JobListing


# =============================================================
# Deduplication Statistics
# =============================================================


@dataclass
class DeduplicationStats:

    total_jobs: int = 0

    url_duplicates: int = 0

    company_duplicates: int = 0

    similar_duplicates: int = 0

    unique_jobs: int = 0

    @property
    def duplicates_removed(self):

        return (

            self.url_duplicates

            + self.company_duplicates

            + self.similar_duplicates

        )


# =============================================================
# Job Deduplicator
# =============================================================


class JobDeduplicator:

    """
    Production-ready job deduplication engine.
    """

    DESCRIPTION_THRESHOLD = 0.90

    TITLE_THRESHOLD = 0.85

    # ---------------------------------------------------------

    @staticmethod
    def normalize(text: str) -> str:

        """
        Normalizes text for comparisons.
        """

        if not text:

            return ""

        text = text.lower()

        text = re.sub(
            r"\([^)]*\)",
            " ",
            text,
        )

        text = re.sub(
            r"\[[^\]]*\]",
            " ",
            text,
        )

        text = re.sub(
            r"[^a-z0-9 ]",
            " ",
            text,
        )

        text = re.sub(
            r"\s+",
            " ",
            text,
        )

        return text.strip()

    # ---------------------------------------------------------

    @classmethod
    def normalize_title(
        cls,
        title: str,
    ) -> str:

        """
        Removes location and marketing words
        from titles before comparison.
        """

        title = cls.normalize(title)

        ignored_words = {

            "remote",
            "hybrid",
            "onsite",

            "india",
            "bangalore",
            "bengaluru",
            "hyderabad",
            "chennai",
            "mumbai",
            "delhi",
            "gurgaon",
            "pune",
            "kolkata",

            "saas",
            "b2b",

        }

        words = [

            word

            for word in title.split()

            if word not in ignored_words

        ]

        return " ".join(words)

    # ---------------------------------------------------------

    @classmethod
    def normalize_url(
        cls,
        url: str,
    ) -> str:

        if not url:

            return ""

        url = url.lower().strip()

        url = url.replace(
            "https://",
            "",
        )

        url = url.replace(
            "http://",
            "",
        )

        url = url.rstrip("/")

        return url

    # ---------------------------------------------------------

    @classmethod
    def title_similarity(
        cls,
        title1: str,
        title2: str,
    ) -> float:

        return SequenceMatcher(

            None,

            cls.normalize_title(title1),

            cls.normalize_title(title2),

        ).ratio()

    # ---------------------------------------------------------

    @classmethod
    def description_similarity(
        cls,
        job1: JobListing,
        job2: JobListing,
    ) -> float:

        return SequenceMatcher(

            None,

            cls.normalize(job1.description),

            cls.normalize(job2.description),

        ).ratio()
        # ---------------------------------------------------------

    @classmethod
    def quality_score(
        cls,
        job: JobListing,
    ) -> int:
        """
        Calculates the quality of a job listing.

        Richer jobs receive higher scores.
        """

        score = 0

        # Basic Information

        if job.title:
            score += 5

        if job.company:
            score += 5

        if job.location:
            score += 5

        if job.apply_url:
            score += 10

        # Salary

        if job.salary:

            if job.salary != "Not Disclosed":

                score += 15

        # Skills

        if job.skills:

            score += min(
                len(job.skills) * 2,
                20,
            )

        # Description

        if job.description:

            score += min(
                len(job.description) // 40,
                40,
            )

        return score

    # ---------------------------------------------------------

    @classmethod
    def better_job(
        cls,
        job1: JobListing,
        job2: JobListing,
    ) -> JobListing:
        """
        Returns the better quality job.
        """

        if (
            cls.quality_score(job2)
            >
            cls.quality_score(job1)
        ):

            return job2

        return job1

    # ---------------------------------------------------------

    @classmethod
    def group_by_company(
        cls,
        jobs: List[JobListing],
    ) -> Dict[str, List[JobListing]]:
        """
        Groups jobs by normalized company.
        """

        grouped: Dict[
            str,
            List[JobListing],
        ] = {}

        for job in jobs:

            company = cls.normalize(
                job.company
            )

            if not company:

                company = "unknown"

            grouped.setdefault(
                company,
                [],
            ).append(job)

        return grouped

    # ---------------------------------------------------------

    @classmethod
    def remove_url_duplicates(
        cls,
        jobs: List[JobListing],
        stats: DeduplicationStats,
    ) -> List[JobListing]:
        """
        Removes duplicate jobs having
        identical Apply URLs.
        """

        unique = []

        seen = set()

        for job in jobs:

            url = cls.normalize_url(
                job.apply_url
            )

            if not url:

                unique.append(job)

                continue

            if url in seen:

                stats.url_duplicates += 1

                continue

            seen.add(url)

            unique.append(job)

        return unique

    # ---------------------------------------------------------

    @classmethod
    def remove_company_duplicates(
        cls,
        jobs: List[JobListing],
        stats: DeduplicationStats,
    ) -> List[JobListing]:
        """
        Removes exact Company + Title duplicates.
        """

        unique = []

        seen = {}

        for job in jobs:

            key = (

                cls.normalize(
                    job.company
                ),

                cls.normalize_title(
                    job.title
                ),

            )

            if key not in seen:

                seen[key] = job

                unique.append(job)

                continue

            better = cls.better_job(

                seen[key],

                job,

            )

            if better is not seen[key]:

                index = unique.index(
                    seen[key]
                )

                unique[index] = better

                seen[key] = better

            stats.company_duplicates += 1

        return unique
        # ---------------------------------------------------------

    @classmethod
    def remove_similar_jobs(
        cls,
        jobs: List[JobListing],
        stats: DeduplicationStats,
    ) -> List[JobListing]:
        """
        Removes near-duplicate jobs within the same company.

        Two jobs are considered duplicates when

        • Company is identical
        • Title similarity >= TITLE_THRESHOLD
        • Description similarity >= DESCRIPTION_THRESHOLD

        The richer job is retained.
        """

        grouped = cls.group_by_company(
            jobs
        )

        final_jobs: List[JobListing] = []

        for company, company_jobs in grouped.items():

            company_unique: List[JobListing] = []

            for current_job in company_jobs:

                matched = False

                for index, saved_job in enumerate(
                    company_unique
                ):

                    title_score = cls.title_similarity(
                        current_job.title,
                        saved_job.title,
                    )

                    if title_score < cls.TITLE_THRESHOLD:
                        continue

                    description_score = (
                        cls.description_similarity(
                            current_job,
                            saved_job,
                        )
                    )

                    if (
                        description_score
                        >= cls.DESCRIPTION_THRESHOLD
                    ):

                        better = cls.better_job(
                            saved_job,
                            current_job,
                        )

                        company_unique[index] = better

                        stats.similar_duplicates += 1

                        matched = True

                        break

                if not matched:

                    company_unique.append(
                        current_job
                    )

            final_jobs.extend(
                company_unique
            )

        return final_jobs

    # ---------------------------------------------------------

    @classmethod
    def deduplicate(
        cls,
        jobs: List[JobListing],
    ):

        """
        Internal production pipeline.

        URL
            ↓

        Company + Title
            ↓

        Similar Jobs

        Returns
        -------
        unique_jobs,
        statistics
        """

        stats = DeduplicationStats()

        stats.total_jobs = len(jobs)

        jobs = cls.remove_url_duplicates(
            jobs,
            stats,
        )

        jobs = cls.remove_company_duplicates(
            jobs,
            stats,
        )

        jobs = cls.remove_similar_jobs(
            jobs,
            stats,
        )

        stats.unique_jobs = len(jobs)

        return jobs, stats
        # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    @classmethod
    def remove_duplicates(
        cls,
        jobs: List[JobListing],
    ) -> List[JobListing]:
        """
        Public API used by JobSearchService.

        Performs the complete deduplication pipeline and
        returns only the unique jobs.
        """

        jobs, stats = cls.deduplicate(
            jobs
        )

        print()

        print("-" * 70)
        print("JOB DEDUPLICATION SUMMARY")
        print("-" * 70)

        print(
            f"Collected Jobs       : {stats.total_jobs}"
        )

        print(
            f"URL Duplicates      : {stats.url_duplicates}"
        )

        print(
            f"Company Duplicates  : {stats.company_duplicates}"
        )

        print(
            f"Similar Duplicates  : {stats.similar_duplicates}"
        )

        print(
            f"Duplicates Removed  : {stats.duplicates_removed}"
        )

        print(
            f"Unique Jobs         : {stats.unique_jobs}"
        )

        print("-" * 70)
        print()

        return jobs