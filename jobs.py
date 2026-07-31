from profile_1 import save_profile
from history import save_search_history

import webbrowser
import urllib.parse


def find_jobs(name):

    print()
    print("========== JobHunter AI ==========")

    print("Where would you like to search?")
    print("1. LinkedIn")
    print("2. Naukri")
    print("3. Indeed")
    print("4. Foundit")
    print("5. Remote Jobs")
    print()

    platforms = {
        "1": "LinkedIn",
        "2": "Naukri",
        "3": "Indeed",
        "4": "Foundit",
        "5": "RemoteOK"
    }

    while True:

        platform = input("Choose a platform (1-5): ")

        if platform in platforms:
            break

        print("❌ Invalid choice. Please enter a number between 1 and 5.")

    print()

    role = input("What role are you looking for? ")

    locations = input(
        "Preferred locations (comma separated if multiple): "
    )

    experience = input("Years of experience: ")

    location_list = [location.strip() for location in locations.split(",")]

    print()
    print("========== Search Summary ==========")
    print("Platform :", platforms[platform])
    print("Role :", role)
    print("Locations :", ", ".join(location_list))
    print("Experience :", experience)
    print()

    print("🚀 Opening search tabs...\n")

    for location in location_list:

        role_encoded = urllib.parse.quote(role)
        location_encoded = urllib.parse.quote(location)

        if platform == "1":

            print(f"✔ LinkedIn -> {location}")

            url = (
                f"https://www.linkedin.com/jobs/search/"
                f"?keywords={role_encoded}"
                f"&location={location_encoded}"
            )

        elif platform == "2":

            print(f"✔ Naukri -> {location}")

            url = (
                f"https://www.naukri.com/{role_encoded}-jobs-in-{location_encoded}"
            )

        elif platform == "3":

            print(f"✔ Indeed -> {location}")

            url = (
                f"https://in.indeed.com/jobs?q={role_encoded}&l={location_encoded}"
            )

        elif platform == "4":

            print(f"✔ Foundit -> {location}")

            url = (
                f"https://www.foundit.in/srp/results?query={role_encoded}&locations={location_encoded}"
            )

        else:

            print(f"✔ RemoteOK -> {location}")

            url = (
                f"https://remoteok.com/remote-{role_encoded}-jobs"
            )

        webbrowser.open_new_tab(url)

    search_id = save_search_history(
        platforms[platform],
        role,
        locations,
        experience
    )

    print()
    print("✅ All searches have been opened successfully.")
    print(f"📁 Search saved successfully.")
    print(f"🆔 Search ID : {search_id}")

    save_profile(name, role, locations, experience)