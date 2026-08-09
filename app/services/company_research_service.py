"""
============================================================
JobHunter AI
Company Research Service
============================================================
"""

from app.providers.live_company_provider import LiveCompanyProvider


class CompanyResearchService:
    """
    Company Research Service

    Fetches and displays company information.
    """

    def __init__(self):

        self.provider = LiveCompanyProvider()

    # ==================================================

    def run(self):

        print()
        print("=" * 70)
        print("COMPANY RESEARCH")
        print("=" * 70)

        print()
        print("Research a company before applying.")
        print()

        company = input(
            "Enter Company Name : "
        ).strip()

        if not company:

            print()
            print("❌ Company name cannot be empty.")
            print()

            return

        print()
        print(f"🔍 Researching '{company}'...")
        print()

        profile = self.provider.search(
            company
        )

        if profile is None:

            print()
            print("=" * 70)
            print("COMPANY NOT FOUND")
            print("=" * 70)

            print()
            print("Try searching for another company.")
            print()

            return

        print()

        # CompanyProfile.display() already prints
        # the COMPANY PROFILE header.
        profile.display()

        print()
        print("=" * 70)
        print("✅ Company Research Completed")
        print("=" * 70)