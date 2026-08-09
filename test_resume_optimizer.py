from resume_parser import parse_resume

from app.optimizer.resume_optimizer import ResumeOptimizer

resume = parse_resume("resume.docx")

jd = """

Customer Success Manager

Responsibilities

Manage Enterprise Accounts

Drive Renewals

Conduct Quarterly Business Reviews

Work with Salesforce CRM

Lead Customer Onboarding

MBA

5+ years

"""

optimizer = ResumeOptimizer()

report = optimizer.optimize(resume, jd)

print("\n" + "=" * 60)
print("RESUME OPTIMIZER REPORT")
print("=" * 60)

print(f"\nATS Score: {report['ats_score']}%")

print("\nMatched Skills:")
for skill in report["matched_skills"]:
    print(f"✔ {skill}")

print("\nRecommendations:")
for item in report["recommendations"]:
    print(
        f"[{item['priority']}] {item['skill']}\n"
        f"  → {item['recommendation']}"
    )