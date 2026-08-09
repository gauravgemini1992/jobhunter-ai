"""
============================================================
JobHunter AI
Live Company Provider
============================================================
"""

from urllib.parse import quote

import requests

from app.models.company_profile import CompanyProfile
from app.providers.company_provider import CompanyProvider
from app.providers.mock_company_provider import MockCompanyProvider


class LiveCompanyProvider(CompanyProvider):
    """
    Live Company Provider

    Retrieves live company information from Wikipedia.

    Falls back to MockCompanyProvider whenever
    richer local data is available or the company
    cannot be retrieved online.
    """

    WIKI_URL = (
        "https://en.wikipedia.org/api/rest_v1/page/summary/{}"
    )

    USER_AGENT = {
        "User-Agent": "JobHunterAI/1.0"
    }

    # --------------------------------------------------

    def __init__(self):

        self.mock = MockCompanyProvider()

        self.aliases = {

            "tesla": "Tesla, Inc.",

            "amazon": "Amazon (company)",

            "apple": "Apple Inc.",

            "meta": "Meta Platforms",

            "facebook": "Meta Platforms",

            "google": "Google",

            "alphabet": "Alphabet Inc.",

            "x": "X Corp.",

            "twitter": "Twitter",

            "ibm": "IBM",

            "oracle": "Oracle Corporation",

            "adobe": "Adobe Inc.",

            "netflix": "Netflix",

            "uber": "Uber",

            "airbnb": "Airbnb",

            "spotify": "Spotify",

            "microsoft": "Microsoft",

            "openai": "OpenAI",

            "salesforce": "Salesforce",

            "freshworks": "Freshworks",

        }

    # --------------------------------------------------

    def search(self, company_name: str):

        company = company_name.strip()

        if not company:

            return None

        profile = self._search_live(company)

        if profile is None:

            return self.mock.search(company)

        mock = self.mock.search(company)

        if mock:

            self._merge_profile(profile, mock)

        return profile

    # --------------------------------------------------

    def _search_live(self, company):

        page = self.aliases.get(
            company.lower(),
            company,
        )

        profile = self._fetch(page)

        if profile is None:

            return None

        description = profile.description.lower()

        if (

            "may refer to" in description

            or "most commonly refers to" in description

            or "most often refers to" in description

        ):

            company_page = f"{company} (company)"

            retry = self._fetch(company_page)

            if retry:

                return retry

        return profile

    # --------------------------------------------------

    def _fetch(self, page):

        try:

            url = self.WIKI_URL.format(
                quote(page)
            )

            response = requests.get(

                url,

                headers=self.USER_AGENT,

                timeout=8,

            )

            if response.status_code != 200:

                return None

            data = response.json()

            return CompanyProfile(

                name=data.get(
                    "title",
                    page,
                ),

                description=data.get(
                    "extract",
                    "",
                ),

                website="",

                industry="",

                headquarters="",

                founded="",

                employees="",

                ceo="",

            )

        except requests.RequestException:

            return None

        except Exception:

            return None

    # --------------------------------------------------

    def _merge_profile(

        self,

        live,

        mock,

    ):

        if not live.website:

            live.website = mock.website

        if not live.careers_url:

            live.careers_url = mock.careers_url

        if not live.linkedin_url:

            live.linkedin_url = mock.linkedin_url

        if not live.glassdoor_url:

            live.glassdoor_url = mock.glassdoor_url

        if not live.industry:

            live.industry = mock.industry

        if not live.headquarters:

            live.headquarters = mock.headquarters

        if not live.founded:

            live.founded = mock.founded

        if not live.employees:

            live.employees = mock.employees

        if not live.ceo:

            live.ceo = mock.ceo

        live.products = mock.products
        live.hiring_roles = mock.hiring_roles
        live.technologies = mock.technologies
        live.interview_topics = mock.interview_topics
        live.latest_news = mock.latest_news