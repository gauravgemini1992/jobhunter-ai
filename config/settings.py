"""
Application Configuration
JobHunter AI
"""

import os
from pathlib import Path

# --------------------------------------------------
# Load .env manually
# --------------------------------------------------

def load_env():

    env_file = Path(".env")

    if not env_file.exists():
        return

    for line in env_file.read_text().splitlines():

        line = line.strip()

        if not line:
            continue

        if line.startswith("#"):
            continue

        if "=" not in line:
            continue

        key, value = line.split("=", 1)

        os.environ[key.strip()] = value.strip()


load_env()

# --------------------------------------------------
# Application
# --------------------------------------------------

APP_NAME = "JobHunterAI"

VERSION = "1.0.0"

AUTHOR = "Gaurav Hegde"

OUTPUT_DIR = "output"

REPORT_NAME = "ATS_Report"

PDF_TITLE = "Resume Analysis Report"

PDF_SUBTITLE = "AI Powered ATS Resume Evaluation"

PRIMARY_COLOR = "#0A66C2"

SECONDARY_COLOR = "#4CAF50"

PAGE_SIZE = "A4"

ENABLE_PDF = True

# --------------------------------------------------
# Adzuna
# --------------------------------------------------

ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID", "")

ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY", "")

ADZUNA_COUNTRY = "in"

ADZUNA_RESULTS_PER_PAGE = 50

ADZUNA_TIMEOUT = 20