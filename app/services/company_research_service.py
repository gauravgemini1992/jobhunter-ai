from app.providers.mock_company_provider import MockCompanyProvider


class CompanyResearchService:
    """
    Company Research Service

    Fetches and displays
    company information.
    """

    def __init__(self):

        self.provider = MockCompanyProvider()

    # --------------------------------------------------

    def run(self):

        print()
        print("=" * 70)
        print("COMPANY RESEARCH")
        print("=" * 70)

        print()

        company = input(
            "Enter Company Name : "
        ).strip()

        if not company:

            print()
            print("❌ Company name cannot be empty.")
            return

        print()
        print("Searching company database...")
        print()

        profile = self.provider.search(
            company
        )

        if profile is None:

            print("=" * 70)
            print("Company Not Found")
            print("=" * 70)
            print(
                "Currently available companies:"
            )

            print()

            for company_name in [

                "Microsoft",
                "Google",
                "OpenAI",
                "Salesforce",
                "Freshworks",

            ]:

                print(f"• {company_name}")

            print()

            return

        profile.display()