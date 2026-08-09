import re


ROLE_ALIASES = {

    "customer success manager": [
        "customer success manager",
        "sr customer success manager",
        "senior customer success manager",
        "client success manager",
        "customer success lead"
    ],

    "account manager": [
        "account manager",
        "key account manager",
        "senior key account manager",
        "strategic account manager"
    ],

    "business development manager": [
        "business development manager",
        "bdm",
        "business development executive"
    ]
}


def normalize_role(role):

    if not role:
        return ""

    role = role.lower().strip()

    role = re.sub(r"\s+", " ", role)

    for standard_role, aliases in ROLE_ALIASES.items():

        if role in aliases:
            return standard_role.title()

    return role.title()