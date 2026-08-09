"""
============================================================
JobHunter AI
Profile Manager
============================================================
"""

import os

PROFILE_FILE = "profile.txt"


def load_profile():
    """
    Load the saved user profile.

    Returns:
        dict | None
    """

    if not os.path.exists(PROFILE_FILE):
        return None

    profile = {}

    with open(PROFILE_FILE, "r") as file:

        for line in file:

            line = line.strip()

            if not line:

                continue

            if ":" not in line:

                continue

            key, value = line.split(":", 1)

            profile[
                key.strip().lower().replace(" ", "_")
            ] = value.strip()

    return profile


def save_profile(
    name,
    role,
    location,
    experience,
):
    """
    Save the user profile.
    """

    with open(PROFILE_FILE, "w") as file:

        file.write(f"Name: {name}\n")
        file.write(f"Role: {role}\n")
        file.write(f"Location: {location}\n")
        file.write(f"Experience: {experience}\n")

    print("✅ Profile saved successfully!")


def profile_exists():
    """
    Returns True if a profile exists.
    """

    return os.path.exists(PROFILE_FILE)