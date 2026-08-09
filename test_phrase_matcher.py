from app.utils.phrase_matcher import PhraseMatcher

tests = [

    (
        "manage enterprise accounts",
        "managed enterprise accounts",
    ),

    (
        "drive renewals",
        "renewals",
    ),

    (
        "customer onboarding",
        "lead customer onboarding",
    ),

    (
        "crm",
        "crm",
    ),

    (
        "salesforce",
        "hubspot",
    )

]

for a, b in tests:

    similarity = PhraseMatcher.similarity(a, b)

    print("-" * 60)

    print(a)

    print(b)

    print(f"Similarity : {similarity:.2f}")

    print("Match :", PhraseMatcher.is_match(a, b))