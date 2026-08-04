from typing import Dict, List

from app.models.job_listing import JobListing


class JobNormalizer:
    """
    Converts raw API responses from different job providers
    into a common JobListing model.

    Every provider should pass its raw JSON dictionary
    to one of these normalization methods.
    """

    # --------------------------------------------------

    @staticmethod
    def arbeitnow(job: Dict) -> JobListing:

        return JobListing(

            title=job.get("title", ""),

            company=job.get("company_name", ""),

            location=job.get("location", "Remote"),

            description=job.get("description", ""),

            skills=job.get("tags", []),

            experience="",

            employment_type=job.get("job_types", [""])[0]
            if job.get("job_types")
            else "",

            salary="Not Disclosed",

            apply_url=job.get("url", ""),

            source="Arbeitnow",

            ats_match_score=0,
        )

    # --------------------------------------------------

    @staticmethod
    def remoteok(job: Dict) -> JobListing:

        return JobListing(

            title=job.get("position", ""),

            company=job.get("company", ""),

            location="Remote",

            description=job.get("description", ""),

            skills=job.get("tags", []),

            experience="",

            employment_type="Remote",

            salary="Not Disclosed",

            apply_url=job.get("apply_url", ""),

            source="RemoteOK",

            ats_match_score=0,
        )

    # --------------------------------------------------

    @staticmethod
    def adzuna(job: Dict) -> JobListing:

        return JobListing(

            title=job.get("title", ""),

            company=job.get("company", {}).get("display_name", ""),

            location=job.get("location", {}).get("display_name", ""),

            description=job.get("description", ""),

            skills=[],

            experience="",

            employment_type="",

            salary=(
                f"₹{int(job.get('salary_min', 0)):,}"
                if job.get("salary_min")
                else "Not Disclosed"
            ),

            apply_url=job.get("redirect_url", ""),

            source="Adzuna",

            ats_match_score=0,
        )

    # --------------------------------------------------

    @staticmethod
    def normalize_many(
        jobs: List[Dict],
        provider: str,
    ) -> List[JobListing]:

        normalized = []

        for job in jobs:

            try:

                if provider == "arbeitnow":

                    normalized.append(
                        JobNormalizer.arbeitnow(job)
                    )

                elif provider == "remoteok":

                    normalized.append(
                        JobNormalizer.remoteok(job)
                    )

                elif provider == "adzuna":

                    normalized.append(
                        JobNormalizer.adzuna(job)
                    )

            except Exception:

                continue

        return normalized