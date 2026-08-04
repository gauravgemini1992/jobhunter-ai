from app.models.company_profile import CompanyProfile


class MockCompanyProvider:
    """
    Mock Company Provider

    Returns demo company information.

    This provider will later be replaced
    by real APIs/web search without changing
    the CompanyResearchService.
    """

    def __init__(self):

        self.database = {

            "microsoft": self.microsoft(),

            "google": self.google(),

            "openai": self.openai(),

            "salesforce": self.salesforce(),

            "freshworks": self.freshworks(),

        }

    # --------------------------------------------------

    def search(self, company_name: str):

        return self.database.get(
            company_name.lower().strip()
        )

    # --------------------------------------------------

    def microsoft(self):

        return CompanyProfile(

            name="Microsoft",

            industry="Cloud Computing & Software",

            headquarters="Redmond, Washington, USA",

            founded="1975",

            employees="220,000+",

            ceo="Satya Nadella",

            website="https://www.microsoft.com",

            careers_url="https://careers.microsoft.com",

            linkedin_url="https://www.linkedin.com/company/microsoft",

            glassdoor_url="https://www.glassdoor.com/Overview/Working-at-Microsoft",

            description=(
                "Microsoft develops enterprise software, cloud services, "
                "AI products and productivity platforms."
            ),

            products=[
                "Azure",
                "Microsoft 365",
                "GitHub",
                "Copilot",
                "Windows",
            ],

            hiring_roles=[
                "Software Engineer",
                "Customer Success Manager",
                "Cloud Solution Architect",
                "Product Manager",
                "Account Executive",
            ],

            technologies=[
                "Azure",
                ".NET",
                "C#",
                "Python",
                "AI",
                "Power BI",
            ],

            interview_topics=[
                "Coding",
                "System Design",
                "Behavioral",
                "Leadership",
            ],

            latest_news=[
                "Expansion of Microsoft Copilot",
                "AI investments across Azure",
            ],
        )

    # --------------------------------------------------

    def google(self):

        return CompanyProfile(

            name="Google",

            industry="Internet & Cloud",

            headquarters="Mountain View, California, USA",

            founded="1998",

            employees="180,000+",

            ceo="Sundar Pichai",

            website="https://www.google.com",

            careers_url="https://careers.google.com",

            linkedin_url="https://www.linkedin.com/company/google",

            glassdoor_url="https://www.glassdoor.com/Overview/Working-at-Google",

            description=(
                "Google builds products across search, cloud, AI, Android "
                "and digital advertising."
            ),

            products=[
                "Google Cloud",
                "Gemini",
                "Android",
                "YouTube",
                "Workspace",
            ],

            hiring_roles=[
                "Software Engineer",
                "AI Engineer",
                "Cloud Consultant",
                "Customer Engineer",
            ],

            technologies=[
                "GCP",
                "Go",
                "Python",
                "Kubernetes",
                "Gemini",
            ],

            interview_topics=[
                "Coding",
                "Algorithms",
                "System Design",
                "Leadership",
            ],

            latest_news=[
                "Expansion of Gemini AI",
            ],
        )

    # --------------------------------------------------

    def openai(self):

        return CompanyProfile(

            name="OpenAI",

            industry="Artificial Intelligence",

            headquarters="San Francisco, California, USA",

            founded="2015",

            employees="1000+",

            ceo="Sam Altman",

            website="https://openai.com",

            careers_url="https://openai.com/careers",

            linkedin_url="https://www.linkedin.com/company/openai",

            glassdoor_url="",

            description=(
                "OpenAI develops frontier AI models including ChatGPT "
                "and APIs for developers."
            ),

            products=[
                "ChatGPT",
                "OpenAI API",
                "GPT Models",
            ],

            hiring_roles=[
                "Research Engineer",
                "Software Engineer",
                "Customer Success",
                "Solutions Engineer",
            ],

            technologies=[
                "Python",
                "LLMs",
                "PyTorch",
                "OpenAI API",
            ],

            interview_topics=[
                "AI",
                "Machine Learning",
                "Coding",
                "Behavioral",
            ],

            latest_news=[
                "Continuous improvements to ChatGPT and API platform",
            ],
        )

    # --------------------------------------------------

    def salesforce(self):

        return CompanyProfile(

            name="Salesforce",

            industry="CRM & SaaS",

            headquarters="San Francisco, California, USA",

            founded="1999",

            employees="70,000+",

            ceo="Marc Benioff",

            website="https://www.salesforce.com",

            careers_url="https://careers.salesforce.com",

            linkedin_url="https://www.linkedin.com/company/salesforce",

            glassdoor_url="https://www.glassdoor.com/Overview/Working-at-Salesforce",

            description="Global CRM and enterprise SaaS leader.",

            products=[
                "Sales Cloud",
                "Service Cloud",
                "Einstein AI",
                "Slack",
            ],

            hiring_roles=[
                "Customer Success Manager",
                "Account Executive",
                "Technical Architect",
            ],

            technologies=[
                "Salesforce",
                "CRM",
                "AI",
                "Slack",
            ],

            interview_topics=[
                "Behavioral",
                "Sales",
                "Customer Success",
            ],

            latest_news=[
                "Expansion of Einstein AI capabilities",
            ],
        )

    # --------------------------------------------------

    def freshworks(self):

        return CompanyProfile(

            name="Freshworks",

            industry="Customer Experience Software",

            headquarters="Chennai, India",

            founded="2010",

            employees="6000+",

            ceo="Dennis Woodside",

            website="https://www.freshworks.com",

            careers_url="https://www.freshworks.com/company/careers",

            linkedin_url="https://www.linkedin.com/company/freshworks-inc",

            glassdoor_url="https://www.glassdoor.com/Overview/Working-at-Freshworks",

            description="Freshworks develops customer engagement and support software.",

            products=[
                "Freshdesk",
                "Freshsales",
                "Freshservice",
            ],

            hiring_roles=[
                "Customer Success",
                "Sales",
                "Support Engineer",
            ],

            technologies=[
                "CRM",
                "Cloud",
                "SaaS",
            ],

            interview_topics=[
                "Customer Success",
                "Behavioral",
            ],

            latest_news=[
                "Continued AI features across Freshworks platform",
            ],
        )