from urllib.parse import quote_plus


class SearchLinkProvider:
    """
    JobHunter AI

    Search Query Builder v2

    Builds optimized search queries for:

    - LinkedIn
    - Naukri
    - Indeed
    - Foundit
    - Wellfound
    - Google Jobs
    """

    HIGH_PRIORITY = {

        "customer success",
        "crm",
        "saas",
        "salesforce",
        "hubspot",
        "account management",
        "key account",
        "enterprise",
        "enterprise accounts",
        "business development",
        "sql",
        "power bi",
        "artificial intelligence",
        "generative ai",
        "python",
        "aws",
        "azure",
        "react",
        "java",

    }

    MEDIUM_PRIORITY = {

        "renewals",
        "quarterly business review",
        "stakeholder management",
        "customer retention",
        "upsell",
        "cross sell",
        "go to market",
        "analytics",
        "cloud",
        "docker",
        "kubernetes",

    }

    # --------------------------------------------------

    def _clean_role(
        self,
        role: str,
    ) -> str:

        if not role:
            return "Professional"

        role = role.strip()

        replacements = {

            "Professional": "Professional",

            "Customer Success":
                "Customer Success Manager",

            "Account Manager":
                "Enterprise Account Manager",

            "Business Development":
                "Business Development Manager",

        }

        return replacements.get(
            role,
            role,
        )

    # --------------------------------------------------

    def _prioritize_skills(
        self,
        skills,
    ):

        if not skills:
            return []

        high = []
        medium = []
        low = []

        seen = set()

        for skill in skills:

            skill = skill.strip()

            key = skill.lower()

            if key in seen:
                continue

            seen.add(key)

            if key in self.HIGH_PRIORITY:

                high.append(skill)

            elif key in self.MEDIUM_PRIORITY:

                medium.append(skill)

            else:

                low.append(skill)

        return high + medium + low

    # --------------------------------------------------

    def generate_query(
        self,
        role="",
        skills=None,
    ):

        if skills is None:
            skills = []

        role = self._clean_role(role)

        ordered_skills = self._prioritize_skills(
            skills
        )

        words = [role]

        for skill in ordered_skills:

            if len(words) >= 6:
                break

            if skill.lower() in role.lower():
                continue

            words.append(skill)

        return " ".join(words)

    # --------------------------------------------------

    def linkedin(self, query):

        return (
            "https://www.linkedin.com/jobs/search/"
            "?keywords="
            + quote_plus(query)
        )

    # --------------------------------------------------

    def naukri(self, query):

        slug = query.lower().replace(" ", "-")

        return (
            f"https://www.naukri.com/{slug}-jobs"
        )

    # --------------------------------------------------

    def indeed(self, query):

        return (
            "https://in.indeed.com/jobs?q="
            + quote_plus(query)
        )

    # --------------------------------------------------

    def foundit(self, query):

        return (
            "https://www.foundit.in/srp/results"
            "?query="
            + quote_plus(query)
        )

    # --------------------------------------------------

    def wellfound(self, query):

        return (
            "https://wellfound.com/jobs"
            "?query="
            + quote_plus(query)
        )

    # --------------------------------------------------

    def google_jobs(self, query):

        return (
            "https://www.google.com/search?q="
            + quote_plus(query + " jobs")
        )

    # --------------------------------------------------

    def generate_links(
        self,
        role="",
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