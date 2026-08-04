from typing import List

from app.models.job_listing import JobListing
from app.providers.job_provider import JobProvider


class MockProvider(JobProvider):
    """
    Temporary provider used until real APIs
    (Adzuna / RemoteOK / Arbeitnow) are integrated.
    """

    def search(
        self,
        keywords: List[str],
        location: str = "",
        experience: int = 0,
    ) -> List[JobListing]:

        jobs = [

            JobListing(
                title="AI Customer Success Manager",
                company="Microsoft",
                location="Bengaluru, India",
                experience="5+ Years",
                employment_type="Full Time",
                salary="₹28 LPA",
                description="Drive AI adoption for enterprise customers.",
                skills=[
                    "Customer Success",
                    "AI",
                    "CRM",
                    "ChatGPT",
                    "SQL",
                ],
                apply_url="https://careers.microsoft.com",
                source="Mock Provider",
                ats_match_score=96,
            ),

            JobListing(
                title="Senior Customer Success Manager",
                company="Salesforce",
                location="Hyderabad, India",
                experience="6+ Years",
                employment_type="Full Time",
                salary="₹32 LPA",
                description="Manage strategic enterprise customers.",
                skills=[
                    "Customer Success",
                    "Salesforce",
                    "CRM",
                    "Stakeholder Management",
                ],
                apply_url="https://careers.salesforce.com",
                source="Mock Provider",
                ats_match_score=93,
            ),

            JobListing(
                title="Technical Account Manager",
                company="Oracle",
                location="Remote",
                experience="5+ Years",
                employment_type="Full Time",
                salary="₹30 LPA",
                description="Support enterprise SaaS customers.",
                skills=[
                    "SQL",
                    "Customer Success",
                    "Oracle Cloud",
                ],
                apply_url="https://careers.oracle.com",
                source="Mock Provider",
                ats_match_score=91,
            ),

            JobListing(
                title="Enterprise Account Manager",
                company="HubSpot",
                location="Remote",
                experience="4+ Years",
                employment_type="Full Time",
                salary="₹27 LPA",
                description="Grow strategic enterprise accounts.",
                skills=[
                    "CRM",
                    "HubSpot",
                    "Account Management",
                ],
                apply_url="https://www.hubspot.com/careers",
                source="Mock Provider",
                ats_match_score=89,
            ),

            JobListing(
                title="Customer Success Manager",
                company="Freshworks",
                location="Chennai, India",
                experience="5+ Years",
                employment_type="Full Time",
                salary="₹24 LPA",
                description="Drive customer adoption and retention.",
                skills=[
                    "Customer Success",
                    "CRM",
                    "SaaS",
                ],
                apply_url="https://www.freshworks.com/company/careers",
                source="Mock Provider",
                ats_match_score=88,
            ),
        ]

        return jobs