from resume_parser import parse_resume

from app.engines.ats_engine import ATSEngine

resume = parse_resume("resume.docx")

jd = """

Customer Success Manager

Responsibilities

Manage Enterprise Accounts

Drive Renewals

Conduct Quarterly Business Reviews

Work with Salesforce CRM

Lead Customer Onboarding

Qualifications

MBA

5+ years experience

"""

engine = ATSEngine()

report = engine.calculate_match(resume, jd)

print()

print("=" * 60)

print("ATS REPORT")

print("=" * 60)

print(f"Overall Match      : {report['overall_score']}%")
print(f"Skill Match        : {report['skill_score']}%")
print(f"Experience Match   : {report['experience_score']}%")
print(f"Education Match    : {report['education_score']}%")

print()

print("Matched Skills")

for skill in report["matched_skills"]:
    print("✔", skill)

print()

print("Missing Skills")

for skill in report["missing_skills"]:
    print("✘", skill)