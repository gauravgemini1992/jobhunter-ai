import os
import time
from typing import Dict, List

import requests

from config.settings import (
    ADZUNA_COUNTRY,
    ADZUNA_RESULTS_PER_PAGE,
    ADZUNA_TIMEOUT,
)

from app.models.job_listing import JobListing
from app.providers.job_provider import JobProvider
from app.utils.job_normalizer import JobNormalizer


class AdzunaProvider(JobProvider):
    """
    JobHunter AI
    ----------------------------

    Production Adzuna Provider

    Features
    --------
    ✓ Live Adzuna API
    ✓ Multiple search queries
    ✓ Multiple pages
    ✓ Automatic retries
    ✓ Smart filtering
    ✓ Job normalization
    ✓ Duplicate removal
    ✓ Graceful error handling

    Version
    -------
    v1.0.0
    """

    BASE_URL = "https://api.adzuna.com/v1/api/jobs"

    MAX_PAGES = 2

    MAX_RETRIES = 2

    RETRY_DELAY = 1

    # --------------------------------------------------

    def __init__(self):

        self.app_id = os.getenv(
            "ADZUNA_APP_ID",
            "",
        ).strip()

        self.app_key = os.getenv(
            "ADZUNA_APP_KEY",
            "",
        ).strip()

    # --------------------------------------------------

    def _configured(self) -> bool:

        return bool(
            self.app_id
            and
            self.app_key
        )

    # --------------------------------------------------

    def _build_queries(
        self,
        keywords: List[str],
    ) -> List[str]:
        """
        Build multiple intelligent
        search queries.

        Example

        Customer Success Manager

        Key Account Manager

        Enterprise Account Manager

        Customer Success

        Account Management
        """

        if not keywords:

            return [""]

        queries = []

        if len(keywords) >= 3:

            queries.append(
                " ".join(keywords[:3])
            )

        if len(keywords) >= 5:

            queries.append(
                " ".join(keywords[:5])
            )

        queries.append(
            "Customer Success Manager"
        )

        queries.append(
            "Key Account Manager"
        )

        queries.append(
            "Enterprise Account Manager"
        )

        queries.append(
            "Customer Success"
        )

        queries.append(
            "Account Management"
        )

        # Remove duplicates while
        # preserving order

        unique = []

        seen = set()

        for query in queries:

            query = query.strip()

            if (
                query
                and
                query not in seen
            ):

                unique.append(query)

                seen.add(query)

        return unique
        # --------------------------------------------------

    def _request(
        self,
        query: str,
        page: int,
    ) -> List[Dict]:
        """
        Executes a single Adzuna API request.

        Features
        --------
        ✓ Retry mechanism
        ✓ Timeout protection
        ✓ HTTP validation
        ✓ JSON validation
        """

        url = (
            f"{self.BASE_URL}/"
            f"{ADZUNA_COUNTRY}/"
            f"search/{page}"
        )

        params = {

            "app_id": self.app_id,

            "app_key": self.app_key,

            "what": query,

            "results_per_page": ADZUNA_RESULTS_PER_PAGE,

            "content-type": "application/json",

        }

        for attempt in range(

            self.MAX_RETRIES

        ):

            try:

                response = requests.get(

                    url,

                    params=params,

                    timeout=ADZUNA_TIMEOUT,

                )

                response.raise_for_status()

                data = response.json()

                return data.get(

                    "results",

                    [],

                )

            except requests.exceptions.Timeout:

                if attempt + 1 == self.MAX_RETRIES:

                    print(
                        "Adzuna timeout."
                    )

            except requests.exceptions.RequestException as ex:

                if attempt + 1 == self.MAX_RETRIES:

                    print(
                        f"Adzuna request failed: {ex}"
                    )

            except Exception as ex:

                if attempt + 1 == self.MAX_RETRIES:

                    print(
                        f"Unexpected Adzuna error: {ex}"
                    )

            time.sleep(
                self.RETRY_DELAY
            )

        return []

    # --------------------------------------------------

    def _fetch_all_jobs(
        self,
        queries: List[str],
    ) -> List[Dict]:
        """
        Fetches jobs using multiple
        search queries and pages.
        """

        jobs: List[Dict] = []

        for query in queries:

            for page in range(

                1,

                self.MAX_PAGES + 1,

            ):

                results = self._request(

                    query,

                    page,

                )

                if not results:

                    break

                jobs.extend(

                    results

                )

        return jobs
        # --------------------------------------------------

    def _normalize_jobs(
        self,
        jobs: List[Dict],
    ) -> List[JobListing]:
        """
        Converts raw Adzuna jobs into
        the standard JobListing model.
        """

        return JobNormalizer.normalize_many(
            jobs,
            provider="adzuna",
        )

    # --------------------------------------------------

    def _filter_jobs(
        self,
        jobs: List[JobListing],
        keywords: List[str],
    ) -> List[JobListing]:
        """
        Keeps only jobs relevant to the
        candidate's profile.
        """

        if not keywords:
            return jobs

        search_terms = {

            keyword.lower().strip()

            for keyword in keywords

            if keyword.strip()

        }

        filtered: List[JobListing] = []

        for job in jobs:

            searchable = " ".join(

                [

                    job.title,

                    job.company,

                    job.location,

                    job.description,

                    " ".join(job.skills),

                ]

            ).lower()

            if any(

                keyword in searchable

                for keyword in search_terms

            ):

                filtered.append(job)

        return filtered

    # --------------------------------------------------

    def _deduplicate(
        self,
        jobs: List[JobListing],
    ) -> List[JobListing]:
        """
        Removes duplicate jobs.

        Duplicate Definition
        --------------------
        Same company + title + location
        """

        unique: List[JobListing] = []

        seen = set()

        for job in jobs:

            key = (

                job.company.lower().strip(),

                job.title.lower().strip(),

                job.location.lower().strip(),

            )

            if key in seen:

                continue

            seen.add(key)

            unique.append(job)

        return unique

    # --------------------------------------------------

    def _prepare_jobs(
        self,
        raw_jobs: List[Dict],
        keywords: List[str],
    ) -> List[JobListing]:
        """
        Complete processing pipeline.

        Raw JSON
            ↓
        Normalize
            ↓
        Filter
            ↓
        Deduplicate
            ↓
        Production Job Listings
        """

        jobs = self._normalize_jobs(
            raw_jobs
        )

        jobs = self._filter_jobs(
            jobs,
            keywords,
        )

        jobs = self._deduplicate(
            jobs,
        )

        return jobs
        # --------------------------------------------------

    def search(
        self,
        keywords: List[str],
        location: str = "",
        experience: int = 0,
    ) -> List[JobListing]:
        """
        Searches Adzuna and returns production-ready
        JobListing objects.

        Workflow
        --------
            Credentials
                 │
                 ▼
            Build Queries
                 │
                 ▼
            Fetch API Results
                 │
                 ▼
            Normalize Jobs
                 │
                 ▼
            Filter Relevant Jobs
                 │
                 ▼
            Remove Duplicates
                 │
                 ▼
            Return Final Jobs
        """

        if not self._configured():
            return []

        try:

            queries = self._build_queries(
                keywords,
            )

            raw_jobs = self._fetch_all_jobs(
                queries,
            )

            if not raw_jobs:
                return []

            jobs = self._prepare_jobs(
                raw_jobs,
                keywords,
            )

            return jobs

        except Exception as ex:

            print()
            print("=" * 70)
            print("Adzuna Provider Error")
            print("=" * 70)
            print(ex)
            print()

            return []