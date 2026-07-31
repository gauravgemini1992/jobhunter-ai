from dataclasses import dataclass, field
from typing import List

from app.models.recommendation import Recommendation


@dataclass
class ATSReport:
    """
    Complete ATS analysis report.
    """

    overall_score: int = 0

    skill_score: int = 0
    experience_score: int = 0
    education_score: int = 0
    responsibility_score: int = 0
    keyword_score: int = 0

    matched_skills: List[str] = field(default_factory=list)
    missing_skills: List[str] = field(default_factory=list)

    matched_responsibilities: List[str] = field(default_factory=list)
    missing_responsibilities: List[str] = field(default_factory=list)

    strengths: List[str] = field(default_factory=list)
    weaknesses: List[str] = field(default_factory=list)

    recommendations: List[Recommendation] = field(default_factory=list)