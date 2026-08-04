"""
============================================================
JobHunter AI
Version : 1.0.0
Author  : Gaurav Hegde

Main Application Entry Point
============================================================
"""

from menu import show_menu
from profile_1 import (
    load_profile,
    save_profile,
)

from app.services.job_finder_service import JobFinderService
from app.services.resume_review_service import ResumeReviewService
from app.services.company_research_service import (
    CompanyResearchService,
)


# ==========================================================
# User Profile Setup
# ==========================================================


def setup_profile():

    profile = load_profile()

    if profile:

        try:

            name = profile.split("\n")[0].split(": ")[1]

        except Exception:

            name = "User"

        print(f"\n👋 Welcome back, {name}!")

        print("\n1. Use Saved Profile")
        print("2. Update Profile\n")

        while True:

            choice = input(
                "Enter your choice (1 or 2): "
            ).strip()

            if choice == "1":

                return name

            elif choice == "2":

                print()
                print("=" * 60)
                print("UPDATE PROFILE")
                print("=" * 60)

                name = input(
                    "Enter your name: "
                ).strip()

                role = input(
                    "Enter your role: "
                ).strip()

                location = input(
                    "Enter your location: "
                ).strip()

                experience = input(
                    "Enter your experience: "
                ).strip()

                save_profile(
                    name,
                    role,
                    location,
                    experience,
                )

                print()
                print("✅ Profile Updated Successfully.\n")

                return name

            else:

                print(
                    "\n❌ Invalid choice. Please try again.\n"
                )

    # ------------------------------------------------------
    # First Time User
    # ------------------------------------------------------

    print("\n👋 Welcome to JobHunter AI\n")

    name = input(
        "Enter your name: "
    ).strip()

    role = input(
        "Enter your role: "
    ).strip()

    location = input(
        "Enter your location: "
    ).strip()

    experience = input(
        "Enter your experience: "
    ).strip()

    save_profile(
        name,
        role,
        location,
        experience,
    )

    print()
    print("✅ Profile Created Successfully.\n")

    return name


# ==========================================================
# Main Application
# ==========================================================


def main():

    print("=" * 60)
    print("🚀                 JOBHUNTER AI")
    print("=" * 60)

    setup_profile()

    while True:

        choice = show_menu()

        # --------------------------------------------------
        # Find Matching Jobs
        # --------------------------------------------------

        if choice == "1":

            JobFinderService().run()

        # --------------------------------------------------
        # Resume Review
        # --------------------------------------------------

        elif choice == "2":

            ResumeReviewService().run()

        # --------------------------------------------------
        # Company Research
        # --------------------------------------------------

        elif choice == "3":

            CompanyResearchService().run()

        # --------------------------------------------------
        # Exit
        # --------------------------------------------------

        elif choice == "4":

            print()
            print("👋 Thank you for using JobHunter AI.")
            print("See you again!\n")

            break

        else:

            print()

            print("❌ Invalid Choice.")

            print()


# ==========================================================

if __name__ == "__main__":

    main()