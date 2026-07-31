from typing import List

from app.engines.smart_skill_matcher import SmartSkillMatcher
from app.models.ats_report import ATSReport
from app.models.jd_model import JDModel
from app.models.recommendation import Recommendation
from app.utils.scoring import (
    percentage,
    overall_score,
    strengths,
    weaknesses,
)


class ATSEngine:
    """
    Core ATS Matching Engine
    """

    def __init__(self):
        self.matcher = SmartSkillMatcher()

    # ----------------------------------------------------
    # Build searchable resume text
    # ----------------------------------------------------

    def _build_resume_text(self, resume: dict) -> str:

        text = ""

        text += resume.get("summary", "") + "\n"
        text += resume.get("skills", "") + "\n"
        text += resume.get("education", "") + "\n"

        for exp in resume.get("experience", []):

            if isinstance(exp, dict):

                text += exp.get("title", "") + "\n"
                text += exp.get("company", "") + "\n"
                text += exp.get("description", "") + "\n"

            else:

                text += str(exp) + "\n"

        return text.lower()

    # ----------------------------------------------------
    # Skill Matching
    # ----------------------------------------------------

    def _calculate_skill_score(
        self,
        resume_text: str,
        jd: JDModel,
    ):

        matched = []
        missing = []

        for skill in jd.skills:

            if self.matcher.match(skill, resume_text):

                matched.append(skill)

            else:

                missing.append(skill)

        score = percentage(
            len(matched),
            len(jd.skills),
        )

        return score, matched, missing

    # ----------------------------------------------------
    # Experience Matching
    # ----------------------------------------------------

    def _calculate_experience_score(
        self,
        resume: dict,
        jd: JDModel,
    ):

        resume_experience = len(
            resume.get("experience", [])
        )

        if jd.experience is None:
            return 100

        if resume_experience >= jd.experience:
            return 100

        return round(
            (resume_experience / jd.experience) * 100
        )

    # ----------------------------------------------------
    # Education Matching
    # ----------------------------------------------------

    def _calculate_education_score(
        self,
        resume: dict,
        jd: JDModel,
    ):

        education = resume.get(
            "education",
            "",
        ).lower()

        if not jd.education:
            return 100

        matched = 0

        for degree in jd.education:

            if degree.lower() in education:
                matched += 1

        return percentage(
            matched,
            len(jd.education),
        )
        # ----------------------------------------------------
    # Responsibility Matching
    # ----------------------------------------------------

    def _calculate_responsibility_score(
        self,
        resume_text: str,
        jd: JDModel,
    ):

        matched = []
        missing = []

        for responsibility in jd.responsibilities:

            if self.matcher.match(responsibility, resume_text):

                matched.append(responsibility)

            else:

                missing.append(responsibility)

        score = percentage(
            len(matched),
            len(jd.responsibilities),
        )

        return score, matched, missing

    # ----------------------------------------------------
    # Keyword Matching
    # ----------------------------------------------------

    def _calculate_keyword_score(
        self,
        resume_text: str,
        jd: JDModel,
    ):

        if not jd.keywords:
            return 100

        matched = 0

        for keyword in jd.keywords:

            if self.matcher.match(keyword, resume_text):
                matched += 1

        return percentage(
            matched,
            len(jd.keywords),
        )

    # ----------------------------------------------------
    # Strengths
    # ----------------------------------------------------

    def _generate_strengths(
        self,
        matched_skills: List[str],
    ) -> List[str]:

        return strengths(matched_skills)

    # ----------------------------------------------------
    # Weaknesses
    # ----------------------------------------------------

    def _generate_weaknesses(
        self,
        missing_skills: List[str],
    ) -> List[str]:

        return weaknesses(missing_skills)

    # ----------------------------------------------------
    # Recommendations
    # ----------------------------------------------------

    def _generate_recommendations(
        self,
        missing_skills: List[str],
        missing_responsibilities: List[str],
    ) -> List[Recommendation]:

        recommendations = []

        for skill in missing_skills:

            recommendations.append(
                Recommendation(
                    skill=skill,
                    priority="HIGH",
                    message=f"Consider adding experience with '{skill}' if applicable."
                )
            )

        for responsibility in missing_responsibilities:

            recommendations.append(
                Recommendation(
                    skill=responsibility,
                    priority="MEDIUM",
                    message=f"Highlight work related to '{responsibility}' if applicable."
                )
            )

        if not recommendations:

            recommendations.append(
                Recommendation(
                    skill="Profile",
                    priority="LOW",
                    message="Excellent alignment with the job description."
                )
            )

        return recommendations
        # ----------------------------------------------------
    # Main ATS Calculation
    # ----------------------------------------------------

    def calculate_match(
        self,
        resume: dict,
        jd: JDModel,
    ) -> ATSReport:

        resume_text = self._build_resume_text(resume)

        # Skill Score
        (
            skill_score,
            matched_skills,
            missing_skills,
        ) = self._calculate_skill_score(
            resume_text,
            jd,
        )

        # Experience Score
        experience_score = self._calculate_experience_score(
            resume,
            jd,
        )

        # Education Score
        education_score = self._calculate_education_score(
            resume,
            jd,
        )

        # Responsibility Score
        (
            responsibility_score,
            matched_responsibilities,
            missing_responsibilities,
        ) = self._calculate_responsibility_score(
            resume_text,
            jd,
        )

        # Keyword Score
        keyword_score = self._calculate_keyword_score(
            resume_text,
            jd,
        )

        # Overall Score
        final_score = overall_score(
            skill_score,
            experience_score,
            education_score,
            responsibility_score,
            keyword_score,
        )

        # Build ATS Report
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
                matched_skills
            ),
            weaknesses=self._generate_weaknesses(
                missing_skills
            ),
            recommendations=self._generate_recommendations(
                missing_skills,
                missing_responsibilities,
            ),
        )

        return report