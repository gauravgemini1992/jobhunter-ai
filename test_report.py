from app.models.ats_report import ATSReport
from app.models.recommendation import Recommendation
from app.optimizer.resume_optimizer import ResumeOptimizer
from app.reports.ats_report_generator import ATSReportGenerator


ats_report = ATSReport(
    overall_score=72,
    skill_score=80,
    experience_score=100,
    education_score=100,
    responsibility_score=60,
    keyword_score=100,
    matched_skills=[
        "CRM",
        "Customer Success",
        "Enterprise Accounts",
        "Renewals",
    ],
    missing_skills=[
        "Salesforce",
        "Customer Onboarding",
    ],
    matched_responsibilities=[
        "Managed Enterprise Accounts",
    ],
    missing_responsibilities=[
        "Drive Renewals",
    ],
    strengths=[
        "CRM",
        "Customer Success",
        "Enterprise Accounts",
        "Renewals",
    ],
    weaknesses=[
        "Salesforce",
        "Customer Onboarding",
    ],
    recommendations=[
        Recommendation(
            skill="Salesforce",
            priority="HIGH",
            message="Add Salesforce experience if applicable."
        ),
        Recommendation(
            skill="Customer Onboarding",
            priority="MEDIUM",
            message="Highlight Customer Onboarding ownership."
        ),
    ],
)

optimizer = ResumeOptimizer()

optimization = optimizer.optimize(ats_report)

ATSReportGenerator().print_report(
    ats_report,
    optimization,
)