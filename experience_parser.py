import re


def is_job_header(line):
    """
    Determines whether a line represents a job header.

    Example:
    Senior Key Account Manager | Galaxy Weblinks, Remote Since May 2025
    Business Development Manager | CloudoPlus, Remote Jun 2024 – Jan 2025
    """

    if "|" not in line:
        return False

    return bool(
        re.search(
            r"(Since\s+[A-Za-z]+\s+\d{4}|[A-Za-z]{3}\s+\d{4}|Present|\d{4})",
            line,
            re.IGNORECASE,
        )
    )


def split_header(header):
    """
    Splits the header into:
    Designation
    Company
    Duration
    """

    parts = [p.strip() for p in header.split("|")]

    designation = ""
    company = ""
    duration = ""

    if len(parts) >= 3:

        designation = parts[0]
        company = parts[1]
        duration = "|".join(parts[2:]).strip()

    elif len(parts) == 2:

        designation = parts[0]

        right = parts[1]

        duration_match = re.search(
            r"(Since\s+[A-Za-z]+\s+\d{4}|[A-Za-z]{3}\s+\d{4}\s*[–-]\s*(?:Present|[A-Za-z]{3}\s+\d{4}))",
            right,
            re.IGNORECASE,
        )

        if duration_match:

            duration = duration_match.group(0)

            company = right[:duration_match.start()].strip(" ,")

        else:

            company = right

    else:

        designation = header

    return designation, company, duration


def parse_experience(experience_text):
    """
    Parses the Work Experience section into structured jobs.
    """

    if not experience_text.strip():
        return []

    lines = [
        line.strip()
        for line in experience_text.splitlines()
        if line.strip()
    ]

    jobs = []

    current_job = None

    for line in lines:

        # -------------------------
        # Earlier Career Section
        # -------------------------

        if line.upper().startswith("EARLIER CAREER"):

            if current_job:
                jobs.append(current_job)

            year_match = re.search(r"\((.*?)\)", line)

            duration = ""

            if year_match:
                duration = year_match.group(1)

            current_job = {
                "designation": "Earlier Career",
                "company": "Multiple Companies",
                "duration": duration,
                "description": []
            }

            continue

        # -------------------------
        # New Job Header
        # -------------------------

        if is_job_header(line):

            if current_job:
                jobs.append(current_job)

            designation, company, duration = split_header(line)

            current_job = {
                "designation": designation,
                "company": company,
                "duration": duration,
                "description": []
            }

            continue

        # -------------------------
        # Job Description
        # -------------------------

        if current_job:

            current_job["description"].append(line)

    if current_job:
        jobs.append(current_job)

    return jobs