from app.reporting.family_formatter import FamilyFormatter


skills = [
    "ai",
    "chatgpt",
    "openai",
    "generative ai",
    "prompt engineering",
    "power bi",
    "sql",
]

result = FamilyFormatter.group(skills)

print(result)