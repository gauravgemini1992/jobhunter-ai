import re

from resume_parser import parse_resume
from skills_database import skills
from ats_engine import ATSEngine
from report_generator import ReportGenerator


def extract_job_title(jd):
    """
    Extracts the job title from the first non-empty line.
    """
    lines = [line.strip() for line in jd.split("\n") if line.strip()]

    if lines:
        return lines[0]

    return "Unknown"


def extract_experience(jd):
    """
    Extracts required years of experience.
    """

    patterns = [
        r"(\d+)\+?\s*years",
        r"minimum\s*(\d+)\s*years",
        r"at least\s*(\d+)\s*years",
    ]

    for pattern in patterns:

        match = re.search(pattern, jd, re.IGNORECASE)

        if match:
            return int(match.group(1))

    return 0


def extract_education(jd):
    """
    Extracts education requirement.
    """

    education_keywords = [
        "bachelor",
        "master",
        "mba",
        "b.tech",
        "be",
        "engineering",
    ]

    jd = jd.lower()

    for item in education_keywords:

        if item in jd:
            return item.title()

    return ""


def extract_skills(jd):
    """
    Extract mandatory and preferred skills from the JD.
    """

    mandatory = []
    preferred = []

    jd_lower = jd.lower()

    for _, skill_list in skills.items():

        for skill in skill_list:

            if skill.lower() in jd_lower:
                mandatory.append(skill.title())

    preferred_words = [
        "good to have",
        "preferred",
        "nice to have",
    ]

    if any(word in jd_lower for word in preferred_words):

        preferred = mandatory[-5:]

    return sorted(set(mandatory)), sorted(set(preferred))


def extract_responsibilities(jd):
    """
    Extract bullet-point responsibilities.
    """

    responsibilities = []

    for line in jd.split("\n"):

        line = line.strip()

        if not line:
            continue

        if line.startswith("-"):
            responsibilities.append(line[1:].strip())

        elif line.startswith("•"):
            responsibilities.append(line[1:].strip())

    return responsibilities


def analyze_job_description():
    """
    Main ATS Analysis Flow
    """

    try:
        resume = parse_resume("resume.docx")

    except FileNotFoundError:

        print("❌ resume.docx not found.")
        return

    print()
    print("=" * 70)
    print("Paste the Job Description")
    print("Press ENTER twice when finished.")
    print("=" * 70)
    print()

    lines = []

    while True:

        line = input()

        if line == "":
            break

        lines.append(line)

    jd = "\n".join(lines)

    mandatory, preferred = extract_skills(jd)

    job = {

        "job_title": extract_job_title(jd),

        "experience_required": extract_experience(jd),

        "education": extract_education(jd),

        "mandatory_skills": mandatory,

        "preferred_skills": preferred,

        "responsibilities": extract_responsibilities(jd)

    }

    ats = ATSEngine(resume, job)

    report = ats.calculate_score()

    generator = ReportGenerator(report, job)

    generator.print_report()


if __name__ == "__main__":

    analyze_job_description()