from typing import List

from app.models.job_listing import JobListing
from app.providers.job_provider import JobProvider


class JobSearchService:
    """
    Searches jobs from one or more providers
    and ranks them.
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

        jobs = []

        for provider in self.providers:

            try:

                jobs.extend(
                    provider.search(
                        keywords,
                        location,
                        experience,
                    )
                )

            except Exception as e:

                print(
                    f"Provider Error : {provider.__class__.__name__}"
                )

                print(e)

        jobs.sort(
            key=lambda job: job.ats_match_score,
            reverse=True,
        )

        return jobs