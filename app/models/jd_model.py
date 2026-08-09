from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class JDModel:

    job_title: str = ""

    skills: List[str] = field(default_factory=list)

    experience: Optional[int] = None

    education: List[str] = field(default_factory=list)

    responsibilities: List[str] = field(default_factory=list)

    keywords: List[str] = field(default_factory=list)