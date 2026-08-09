from abc import ABC, abstractmethod
from typing import List

from app.models.job_listing import JobListing


class JobProvider(ABC):
    """
    Base class for all job providers.

    Every provider (RemoteOK, Adzuna, Arbeitnow, etc.)
    must implement the search() method.
    """

    @abstractmethod
    def search(
        self,
        keywords: List[str],
        location: str = "",
        experience: int = 0,
    ) -> List[JobListing]:
        """
        Search jobs.

        Parameters
        ----------
        keywords : List[str]
            Skills/keywords extracted from the resume.

        location : str
            Preferred job location.

        experience : int
            Candidate experience in years.

        Returns
        -------
        List[JobListing]
        """
        pass