from dataclasses import dataclass, field
from typing import List


@dataclass
class CompanyProfile:
    """
    Company Information Model

    Used by:
    - Company Research
    - Interview Preparation
    - Job Insights
    """

    name: str = ""

    industry: str = ""

    headquarters: str = ""

    founded: str = ""

    employees: str = ""

    ceo: str = ""

    website: str = ""

    careers_url: str = ""

    linkedin_url: str = ""

    glassdoor_url: str = ""

    description: str = ""

    products: List[str] = field(default_factory=list)

    hiring_roles: List[str] = field(default_factory=list)

    technologies: List[str] = field(default_factory=list)

    interview_topics: List[str] = field(default_factory=list)

    latest_news: List[str] = field(default_factory=list)

    # --------------------------------------------------

    def display(self):

        print("=" * 70)
        print("COMPANY PROFILE")
        print("=" * 70)

        print(f"Company         : {self.name}")
        print(f"Industry        : {self.industry}")
        print(f"Headquarters    : {self.headquarters}")
        print(f"Founded         : {self.founded}")
        print(f"Employees       : {self.employees}")
        print(f"CEO             : {self.ceo}")

        print()

        print("Website")
        print(self.website)

        print()

        print("Careers")
        print(self.careers_url)

        print()

        print("LinkedIn")
        print(self.linkedin_url)

        print()

        print("Glassdoor")
        print(self.glassdoor_url)

        print()

        print("Description")

        if self.description:
            print(self.description)

        print()

        print("Products")

        if self.products:

            for product in self.products:

                print(f"• {product}")

        else:

            print("None")

        print()

        print("Hiring Roles")

        if self.hiring_roles:

            for role in self.hiring_roles:

                print(f"• {role}")

        else:

            print("None")

        print()

        print("Technologies")

        if self.technologies:

            for tech in self.technologies:

                print(f"• {tech}")

        else:

            print("None")

        print()

        print("Interview Topics")

        if self.interview_topics:

            for topic in self.interview_topics:

                print(f"• {topic}")

        else:

            print("None")

        print()

        print("Latest News")

        if self.latest_news:

            for news in self.latest_news:

                print(f"• {news}")

        else:

            print("None")

        print("=" * 70)