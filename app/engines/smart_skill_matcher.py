import re
from typing import List

from app.data.synonyms import SYNONYMS
from app.utils.phrase_matcher import PhraseMatcher
from app.utils.text_normalizer import TextNormalizer


class SmartSkillMatcher:
    """
    Production Smart Skill Matcher

    Matching Order
    --------------
    1. Exact Match
    2. Alias / Synonym Match
    3. Phrase Match
    """

    def __init__(self):

        self._cache = {}

    # ---------------------------------------------------------
    # Regex
    # ---------------------------------------------------------

    def _regex(self, text: str):

        if text not in self._cache:

            self._cache[text] = re.compile(
                r"\b" + re.escape(text) + r"\b",
                re.IGNORECASE,
            )

        return self._cache[text]

    # ---------------------------------------------------------
    # Variations
    # ---------------------------------------------------------

    def _variants(self, skill: str) -> List[str]:

        variants = {skill}

        if skill in SYNONYMS:
            variants.update(
                TextNormalizer.normalize(s)
                for s in SYNONYMS[skill]
            )

        # Singular / plural
        if skill.endswith("s"):
            variants.add(skill[:-1])
        else:
            variants.add(skill + "s")

        # Remove duplicates / blanks
        return sorted(
            {
                v.strip()
                for v in variants
                if v.strip()
            }
        )

    # ---------------------------------------------------------
    # Match
    # ---------------------------------------------------------

    def match(
        self,
        skill: str,
        resume_text: str,
    ) -> bool:

        if not skill or not resume_text:
            return False

        skill = TextNormalizer.normalize(skill)
        resume_text = TextNormalizer.normalize(resume_text)

        # -----------------------------------------------------
        # Exact / Synonym Match
        # -----------------------------------------------------

        for variant in self._variants(skill):

            if self._regex(variant).search(resume_text):
                return True

        # -----------------------------------------------------
        # Phrase Match
        # -----------------------------------------------------

        sentences = re.split(
            r"[,\n.;]",
            resume_text,
        )

        for sentence in sentences:

            sentence = sentence.strip()

            if not sentence:
                continue

            for variant in self._variants(skill):

                if PhraseMatcher.is_match(
                    variant,
                    sentence,
                    threshold=0.72,
                ):
                    return True

        return False