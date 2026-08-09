from app.engines.smart_skill_matcher import SmartSkillMatcher

matcher = SmartSkillMatcher()

resume = """
Managed enterprise accounts,
customer onboarding,
renewals,
QBR,
CRM,
Customer Success,
Stakeholder Management
"""

tests = [

    "manage enterprise accounts",

    "enterprise accounts",

    "drive renewals",

    "renewals",

    "customer success",

    "crm",

    "stakeholder management"

]

for item in tests:

    print(f"{item:35} -> {matcher.match(item, resume)}")