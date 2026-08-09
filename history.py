from datetime import datetime
import os


def generate_search_id():

    if not os.path.exists("search_history.txt"):
        return "JOB-0001"

    count = 0

    with open("search_history.txt", "r") as file:
        for line in file:
            if line.startswith("Search ID"):
                count += 1

    return f"JOB-{count + 1:04d}"


def save_search_history(platform, role, locations, experience):

    search_id = generate_search_id()

    current_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    with open("search_history.txt", "a") as file:

        file.write("=" * 50 + "\n")
        file.write(f"Search ID : {search_id}\n")
        file.write(f"Date : {current_time}\n")
        file.write(f"Platform : {platform}\n")
        file.write(f"Role : {role}\n")
        file.write(f"Locations : {locations}\n")
        file.write(f"Experience : {experience}\n")
        file.write("=" * 50 + "\n\n")

    return search_id