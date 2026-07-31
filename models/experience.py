from dataclasses import dataclass, field


@dataclass
class Experience:
    company: str = ""
    designation: str = ""
    duration: str = ""
    location: str = ""
    description: list[str] = field(default_factory=list)