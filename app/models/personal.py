"""
============================================================
JobHunter AI
Personal Model
============================================================
"""


class Personal:
    """
    Stores candidate personal information.
    """

    def __init__(self):

        self.name = ""
        self.email = ""
        self.phone = ""
        self.location = ""

    def __repr__(self):

        return (
            f"Personal("
            f"name='{self.name}', "
            f"email='{self.email}', "
            f"phone='{self.phone}', "
            f"location='{self.location}')"
        )