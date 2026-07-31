import re

from app.data.synonyms import SYNONYMS
from app.utils.text_normalizer import TextNormalizer
from app.utils.phrase_matcher import PhraseMatcher


class SmartSkillMatcher:
    """
    Production Smart Skill Matcher

    Matching Order:
    1. Exact Match
    2. Synonym Match
    3. Semantic Phrase Match
    """

    def match(self, skill: str, resume_text: str) -> bool:

        skill = TextNormalizer.normalize(skill)
        resume_text = TextNormalizer.normalize(resume_text)

        # -----------------------------
        # Exact Match
        # -----------------------------

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, resume_text):
            return True

        # -----------------------------
        # Synonym Match
        # -----------------------------

        if skill in SYNONYMS:

            for synonym in SYNONYMS[skill]:

                synonym = TextNormalizer.normalize(synonym)

                pattern = r"\b" + re.escape(synonym) + r"\b"

                if re.search(pattern, resume_text):
                    return True

        # -----------------------------
        # Semantic Phrase Match
        # -----------------------------

        resume_sentences = re.split(
            r"[,\n.;]",
            resume_text,
        )

        for sentence in resume_sentences:

            if PhraseMatcher.is_match(
                skill,
                sentence,
                threshold=0.60,
            ):
                return True

        return False