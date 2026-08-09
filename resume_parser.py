"""
============================================================
JobHunter AI
Resume Parser
============================================================
"""

import os
import re

from resume_reader import read_resume
from section_aliases import SECTION_ALIASES
from experience_parser import parse_experience

from app.models.personal import Personal
from app.models.experience import Experience


# ==========================================================
# Section Finder
# ==========================================================

def find_section(lines, aliases):
    """
    Find the starting index of a section.
    """

    for index, line in enumerate(lines):

        clean_line = line.strip().lower()

        for alias in aliases:

            if clean_line == alias.lower():

                return index

    return -1


# ==========================================================
# Section Extractor
# ==========================================================

def extract_section(lines, start_index):
    """
    Extract all text belonging to a section.
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


# ==========================================================
# Resume Parser
# ==========================================================

def parse_resume(file_path):
    """
    Parse a DOCX resume into structured data.
    """

    if not file_path:

        raise FileNotFoundError(
            "No resume path supplied."
        )

    if not os.path.exists(file_path):

        raise FileNotFoundError(
            f"Resume not found:\n{file_path}"
        )

    resume = read_resume(file_path)

    if not resume:

        raise ValueError(
            "Resume is empty or unreadable."
        )

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
        "certifications": "",

    }

    # ------------------------------------------------------
    # Personal Details
    # ------------------------------------------------------

    email = re.findall(

        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",

        resume,

    )

    phone = re.findall(

        r"(\+?\d[\d\s\-]{8,}\d)",

        resume,

    )

    person.name = lines[0].strip() if lines else ""
    person.email = email[0] if email else ""
    person.phone = phone[0] if phone else ""

    # ------------------------------------------------------
    # Sections
    # ------------------------------------------------------

    for section, aliases in SECTION_ALIASES.items():

        location = find_section(

            lines,

            aliases,

        )

        if location == -1:
            continue

        section_text = extract_section(

            lines,

            location,

        )

        if section == "experience":

            parsed_jobs = parse_experience(
                section_text
            )

            for job in parsed_jobs:

                exp = Experience()

                exp.company = job.get(
                    "company",
                    "",
                )

                exp.designation = job.get(
                    "designation",
                    "",
                )

                exp.duration = job.get(
                    "duration",
                    "",
                )

                exp.description = job.get(
                    "description",
                    [],
                )

                experiences.append(exp)

        else:

            data[section] = section_text

    return data


# ==========================================================
# Standalone Test
# ==========================================================

if __name__ == "__main__":

    from profile_manager import get_resume_path

    resume_path = get_resume_path()

    if not resume_path:

        print()
        print("❌ No resume configured.")
        print("Run main.py and update your profile.")
        exit()

    print()
    print("=" * 70)
    print("JOBHUNTER AI - RESUME PARSER")
    print("=" * 70)

    try:

        data = parse_resume(resume_path)

    except Exception as error:

        print()
        print("❌ Failed to parse resume.")
        print(error)
        exit()

    print()
    print("PERSONAL DETAILS")
    print("-" * 70)
    print(f"Name      : {data['personal'].name}")
    print(f"Email     : {data['personal'].email}")
    print(f"Phone     : {data['personal'].phone}")

    print()
    print("EXPERIENCE")
    print("-" * 70)

    if data["experience"]:

        for index, exp in enumerate(
            data["experience"],
            start=1,
        ):

            print(f"\nExperience #{index}")
            print(f"Designation : {exp.designation}")
            print(f"Company     : {exp.company}")
            print(f"Duration    : {exp.duration}")

            if exp.description:

                print("Responsibilities:")

                if isinstance(exp.description, list):

                    for line in exp.description:
                        print(f" • {line}")

                else:

                    print(exp.description)

    else:

        print("No experience found.")

    print()
    print("SUMMARY")
    print("-" * 70)
    print(data["summary"])

    print()
    print("SKILLS")
    print("-" * 70)
    print(data["skills"])

    print()
    print("EDUCATION")
    print("-" * 70)
    print(data["education"])

    print()
    print("PROJECTS")
    print("-" * 70)
    print(data["projects"])

    print()
    print("CERTIFICATIONS")
    print("-" * 70)
    print(data["certifications"])

    print()
    print("=" * 70)
    print("✅ Resume Parsed Successfully")
    print("=" * 70)