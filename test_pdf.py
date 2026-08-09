from app.reports.pdf_report_generator import PDFReportGenerator
from app.models.ats_report import ATSReport
from app.models.recommendation import Recommendation

report = ATSReport(
    overall_score=82,
    skill_score=80,
    experience_score=100,
    education_score=100,
    responsibility_score=50,
    keyword_score=100,
    strengths=[
        "crm",
        "customer success",
        "enterprise accounts",
    ],
    weaknesses=[
        "salesforce",
    ],
    recommendations=[
        Recommendation(
            skill="salesforce",
            priority="HIGH",
            message="Add Salesforce experience if applicable.",
        )
    ],
)

pdf = PDFReportGenerator()

file = pdf.generate(
    report,
    candidate_name="Gaurav Hegde",
)

print(file)