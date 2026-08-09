from __future__ import annotations

import logging
from typing import Dict, List, Tuple

from app.engines.smart_skill_matcher import SmartSkillMatcher
from app.models.ats_report import ATSReport
from app.models.jd_model import JDModel
from app.models.recommendation import Recommendation
from app.utils.scoring import (
    overall_score,
    percentage,
    strengths,
    weaknesses,
)
from app.data.skill_families import SKILL_FAMILIES

logger = logging.getLogger(__name__)


class ATSEngine:
    """
    Core ATS Matching Engine.

    Responsibilities
    ----------------
    - Build searchable resume text
    - Calculate ATS component scores
    - Generate strengths & weaknesses
    - Generate recommendations
    - Produce the final ATS report
    """

    def __init__(self) -> None:
        self.matcher = SmartSkillMatcher()

    # ------------------------------------------------------------------
    # Resume Processing
    # ------------------------------------------------------------------

    def _build_resume_text(self, resume: Dict) -> str:
        """
        Convert structured resume data into a searchable text blob.
        """

        sections: List[str] = []

        for field in ("summary", "skills", "education"):
            value = resume.get(field)
            if value:
                sections.append(str(value))

        for experience in resume.get("experience", []):

            # Experience object from resume_parser.py
            if hasattr(experience, "designation"):

                description = experience.description

                if isinstance(description, list):
                    description = " ".join(description)

                sections.extend(
                    filter(
                        None,
                        [
                            experience.designation,
                            experience.company,
                            experience.duration,
                            description,
                        ],
                    )
                )

            # Dictionary support
            elif isinstance(experience, dict):

                description = experience.get("description")

                if isinstance(description, list):
                    description = " ".join(description)

                sections.extend(
                    filter(
                        None,
                        [
                            experience.get("designation"),
                            experience.get("company"),
                            experience.get("duration"),
                            description,
                        ],
                    )
                )

            else:

                sections.append(str(experience))

        return "\n".join(sections).lower()
    # ------------------------------------------------------------------
    # Generic Matching
    # ------------------------------------------------------------------

    def _match_items(
        self,
        items: List[str],
        resume_text: str,
    ) -> Tuple[int, List[str], List[str]]:
        """
        Smart matching with Skill Family support.

        If one member of a family matches, the family is counted once.
        """

        matched: List[str] = []
        missing: List[str] = []

        matched_families = set()
        seen = set()

        for item in items:

            item = item.strip()

            if not item:
                continue

            normalized = item.lower()

            if normalized in seen:
                continue

            seen.add(normalized)

            family_name = None

            # -----------------------------------
            # Find the family (if any)
            # -----------------------------------

            for family, members in SKILL_FAMILIES.items():

                if normalized in members:
                    family_name = family
                    break

            # -----------------------------------
            # Family Match
            # -----------------------------------

            if family_name:

                if family_name in matched_families:
                    matched.append(item)
                    continue

                family_members = SKILL_FAMILIES[family_name]

                found = False

                for member in family_members:

                    if self.matcher.match(
                        member,
                        resume_text,
                    ):
                        found = True
                        break

                if found:

                    matched.append(item)
                    matched_families.add(family_name)

                else:

                    missing.append(item)

            # -----------------------------------
            # Normal Skill
            # -----------------------------------

            else:

                if self.matcher.match(
                    item,
                    resume_text,
                ):
                    matched.append(item)

                else:
                    missing.append(item)

        score = percentage(
            len(matched),
            len(seen),
        )

        return (
            score,
            matched,
            missing,
        )
        # ------------------------------------------------------------------
    # Skill Score
    # ------------------------------------------------------------------

    def _calculate_skill_score(
        self,
        resume_text: str,
        jd: JDModel,
    ) -> Tuple[int, List[str], List[str]]:

        return self._match_items(jd.skills, resume_text)

    # ------------------------------------------------------------------
    # Responsibility Score
    # ------------------------------------------------------------------

    def _calculate_responsibility_score(
        self,
        resume_text: str,
        jd: JDModel,
    ) -> Tuple[int, List[str], List[str]]:

        matched = []
        missing = []

        for responsibility in jd.responsibilities:

            text = responsibility.lower()

            words = [
                word
                for word in text.replace(".", "").replace(",", "").split()
                if len(word) > 3
            ]

            hits = 0

            for word in words:

                if word in resume_text:
                    hits += 1

            if hits >= max(2, len(words) // 3):
                matched.append(responsibility)
            else:
                missing.append(responsibility)

        score = percentage(
            len(matched),
            len(jd.responsibilities),
        )

        return (
            score,
            matched,
            missing,
        )
    # ------------------------------------------------------------------
    # Experience Score
    # ------------------------------------------------------------------

    def _calculate_experience_score(
        self,
        resume: Dict,
        jd: JDModel,
    ) -> int:
        """
        Current implementation estimates experience from the
        number of experience entries.
        """

        resume_experience = len(resume.get("experience", []))

        if jd.experience is None:
            return 100

        if jd.experience <= 0:
            return 100

        if resume_experience >= jd.experience:
            return 100

        return round(
            (resume_experience / jd.experience) * 100
        )

    # ------------------------------------------------------------------
    # Education Score
    # ------------------------------------------------------------------

    def _calculate_education_score(
        self,
        resume: Dict,
        jd: JDModel,
    ) -> int:

        if not jd.education:
            return 100

        education_text = str(
            resume.get("education", "")
        ).lower()

        matched = sum(
            1
            for degree in jd.education
            if degree.lower() in education_text
        )

        return percentage(
            matched,
            len(jd.education),
        )

    # ------------------------------------------------------------------
    # Keyword Score
    # ------------------------------------------------------------------

    def _calculate_keyword_score(
        self,
        resume_text: str,
        jd: JDModel,
    ) -> int:

        if not jd.keywords:
            return 100

        matched = sum(
            1
            for keyword in jd.keywords
            if self.matcher.match(
                keyword,
                resume_text,
            )
        )

        return percentage(
            matched,
            len(jd.keywords),
        )

    # ------------------------------------------------------------------
    # Strengths
    # ------------------------------------------------------------------

    def _generate_strengths(
        self,
        matched_skills: List[str],
    ) -> List[str]:

        return strengths(matched_skills)

    # ------------------------------------------------------------------
    # Weaknesses
    # ------------------------------------------------------------------

    def _generate_weaknesses(
        self,
        missing_skills: List[str],
    ) -> List[str]:

        return weaknesses(missing_skills)

    # ------------------------------------------------------------------
    # Recommendations
    # ------------------------------------------------------------------

    def _generate_recommendations(
        self,
        missing_skills: List[str],
        missing_responsibilities: List[str],
    ) -> List[Recommendation]:

        recommendations: List[Recommendation] = []

        handled_families = set()

        for skill in missing_skills:

            family_name = None

            for family, members in SKILL_FAMILIES.items():

                if skill.lower() in members:
                    family_name = family
                    break

            if family_name:

                if family_name in handled_families:
                    continue

                handled_families.add(family_name)

                recommendations.append(
                    Recommendation(
                        skill=family_name,
                        priority="HIGH",
                        message=(
                            f"Consider adding experience with "
                            f"'{family_name}' related technologies if applicable."
                        ),
                    )
                )

            else:

                recommendations.append(
                    Recommendation(
                        skill=skill,
                        priority="HIGH",
                        message=(
                            f"Consider adding experience with "
                            f"'{skill}' if applicable."
                        ),
                    )
                )
        for responsibility in missing_responsibilities:

            recommendations.append(
                Recommendation(
                    skill=responsibility,
                    priority="MEDIUM",
                    message=(
                        f"Highlight work related to "
                        f"'{responsibility}' if applicable."
                    ),
                )
            )

        if not recommendations:

            recommendations.append(
                Recommendation(
                    skill="Profile",
                    priority="LOW",
                    message=(
                        "Excellent alignment with the "
                        "job description."
                    ),
                )
            )

        return recommendations

    # ------------------------------------------------------------------
    # Main ATS Calculation
    # ------------------------------------------------------------------

    def calculate_match(
        self,
        resume: Dict,
        jd: JDModel,
    ) -> ATSReport:

        logger.info(
            "Starting ATS calculation for '%s'",
            jd.job_title,
        )

        resume_text = self._build_resume_text(
            resume
        )

        (
            skill_score,
            matched_skills,
            missing_skills,
        ) = self._calculate_skill_score(
            resume_text,
            jd,
        )

        experience_score = (
            self._calculate_experience_score(
                resume,
                jd,
            )
        )

        education_score = (
            self._calculate_education_score(
                resume,
                jd,
            )
        )

        (
            responsibility_score,
            matched_responsibilities,
            missing_responsibilities,
        ) = self._calculate_responsibility_score(
            resume_text,
            jd,
        )

        keyword_score = (
            self._calculate_keyword_score(
                resume_text,
                jd,
            )
        )

        final_score = overall_score(
            skill_score,
            experience_score,
            education_score,
            responsibility_score,
            keyword_score,
        )

        report = ATSReport(
            overall_score=final_score,
            skill_score=skill_score,
            experience_score=experience_score,
            education_score=education_score,
            responsibility_score=responsibility_score,
            keyword_score=keyword_score,
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            matched_responsibilities=matched_responsibilities,
            missing_responsibilities=missing_responsibilities,
            strengths=self._generate_strengths(
                matched_skills,
            ),
            weaknesses=self._generate_weaknesses(
                missing_skills,
            ),
            recommendations=self._generate_recommendations(
                missing_skills,
                missing_responsibilities,
            ),
        )

        logger.info(
            "ATS completed. Final score: %s",
            final_score,
        )

        return report