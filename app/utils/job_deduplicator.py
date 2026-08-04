from typing import List

from app.models.job_listing import JobListing


class JobDeduplicator:
    """
    Removes duplicate jobs collected from multiple providers.

    A duplicate is identified using:

    • Job Title
    • Company
    • Location

    If duplicates exist, the job with the highest ATS score
    is retained.
    """

    @staticmethod
    def remove_duplicates(
        jobs: List[JobListing],
    ) -> List[JobListing]:

        unique_jobs = {}

        for job in jobs:

            key = (
                job.title.strip().lower(),
                job.company.strip().lower(),
                job.location.strip().lower(),
            )

            if key not in unique_jobs:

                unique_jobs[key] = job

            else:

                existing = unique_jobs[key]

                if job.ats_match_score > existing.ats_match_score:

                    unique_jobs[key] = job

        return list(unique_jobs.values())