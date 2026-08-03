from __future__ import annotations

import logging
import re
from collections import OrderedDict
from typing import Dict, List, Optional, Set

from app.data.skills import SKILLS
from app.engines.smart_skill_matcher import SmartSkillMatcher
from app.models.jd_model import JDModel
from app.parsers.section_parser import SectionParser
from app.parsers.skill_extractor import SkillExtractor

logger = logging.getLogger(__name__)


class JDParser:
    """
    Production Job Description Parser.

    Responsibilities
    ----------------
    - Extract Job Title
    - Extract Skills
    - Extract Experience
    - Extract Education
    - Extract Responsibilities
    - Extract Keywords

    Returns
    -------
    JDModel
    """

    SECTION_HEADERS = {
        "requirements": [
            "requirements",
            "required skills",
            "must have",
            "mandatory skills",
            "technical skills",
            "core skills",
            "skills",
            "qualification",
            "qualifications",
        ],
        "responsibilities": [
            "responsibilities",
            "responsibility",
            "what you'll do",
            "what you will do",
            "key responsibilities",
            "duties",
            "role",
            "job responsibilities",
        ],
        "education": [
            "education",
            "educational qualification",
            "academic qualification",
            "academic qualifications",
        ],
        "experience": [
            "experience",
            "required experience",
            "work experience",
        ],
    }

    EDUCATION_PATTERNS = [
        r"\bbachelor'?s degree\b",
        r"\bmaster'?s degree\b",
        r"\bb\.?tech\b",
        r"\bm\.?tech\b",
        r"\bb\.?e\b",
        r"\bm\.?e\b",
        r"\bbca\b",
        r"\bmca\b",
        r"\bmba\b",
        r"\bcomputer science\b",
        r"\binformation technology\b",
        r"\bengineering\b",
        r"\bbusiness administration\b",
    ]

    RESPONSIBILITY_VERBS = {
        "develop",
        "design",
        "build",
        "manage",
        "lead",
        "support",
        "maintain",
        "deliver",
        "create",
        "implement",
        "identify",
        "track",
        "resolve",
        "provide",
        "collaborate",
        "analyze",
        "drive",
        "own",
        "optimize",
        "monitor",
        "coordinate",
        "execute",
        "improve",
        "test",
        "deploy",
        "document",
        "review",
    }

    TITLE_BLACKLIST = {
        "about us",
        "company overview",
        "who we are",
        "job description",
        "overview",
        "introduction",
    }

    def __init__(self) -> None:
        self.matcher = SmartSkillMatcher()

        self.all_skills: List[str] = []

        for _, skills in SKILLS.items():
            self.all_skills.extend(skills)

        self.all_skills = sorted(
            set(self.all_skills),
            key=len,
            reverse=True,
        )

        self.skill_extractor = SkillExtractor(
            self.all_skills
        )        
        

    # ----------------------------------------------------
    # Utilities
    # ----------------------------------------------------

    @staticmethod
    def _normalize(text: str) -> str:
        text = text.replace("\r", "")
        text = re.sub(r"[ \t]+", " ", text)
        return text.strip()

    @staticmethod
    def _deduplicate(items: List[str]) -> List[str]:
        return list(OrderedDict.fromkeys(items))

    @staticmethod
    def _clean_line(line: str) -> str:
        return (
            line.strip()
            .lstrip("-•*0123456789.")
            .strip()
        )

    @staticmethod
    def _is_heading(line: str) -> bool:
        value = line.strip().lower()

        for headers in JDParser.SECTION_HEADERS.values():
            if value in headers:
                return True

        return False

    def _extract_title(
        self,
        lines: List[str],
    ) -> str:

        for line in lines[:10]:

            cleaned = self._clean_line(line)

            if not cleaned:
                continue

            lower = cleaned.lower()

            if lower in self.TITLE_BLACKLIST:
                continue

            if len(cleaned.split()) > 10:
                continue

            if self._is_heading(cleaned):
                continue

            return cleaned

        return ""
        # ----------------------------------------------------
    # Section Extraction
    # ----------------------------------------------------
    def _split_sections(
        self,
        lines: List[str],
    ) -> Dict[str, List[str]]:

        return SectionParser.split_sections(
            lines=lines,
            section_headers=self.SECTION_HEADERS,
            clean_line=self._clean_line,
        )
        return sections

    # ----------------------------------------------------
    # Skill Extraction
    # ----------------------------------------------------

    def _extract_skills(
        self,
        sections: Dict[str, List[str]],
        normalized_text: str,
    ) -> List[str]:

        search_area = "\n".join(
            sections["requirements"]
        )

        if not search_area.strip():
            search_area = normalized_text

        return self.skill_extractor.extract(
            search_area
        )
    # ----------------------------------------------------
    # Experience Extraction
    # ----------------------------------------------------

    def _extract_experience(
        self,
        normalized_text: str,
    ) -> Optional[int]:

        patterns = [

            r"(\d+)\s*\+\s*(?:years?|yrs?)",

            r"(\d+)\s*-\s*(\d+)\s*(?:years?|yrs?)",

            r"(\d+)\s*to\s*(\d+)\s*(?:years?|yrs?)",

            r"minimum\s+(\d+)\s*(?:years?|yrs?)",

            r"at\s+least\s+(\d+)\s*(?:years?|yrs?)",

            r"(\d+)\s*(?:years?|yrs?)",

        ]

        values: List[int] = []

        for pattern in patterns:

            for match in re.finditer(
                pattern,
                normalized_text,
                flags=re.IGNORECASE,
            ):

                groups = [
                    g
                    for g in match.groups()
                    if g
                ]

                if not groups:
                    continue

                values.append(
                    max(
                        int(x)
                        for x in groups
                    )
                )

        if values:
            return max(values)

        return None
        # ----------------------------------------------------
    # Education Extraction
    # ----------------------------------------------------

    def _extract_education(
        self,
        normalized_text: str,
        sections: Dict[str, List[str]],
    ) -> List[str]:

        detected: List[str] = []

        search_text = "\n".join(
            sections["education"]
        )

        if not search_text.strip():
            return []
        for pattern in self.EDUCATION_PATTERNS:

            match = re.search(
                pattern,
                search_text,
                flags=re.IGNORECASE,
            )

            if match:

                detected.append(
                    match.group(0)
                )

        return self._deduplicate(detected)

    # ----------------------------------------------------
    # Responsibility Extraction
    # ----------------------------------------------------

    def _extract_responsibilities(
        self,
        sections: Dict[str, List[str]],
        lines: List[str],
    ) -> List[str]:

        candidates = (
            sections["responsibilities"]
            if sections["responsibilities"]
            else lines
        )

        responsibilities: List[str] = []

        for raw in candidates:

            line = self._clean_line(raw)

            if len(line) < 8:
                continue

            lower = line.lower()

            if any(
                lower.startswith(
                    (
                        verb,
                        f"{verb}ing",
                        f"{verb}ed",
                    )
                )
                for verb in self.RESPONSIBILITY_VERBS
            ):
                responsibilities.append(line)
                continue

            if any(
                f" {verb} "
                in f" {lower} "
                for verb in self.RESPONSIBILITY_VERBS
            ):
                responsibilities.append(line)
                continue

            if lower.startswith(
                (
                    "responsible for",
                    "you will",
                    "candidate will",
                    "should",
                    "must",
                )
            ):
                responsibilities.append(line)

        return self._deduplicate(
            responsibilities
        )

    # ----------------------------------------------------
    # Keyword Extraction
    # ----------------------------------------------------

    def _extract_keywords(
        self,
        skills: List[str],
        responsibilities: List[str],
    ) -> List[str]:

        keywords: List[str] = []

        keywords.extend(skills)

        for responsibility in responsibilities:

            words = re.findall(
                r"[A-Za-z][A-Za-z0-9\-/+#.]{2,}",
                responsibility,
            )

            keywords.extend(
                word.lower()
                for word in words
            )

        return sorted(
            set(keywords)
        )
        # ----------------------------------------------------
    # Parse
    # ----------------------------------------------------

    def parse(
        self,
        jd_text: str,
    ) -> JDModel:

        logger.info(
            "Starting JD parsing..."
        )

        jd_text = self._normalize(jd_text)

        normalized_text = jd_text.lower()

        lines = [
            self._clean_line(line)
            for line in jd_text.split("\n")
            if self._clean_line(line)
        ]

        jd = JDModel()

        # ----------------------------------------------------
        # Job Title
        # ----------------------------------------------------

        jd.job_title = self._extract_title(
            lines
        )

        # ----------------------------------------------------
        # Sections
        # ----------------------------------------------------

        sections = self._split_sections(
            lines
        )

        # ----------------------------------------------------
        # Skills
        # ----------------------------------------------------

        jd.skills = self._extract_skills(
            sections,
            normalized_text,
        )

        # ----------------------------------------------------
        # Experience
        # ----------------------------------------------------

        jd.experience = (
            self._extract_experience(
                normalized_text
            )
        )

        # ----------------------------------------------------
        # Education
        # ----------------------------------------------------

        jd.education = (
            self._extract_education(
                normalized_text,
                sections,
            )
        )

        # ----------------------------------------------------
        # Responsibilities
        # ----------------------------------------------------

        jd.responsibilities = (
            self._extract_responsibilities(
                sections,
                lines,
            )
        )

        # ----------------------------------------------------
        # Keywords
        # ----------------------------------------------------

        jd.keywords = (
            self._extract_keywords(
                jd.skills,
                jd.responsibilities,
            )
        )
        logger.info(
            "JD parsed successfully."
        )

        logger.debug(
            "Job Title: %s",
            jd.job_title,
        )

        logger.debug(
            "Skills: %s",
            jd.skills,
        )

        logger.debug(
            "Responsibilities: %s",
            jd.responsibilities,
        )

        logger.debug(
            "Education: %s",
            jd.education,
        )

        logger.debug(
            "Experience: %s",
            jd.experience,
        )

        logger.debug(
            "Keywords: %s",
            jd.keywords,
        )

        return jd
