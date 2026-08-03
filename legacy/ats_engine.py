from app.engines.ats_engine import ATSEngine
from app.models.jd_model import JDModel

resume = {
    "summary": "Customer Success Manager with experience in CRM, renewals and enterprise accounts.",
    "skills": "CRM, Customer Success, Enterprise Accounts, QBR",
    "education": "MBA",
    "experience": [
        {
            "title": "Customer Success Manager",
            "description": "Managed enterprise accounts, renewals, customer onboarding and QBRs."
        }
    ]
}

jd = JDModel(
    job_title="Customer Success Manager",
    skills=[
        "crm",
        "customer success",
        "enterprise accounts",
        "renewals",
        "salesforce",
    ],
    experience=1,
    education=["mba"],
    responsibilities=[
        "manage enterprise accounts",
        "drive renewals",
    ],
    keywords=[
        "crm",
        "renewals",
        "qbr",
    ],
)

engine = ATSEngine()
report = engine.calculate_match(resume, jd)

print(report)