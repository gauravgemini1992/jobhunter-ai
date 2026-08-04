import requests
from typing import List

from app.models.job_listing import JobListing
from app.providers.job_provider import JobProvider
from app.utils.job_normalizer import JobNormalizer


class ArbeitnowProvider(JobProvider):
    """
    Live Job Provider

    Source:
    https://www.arbeitnow.com/jobs/api/job-board-api

    No API key required.
    """

    API_URL = "https://www.arbeitnow.com/api/job-board-api"

    def search(
        self,
        keywords: List[str],
        location: str = "",
        experience: int = 0,
    ) -> List[JobListing]:

        try:

            response = requests.get(
                self.API_URL,
                timeout=15,
            )

            response.raise_for_status()

            data = response.json()

            jobs = data.get("data", [])

            normalized_jobs = JobNormalizer.normalize_many(
                jobs,
                provider="arbeitnow",
            )

            if not keywords:
                return normalized_jobs

            filtered_jobs = []

            search_terms = {
                keyword.lower().strip()
                for keyword in keywords
            }

            for job in normalized_jobs:

                searchable_text = " ".join([
                    job.title,
                    job.company,
                    job.description,
                    " ".join(job.skills),
                ]).lower()

                if any(
                    term in searchable_text
                    for term in search_terms
                ):
                    filtered_jobs.append(job)

            return filtered_jobs

        except requests.exceptions.RequestException as e:

            print()
            print("=" * 70)
            print("Arbeitnow Provider Error")
            print("=" * 70)
            print(e)
            print()

            return []

        except Exception as e:

            print()
            print("=" * 70)
            print("Unexpected Arbeitnow Error")
            print("=" * 70)
            print(e)
            print()

            return []