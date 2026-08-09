"""
============================================================
JobHunter AI
Version : 1.0.0
Author  : Gaurav Hegde

Main Application Entry Point
============================================================
"""

import os

from menu import show_menu

from profile_manager import (
    load_profile,
    save_profile,
)

from resume_parser import parse_resume

from app.session import Session

from app.services.job_finder_service import JobFinderService
from app.services.resume_review_service import ResumeReviewService
from app.services.company_research_service import (
    CompanyResearchService,
)


# ==========================================================
# Resume Loader
# ==========================================================


def ask_resume_path():
    """
    Ask the user for a valid DOCX resume.
    """

    while True:

        print()

        resume_path = input(
            "Enter the full path to your resume (.docx): "
        ).strip()

        if not resume_path:

            print("❌ Resume path cannot be empty.")
            continue

        resume_path = os.path.abspath(resume_path)

        if not os.path.exists(resume_path):

            print("❌ File not found.")
            continue

        if not resume_path.lower().endswith(".docx"):

            print("❌ Only DOCX resumes are supported.")
            continue

        return resume_path


# ==========================================================


def load_resume():
    """
    Load and parse the resume once per application session.
    """

    while True:

        resume_path = ask_resume_path()

        try:

            print()
            print("Loading Resume...")

            Session.resume_path = resume_path

            Session.resume = parse_resume(
                resume_path
            )

            print("✅ Resume loaded successfully.\n")

            return

        except Exception as error:

            print()
            print("❌ Failed to read resume.")
            print(error)
            print()


# ==========================================================
# Profile Creation
# ==========================================================


def create_profile():

    print()
    print("=" * 60)
    print("CREATE PROFILE")
    print("=" * 60)

    name = input(
        "Enter your name: "
    ).strip()

    role = input(
        "Enter your current role: "
    ).strip()

    location = input(
        "Enter your location: "
    ).strip()

    experience = input(
        "Enter your experience (Years): "
    ).strip()

    save_profile(

        name,

        role,

        location,

        experience,

    )

    print()
    print("✅ Profile created successfully.\n")

    return {

        "name": name,

        "role": role,

        "location": location,

        "experience": experience,

    }


# ==========================================================


def update_profile():

    print()
    print("=" * 60)
    print("UPDATE PROFILE")
    print("=" * 60)

    name = input(
        "Enter your name: "
    ).strip()

    role = input(
        "Enter your current role: "
    ).strip()

    location = input(
        "Enter your location: "
    ).strip()

    experience = input(
        "Enter your experience (Years): "
    ).strip()

    save_profile(

        name,

        role,

        location,

        experience,

    )

    print()
    print("✅ Profile updated successfully.\n")

    return {

        "name": name,

        "role": role,

        "location": location,

        "experience": experience,

    }


# ==========================================================


def setup_profile():

    profile = load_profile()

    if not profile:

        print()
        print("👋 Welcome to JobHunter AI")

        return create_profile()

    print(
        f"\n👋 Welcome back, {profile.get('name', 'User')}!"
    )

    while True:

        print()
        print("1. Continue")
        print("2. Update Profile")
        print()

        choice = input(
            "Enter your choice (1-2): "
        ).strip()

        if choice == "1":

            return profile

        if choice == "2":

            return update_profile()

        print()
        print("❌ Invalid choice.")


# ==========================================================
# Main Application
# ==========================================================


def main():

    print("=" * 60)
    print("🚀                 JOBHUNTER AI")
    print("=" * 60)

    # ------------------------------------------------------
    # Load Profile
    # ------------------------------------------------------

    Session.profile = setup_profile()

    # ------------------------------------------------------
    # Load Resume
    # ------------------------------------------------------

    load_resume()

    # ------------------------------------------------------
    # Main Menu
    # ------------------------------------------------------

    while True:

        choice = show_menu()

        if choice == "1":

            JobFinderService().run()

        elif choice == "2":

            ResumeReviewService().run()

        elif choice == "3":

            CompanyResearchService().run()

        elif choice == "4":

            print()
            print("👋 Thank you for using JobHunter AI.")
            print("See you again!\n")

            Session.reset()

            break

        else:

            print()
            print("❌ Invalid Choice.\n")


# ==========================================================

if __name__ == "__main__":

    main()