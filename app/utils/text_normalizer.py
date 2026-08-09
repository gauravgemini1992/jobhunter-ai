import re

from nltk.stem import PorterStemmer


stemmer = PorterStemmer()


class TextNormalizer:
    """
    Text normalizer using Porter Stemmer.
    """

    @staticmethod
    def normalize(text: str) -> str:

        text = text.lower()

        text = re.sub(
            r"[^a-z0-9 ]",
            " ",
            text,
        )

        words = []

        for word in text.split():

            words.append(
                stemmer.stem(word)
            )

        return " ".join(words)