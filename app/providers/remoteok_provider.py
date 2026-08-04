import requests
from typing import List

from app.models.job_listing import JobListing
from app.providers.job_provider import JobProvider
from app.utils.job_normalizer import JobNormalizer


class RemoteOKProvider(JobProvider):
    """
    RemoteOK Live Job Provider

    Source:
    https://remoteok.com/api

    No API Key Required.
    """

    API_URL = "https://remoteok.com/api"

    def search(
        self,
        keywords: List[str],
        location: str = "",
        experience: int = 0,
    ) -> List[JobListing]:

        try:

            headers = {
                "User-Agent": "JobHunterAI/1.0"
            }

            response = requests.get(
                self.API_URL,
                headers=headers,
                timeout=20,
            )

            response.raise_for_status()

            data = response.json()

            # First element contains metadata
            if isinstance(data, list) and len(data) > 0:
                jobs = data[1:]
            else:
                jobs = []

            normalized_jobs = JobNormalizer.normalize_many(
                jobs,
                provider="remoteok",
            )

            # --------------------------------------------------
            # Keyword Filtering
            # --------------------------------------------------

            if not keywords:
                return normalized_jobs

            filtered_jobs = []

            search_terms = {
                keyword.lower().strip()
                for keyword in keywords
            }

            for job in normalized_jobs:

                searchable_text = " ".join(
                    [
                        job.title,
                        job.company,
                        job.description,
                        " ".join(job.skills),
                    ]
                ).lower()

                if any(
                    keyword in searchable_text
                    for keyword in search_terms
                ):
                    filtered_jobs.append(job)

            return filtered_jobs

        except requests.exceptions.RequestException as e:

            print()
            print("=" * 70)
            print("RemoteOK Provider Error")
            print("=" * 70)
            print(e)
            print()

            return []

        except Exception as e:

            print()
            print("=" * 70)
            print("Unexpected RemoteOK Error")
            print("=" * 70)
            print(e)
            print()

            return []