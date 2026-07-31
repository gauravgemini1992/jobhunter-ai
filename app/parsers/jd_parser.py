import re

from app.data.skills import SKILLS
from app.engines.smart_skill_matcher import SmartSkillMatcher
from app.models.jd_model import JDModel


class JDParser:
    """
    Parses a Job Description into a structured JDModel.
    """

    def __init__(self):
        self.matcher = SmartSkillMatcher()

    def parse(self, jd_text: str) -> JDModel:

        jd_text = jd_text.lower()

        jd = JDModel()

        # -----------------------------
        # Job Title
        # -----------------------------

        lines = [line.strip() for line in jd_text.split("\n") if line.strip()]

        if lines:
            jd.job_title = lines[0].title()

        # -----------------------------
        # Skills
        # -----------------------------

        for _, skill_list in SKILLS.items():

            for skill in skill_list:

                if self.matcher.match(jd_text, skill):
                    jd.skills.append(skill)

        jd.skills = sorted(list(set(jd.skills)))

        # -----------------------------
        # Experience
        # -----------------------------

        experience = re.findall(
            r"(\d+)\+?\s*(?:years|yrs)",
            jd_text
        )

        if experience:
            jd.experience = max(map(int, experience))

        # -----------------------------
        # Education
        # -----------------------------

        education_keywords = [

            "mba",
            "b.tech",
            "btech",
            "be",
            "b.e",
            "mca",
            "bca",
            "engineering",
            "computer science"

        ]

        for edu in education_keywords:

            if edu in jd_text:
                jd.education.append(edu)

        # -----------------------------
        # Responsibilities
        # -----------------------------

        action_words = [

            "manage",
            "drive",
            "lead",
            "build",
            "maintain",
            "develop",
            "support",
            "deliver",
            "collaborate",
            "own"

        ]

        for line in lines:

            normalized = line.lower().lstrip("-•* ").strip()

            if len(normalized) < 10:
                continue

            for word in action_words:

                if normalized.startswith(word):

                    jd.responsibilities.append(normalized)
                    break

        jd.responsibilities = list(dict.fromkeys(jd.responsibilities))

        jd.keywords = jd.skills.copy()

        return jd