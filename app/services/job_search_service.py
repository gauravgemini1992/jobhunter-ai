from typing import List

from app.models.job_listing import JobListing
from app.providers.job_provider import JobProvider
from app.utils.job_deduplicator import JobDeduplicator


class JobSearchService:
    """
    Multi-Provider Job Search Service.

    Responsibilities
    ----------------
    • Search all registered providers
    • Merge job results
    • Remove duplicate jobs
    • Sort jobs by ATS score
    • Continue gracefully if a provider fails
    """

    def __init__(self):

        self.providers: List[JobProvider] = []

    # --------------------------------------------------

    def add_provider(
        self,
        provider: JobProvider,
    ):

        self.providers.append(provider)

    # --------------------------------------------------

    def search(
        self,
        keywords: List[str],
        location: str = "",
        experience: int = 0,
    ) -> List[JobListing]:

        all_jobs: List[JobListing] = []

        print()
        print("=" * 70)
        print("Searching Registered Providers")
        print("=" * 70)

        for provider in self.providers:

            try:

                jobs = provider.search(
                    keywords=keywords,
                    location=location,
                    experience=experience,
                )

                print(
                    f"✓ {provider.__class__.__name__:<25}"
                    f"{len(jobs)} jobs"
                )

                all_jobs.extend(jobs)

            except Exception as e:

                print(
                    f"✗ {provider.__class__.__name__:<25}"
                    "Failed"
                )

                print(e)

        # --------------------------------------------------
        # Remove duplicate jobs
        # --------------------------------------------------

        all_jobs = JobDeduplicator.remove_duplicates(
            all_jobs
        )

        # --------------------------------------------------
        # Sort by ATS score
        # (Final ranking happens later in JobRanker)
        # --------------------------------------------------

        all_jobs.sort(
            key=lambda job: job.ats_match_score,
            reverse=True,
        )

        return all_jobs

    # --------------------------------------------------

    def provider_count(self) -> int:

        return len(self.providers)