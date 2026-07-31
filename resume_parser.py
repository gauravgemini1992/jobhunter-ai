import re

from resume_reader import read_resume
from section_aliases import SECTION_ALIASES
from models.personal import Personal
from models.experience import Experience
from experience_parser import parse_experience


def find_section(lines, aliases):
    """
    Finds the starting line number of a resume section.
    Returns -1 if the section is not found.
    """

    for index, line in enumerate(lines):

        clean_line = line.strip().lower()

        for alias in aliases:
            if clean_line == alias.lower():
                return index

    return -1


def extract_section(lines, start_index):
    """
    Extracts all lines belonging to a section until the next section begins.
    """

    collected = []

    for line in lines[start_index + 1:]:

        lower = line.strip().lower()

        is_new_section = False

        for alias_list in SECTION_ALIASES.values():

            if lower in [alias.lower() for alias in alias_list]:
                is_new_section = True
                break

        if is_new_section:
            break

        collected.append(line)

    return "\n".join(collected).strip()


def parse_resume(file_path):
    """
    Reads and parses the resume into structured objects.
    """

    resume = read_resume(file_path)

    lines = resume.splitlines()

    person = Personal()

    experiences = []

    data = {
        "personal": person,
        "summary": "",
        "experience": experiences,
        "education": "",
        "skills": "",
        "projects": "",
        "certifications": ""
    }

    email = re.findall(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        resume
    )

    phone = re.findall(
        r"(\+?\d[\d\s\-]{8,}\d)",
        resume
    )

    person.name = lines[0].strip() if lines else ""
    person.email = email[0] if email else ""
    person.phone = phone[0] if phone else ""

    for section, aliases in SECTION_ALIASES.items():

        location = find_section(lines, aliases)

        if location == -1:
            continue

        section_text = extract_section(lines, location)

        if section == "experience":

            parsed_jobs = parse_experience(section_text)

            for job in parsed_jobs:

                exp = Experience()

                exp.company = job["company"]
                exp.designation = job["designation"]
                exp.duration = job["duration"]
                exp.description = job["description"]

                experiences.append(exp)

        else:

            data[section] = section_text

    return data


if __name__ == "__main__":

    data = parse_resume("resume.docx")

    print("=" * 70)
    print("                      JOBHUNTER AI")
    print("=" * 70)

    print("\nPERSONAL DETAILS")
    print("-" * 70)
    print(f"Name      : {data['personal'].name}")
    print(f"Email     : {data['personal'].email}")
    print(f"Phone     : {data['personal'].phone}")

    print("\nEXPERIENCE")
    print("-" * 70)

    if data["experience"]:

        for index, exp in enumerate(data["experience"], start=1):

            print(f"\nExperience #{index}")
            print(f"Designation : {exp.designation}")
            print(f"Company     : {exp.company}")
            print(f"Duration    : {exp.duration}")

            if exp.description:
                print("\nResponsibilities:")

                for line in exp.description:
                    print(f"• {line}")

    else:
        print("No experience found.")

    print("\nEDUCATION")
    print("-" * 70)
    print(data["education"])

    print("\nSKILLS")
    print("-" * 70)
    print(data["skills"])

    print("\nPROJECTS")
    print("-" * 70)
    print(data["projects"])

    print("\nCERTIFICATIONS")
    print("-" * 70)
    print(data["certifications"])