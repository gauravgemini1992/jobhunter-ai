from typing import List


class RoleInference:
    """
    Infers suitable job roles from resume skills.

    This helps search multiple relevant roles
    instead of relying only on extracted keywords.
    """

    ROLE_MAP = {

        "customer success": [
            "Customer Success Manager",
            "Senior Customer Success Manager",
            "Enterprise Customer Success Manager",
            "Customer Success Lead",
            "AI Customer Success Manager",
        ],

        "account management": [
            "Key Account Manager",
            "Enterprise Account Manager",
            "Strategic Account Manager",
            "Technical Account Manager",
            "Client Partner",
        ],

        "crm": [
            "CRM Manager",
            "Customer Success Manager",
            "Account Manager",
        ],

        "saas": [
            "Customer Success Manager",
            "Account Executive",
            "Technical Account Manager",
        ],

        "sales": [
            "Enterprise Sales Manager",
            "Business Development Manager",
            "Sales Manager",
        ],

        "renewals": [
            "Customer Success Manager",
            "Renewal Manager",
        ],

        "qbr": [
            "Customer Success Manager",
            "Strategic Account Manager",
        ],

        "sql": [
            "Technical Account Manager",
            "Solutions Consultant",
        ],

        "ai": [
            "AI Customer Success Manager",
            "AI Solutions Consultant",
        ],
    }

    @classmethod
    def infer_roles(
        cls,
        skills: List[str],
    ) -> List[str]:

        roles = []

        for skill in skills:

            key = skill.lower().strip()

            if key in cls.ROLE_MAP:

                roles.extend(
                    cls.ROLE_MAP[key]
                )

        # Remove duplicates while preserving order
        seen = set()
        unique_roles = []

        for role in roles:

            if role not in seen:

                seen.add(role)
                unique_roles.append(role)

        if not unique_roles:

            unique_roles.append("Professional")

        return unique_roles[:10]