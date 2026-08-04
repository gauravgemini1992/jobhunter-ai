from typing import Dict, List

from app.models.job_listing import JobListing


class JobNormalizer:
    """
    Converts different job provider responses into a
    common JobListing model.
    """

    # --------------------------------------------------
    # Arbeitnow
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

            employment_type=(
                job.get("job_types", [""])[0]
                if job.get("job_types")
                else ""
            ),

            salary="Not Disclosed",

            apply_url=job.get("url", ""),

            source="Arbeitnow",

            ats_match_score=0,
        )

    # --------------------------------------------------
    # RemoteOK
    # --------------------------------------------------

    @staticmethod
    def remoteok(job: Dict) -> JobListing:

        return JobListing(

            title=job.get("position", ""),

            company=job.get("company", ""),

            location=job.get("location", "Remote"),

            description=job.get("description", ""),

            skills=job.get("tags", []),

            experience="",

            employment_type="Remote",

            salary="Not Disclosed",

            apply_url=job.get("url", ""),

            source="RemoteOK",

            ats_match_score=0,
        )

    # --------------------------------------------------
    # Adzuna
    # --------------------------------------------------

    @staticmethod
    def adzuna(job: Dict) -> JobListing:

        salary = "Not Disclosed"

        if job.get("salary_min"):

            salary = f"₹{int(job['salary_min']):,}"

        return JobListing(

            title=job.get("title", ""),

            company=job.get(
                "company",
                {},
            ).get(
                "display_name",
                "",
            ),

            location=job.get(
                "location",
                {},
            ).get(
                "display_name",
                "",
            ),

            description=job.get("description", ""),

            skills=[],

            experience="",

            employment_type="",

            salary=salary,

            apply_url=job.get(
                "redirect_url",
                "",
            ),

            source="Adzuna",

            ats_match_score=0,
        )

    # --------------------------------------------------
    # Universal Normalizer
    # --------------------------------------------------

    @staticmethod
    def normalize_many(
        jobs: List[Dict],
        provider: str,
    ) -> List[JobListing]:

        normalized = []

        provider = provider.lower()

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