from urllib.parse import quote_plus


class SearchLinkProvider:
    """
    Generates smart job search links for multiple job portals.

    Instead of depending on APIs, this provider builds
    optimized search URLs using the candidate's target role
    and skills.

    Supported Platforms:
        - LinkedIn
        - Naukri
        - Indeed India
        - Foundit
        - Wellfound
        - Google Jobs
    """

    # --------------------------------------------------

    def generate_query(
        self,
        role: str = "",
        skills=None,
    ) -> str:

        if skills is None:
            skills = []

        words = []

        if role:
            words.append(role)

        # Add first few important skills
        for skill in skills[:5]:

            if skill.lower() not in role.lower():

                words.append(skill)

        return " ".join(words).strip()

    # --------------------------------------------------

    def linkedin(self, query: str) -> str:

        return (
            "https://www.linkedin.com/jobs/search/"
            "?keywords="
            + quote_plus(query)
        )

    # --------------------------------------------------

    def naukri(self, query: str) -> str:

        slug = query.lower().replace(" ", "-")

        return (
            "https://www.naukri.com/"
            f"{slug}-jobs"
        )

    # --------------------------------------------------

    def indeed(self, query: str) -> str:

        return (
            "https://in.indeed.com/jobs?q="
            + quote_plus(query)
        )

    # --------------------------------------------------

    def foundit(self, query: str) -> str:

        return (
            "https://www.foundit.in/srp/results"
            "?query="
            + quote_plus(query)
        )

    # --------------------------------------------------

    def wellfound(self, query: str) -> str:

        return (
            "https://wellfound.com/jobs"
            "?query="
            + quote_plus(query)
        )

    # --------------------------------------------------

    def google_jobs(self, query: str) -> str:

        return (
            "https://www.google.com/search?q="
            + quote_plus(query + " jobs")
        )

    # --------------------------------------------------

    def generate_links(
        self,
        role: str = "",
        skills=None,
    ):

        query = self.generate_query(
            role,
            skills,
        )

        return {
            "query": query,
            "LinkedIn": self.linkedin(query),
            "Naukri": self.naukri(query),
            "Indeed": self.indeed(query),
            "Foundit": self.foundit(query),
            "Wellfound": self.wellfound(query),
            "Google Jobs": self.google_jobs(query),
        }