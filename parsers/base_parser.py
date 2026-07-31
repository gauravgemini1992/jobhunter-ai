from abc import ABC, abstractmethod


class BaseParser(ABC):
    """
    Base class for all parsers.
    Every parser in the system must implement parse().
    """

    @abstractmethod
    def parse(self, text: str):
        """
        Parse the given text and return structured data.
        """
        pass