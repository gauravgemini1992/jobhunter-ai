from __future__ import annotations

import re
from typing import List, Set

from app.engines.smart_skill_matcher import SmartSkillMatcher


class SkillExtractor:
    """
    Production Skill Extractor

    Features
    --------
    ✓ Longest skill first
    ✓ Duplicate removal
    ✓ Overlap removal
    ✓ Canonical skill extraction
    """

    def __init__(self, skills: List[str]):

        self.matcher = SmartSkillMatcher()

        # Longest skills first
        self.skills = sorted(
            set(skills),
            key=len,
            reverse=True,
        )

    def extract(
        self,
        search_text: str,
    ) -> List[str]:

        detected: List[str] = []

        occupied: List[range] = []

        normalized = search_text.lower()

        for skill in self.skills:

            if not self.matcher.match(
                skill,
                normalized,
            ):
                continue

            pattern = re.escape(skill.lower())

            match = re.search(pattern, normalized)

            if not match:
                continue

            span = range(
                match.start(),
                match.end(),
            )

            overlap = False

            for existing in occupied:

                if (
                    span.start < existing.stop
                    and span.stop > existing.start
                ):
                    overlap = True
                    break

            if overlap:
                continue

            occupied.append(span)

            detected.append(skill)

        return sorted(
            set(detected)
        )
