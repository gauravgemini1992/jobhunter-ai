from app.optimizer.resume_optimizer import ResumeOptimizer
from app.models.ats_report import ATSReport
from app.models.recommendation import Recommendation

report = ATSReport(
    overall_score=72,
    skill_score=80,
    experience_score=100,
    education_score=100,
    responsibility_score=60,
    keyword_score=90,
    matched_skills=["crm", "customer success"],
    missing_skills=["salesforce", "gainsight"],
    matched_responsibilities=[],
    missing_responsibilities=["customer onboarding"],
    strengths=["crm", "customer success"],
    weaknesses=["salesforce"],
    recommendations=[
        Recommendation(
            skill="salesforce",
            priority="HIGH",
            message="Add Salesforce experience if applicable."
        ),
        Recommendation(
            skill="customer onboarding",
            priority="MEDIUM",
            message="Highlight Customer Onboarding ownership."
        )
    ]
)

optimizer = ResumeOptimizer()

result = optimizer.optimize(report)

for key, value in result.items():
    print(f"\n{key.upper()}")
    print(value)