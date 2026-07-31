from app.parsers.jd_parser import JDParser

jd = """

Customer Success Manager

Responsibilities

Manage enterprise accounts

Drive renewals

Conduct Quarterly Business Reviews

Work with Salesforce CRM

Lead customer onboarding

Experience

5+ years

MBA Preferred

"""

parser = JDParser()

result = parser.parse(jd)

print(result)