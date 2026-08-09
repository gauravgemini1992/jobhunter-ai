"""
============================================================
JobHunter AI
Company Provider Interface
============================================================
"""

from abc import ABC, abstractmethod
from typing import Optional

from app.models.company_profile import CompanyProfile


class CompanyProvider(ABC):
    """
    Base interface for all company providers.
    """

    @abstractmethod
    def search(
        self,
        company_name: str,
    ) -> Optional[CompanyProfile]:
        """
        Search company information.

        Parameters
        ----------
        company_name : str

        Returns
        -------
        CompanyProfile | None
        """
        pass