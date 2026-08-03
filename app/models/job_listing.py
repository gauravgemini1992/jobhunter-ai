from dataclasses import dataclass, field
from typing import List


@dataclass
class JobListing:
    """
    Represents a job returned by any provider.
    """

    title: str
    company: str
    location: str
    description: str

    skills: List[str] = field(default_factory=list)

    experience: str = ""
    employment_type: str = ""
    salary: str = ""

    apply_url: str = ""
    source: str = ""

    ats_match_score: int = 0

    def display(self):

        print("=" * 70)
        print(f"Job Title      : {self.title}")
        print(f"Company        : {self.company}")
        print(f"Location       : {self.location}")

        if self.experience:
            print(f"Experience     : {self.experience}")

        if self.employment_type:
            print(f"Employment     : {self.employment_type}")

        if self.salary:
            print(f"Salary         : {self.salary}")

        print(f"ATS Match      : {self.ats_match_score}%")

        if self.skills:

            print(
                "Skills         : "
                + ", ".join(self.skills)
            )

        if self.source:
            print(f"Source         : {self.source}")

        if self.apply_url:
            print(f"Apply          : {self.apply_url}")

        print("=" * 70)