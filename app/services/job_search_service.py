from time import perf_counter
from typing import List

from app.models.job_listing import JobListing
from app.providers.job_provider import JobProvider
from app.utils.job_deduplicator import JobDeduplicator


class JobSearchService:
    """
    JobHunter AI

    Multi Provider Job Search Engine

    Responsibilities
    ----------------
    ✓ Execute every registered provider
    ✓ Prevent one provider failure from stopping others
    ✓ Display provider statistics
    ✓ Remove duplicate jobs
    ✓ Return merged results
    """

    # --------------------------------------------------

    def __init__(self):

        self.providers: List[JobProvider] = []

    # --------------------------------------------------

    def add_provider(
        self,
        provider: JobProvider,
    ):

        self.providers.append(provider)

    # --------------------------------------------------

    def provider_count(self) -> int:

        return len(self.providers)

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

            provider_name = provider.__class__.__name__

            start = perf_counter()

            try:

                jobs = provider.search(
                    keywords=keywords,
                    location=location,
                    experience=experience,
                )

                elapsed = round(
                    perf_counter() - start,
                    2,
                )

                print(
                    f"✓ {provider_name:<25}"
                    f"{len(jobs):>4} jobs   "
                    f"{elapsed:>5}s"
                )

                all_jobs.extend(jobs)

            except Exception as ex:

                elapsed = round(
                    perf_counter() - start,
                    2,
                )

                print(
                    f"✗ {provider_name:<25}"
                    f"FAILED   {elapsed:>5}s"
                )

                print(ex)

        print()
        print("-" * 70)
        print(
            f"Collected Jobs : {len(all_jobs)}"
        )

        # --------------------------------------------------
        # Remove Duplicate Jobs
        # --------------------------------------------------

        before = len(all_jobs)

        all_jobs = JobDeduplicator.remove_duplicates(
            all_jobs
        )

        duplicates_removed = before - len(all_jobs)

        print(
            f"Duplicates Removed : {duplicates_removed}"
        )

        print(
            f"Unique Jobs : {len(all_jobs)}"
        )

        print("-" * 70)

        return all_jobs