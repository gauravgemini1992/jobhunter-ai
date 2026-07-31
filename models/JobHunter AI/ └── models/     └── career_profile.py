from dataclasses import dataclass, field

from models.personal import Personal
from models.experience import Experience


@dataclass
class CareerProfile:
    """
    This class stores everything about a candidate.
    As we build JobHunter AI, more sections will be added here.
    """

    personal: Personal = field(default_factory=Personal)
    experiences: list[Experience] = field(default_factory=list)
    education: list = field(default_factory=list)
    skills: list = field(default_factory=list)
    projects: list = field(default_factory=list)
    certifications: list = field(default_factory=list)