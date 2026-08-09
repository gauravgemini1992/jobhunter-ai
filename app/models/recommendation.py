from dataclasses import dataclass


@dataclass
class Recommendation:
    skill: str
    priority: str
    message: str