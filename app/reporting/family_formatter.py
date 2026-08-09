"""
Family Formatter

Groups related skills into a single capability.
"""

from typing import Dict, List

from app.data.skill_families import SKILL_FAMILIES


class FamilyFormatter:

    @staticmethod
    def group(skills: List[str]) -> Dict[str, List[str]]:
        """
        Returns:

        {
            "Artificial Intelligence": [
                "chatgpt",
                "openai"
            ],
            "Analytics": [
                "power bi"
            ],
            "SQL": [
                "sql"
            ]
        }
        """

        grouped: Dict[str, List[str]] = {}

        for skill in skills:

            skill_lower = skill.lower()

            family_found = False

            for family, members in SKILL_FAMILIES.items():

                if skill_lower in members:

                    grouped.setdefault(
                        family,
                        []
                    ).append(skill)

                    family_found = True
                    break

            if not family_found:

                grouped.setdefault(
                    skill.title(),
                    []
                ).append(skill)

        return grouped