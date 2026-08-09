from app.utils.text_normalizer import TextNormalizer


class PhraseMatcher:
    """
    Calculates similarity between two phrases
    using normalized word overlap.
    """

    @staticmethod
    def similarity(phrase1: str, phrase2: str) -> float:

        phrase1 = TextNormalizer.normalize(phrase1)
        phrase2 = TextNormalizer.normalize(phrase2)

        words1 = set(phrase1.split())
        words2 = set(phrase2.split())

        if not words1 or not words2:
            return 0.0

        common = words1.intersection(words2)

        return len(common) / max(len(words1), len(words2))

    @staticmethod
    def is_match(
        phrase1: str,
        phrase2: str,
        threshold: float = 0.60,
    ) -> bool:

        return (
            PhraseMatcher.similarity(
                phrase1,
                phrase2,
            ) >= threshold
        )