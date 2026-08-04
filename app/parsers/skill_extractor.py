from __future__ import annotations

import re
from typing import Dict, List, Set

from app.engines.smart_skill_matcher import SmartSkillMatcher


class SkillExtractor:
    """
    JobHunter AI
    Production Skill Extractor v2.1

    Features
    --------
    ✓ Longest skill first
    ✓ Whole-word matching
    ✓ Overlap detection
    ✓ Duplicate removal
    ✓ Canonical normalization
    ✓ Synonym support
    ✓ Ignore invalid one-letter skills
    ✓ Compiled regex cache
    """

    # --------------------------------------------------
    # Ignore one-letter skills except known abbreviations
    # --------------------------------------------------

    MIN_SKILL_LENGTH = 2

    ALLOWED_SHORT_SKILLS = {

        "ai",
        "ml",
        "bi",
        "qa",
        "hr",
        "ui",
        "ux",
        "ci",
        "cd",

    }

    # --------------------------------------------------

    SYNONYMS: Dict[str, str] = {

        # AI

        "gen ai": "generative ai",
        "genai": "generative ai",
        "llms": "llm",

        # Customer Success

        "g2m": "go to market",
        "gtm": "go to market",
        "go-to-market": "go to market",

        "ebr": "executive business review",
        "qbr": "quarterly business review",

        "voc": "voice of customer",

        "nrr": "net revenue retention",
        "grr": "gross revenue retention",

        "upselling": "upsell",
        "cross selling": "cross sell",

        # CRM

        "sales cloud": "salesforce",
        "service cloud": "salesforce",

    }

    # --------------------------------------------------

    def __init__(
        self,
        skills: List[str],
    ):

        self.matcher = SmartSkillMatcher()

        self.skills = sorted(

            set(skills),

            key=len,

            reverse=True,

        )

        # Compile regex once

        self.patterns = {

            skill: re.compile(

                rf"\b{re.escape(self._normalize(skill))}\b"

            )

            for skill in self.skills

        }

    # --------------------------------------------------

    def _normalize(
        self,
        text: str,
    ) -> str:

        text = text.lower()

        text = text.replace("-", " ")

        text = re.sub(

            r"\s+",

            " ",

            text,

        )

        return text.strip()

    # --------------------------------------------------

    def _canonical(
        self,
        skill: str,
    ) -> str:

        skill = self._normalize(skill)

        return self.SYNONYMS.get(
            skill,
            skill,
        )

    # --------------------------------------------------

    def _find_matches(
        self,
        skill: str,
        text: str,
    ) -> List[range]:

        spans: List[range] = []

        pattern = self.patterns[skill]

        for match in pattern.finditer(text):

            spans.append(

                range(

                    match.start(),

                    match.end(),

                )

            )

        return spans

    # --------------------------------------------------

    def _overlaps(
        self,
        span: range,
        occupied: List[range],
    ) -> bool:

        for existing in occupied:

            if (

                span.start < existing.stop

                and

                span.stop > existing.start

            ):

                return True

        return False

    # --------------------------------------------------

    def extract(
        self,
        search_text: str,
    ) -> List[str]:

        if not search_text:
            return []

        normalized_text = self._normalize(
            search_text
        )

        detected: Set[str] = set()

        occupied: List[range] = []

        for skill in self.skills:

            searchable_skill = self._normalize(skill)

            # ------------------------------------------
            # Ignore invalid short skills
            # ------------------------------------------

            if (

                len(searchable_skill) < self.MIN_SKILL_LENGTH

                and

                searchable_skill
                not in self.ALLOWED_SHORT_SKILLS

            ):

                continue

            if not self.matcher.match(

                searchable_skill,

                normalized_text,

            ):

                continue

            spans = self._find_matches(

                skill,

                normalized_text,

            )

            if not spans:

                continue

            accepted = False

            for span in spans:

                if self._overlaps(

                    span,

                    occupied,

                ):

                    continue

                occupied.append(span)

                accepted = True

            if accepted:

                detected.add(

                    self._canonical(skill)

                )

        return sorted(

            detected,

            key=str.lower,

        )