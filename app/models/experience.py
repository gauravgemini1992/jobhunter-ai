"""
============================================================
JobHunter AI
Experience Model
============================================================
"""


class Experience:
    """
    Stores a single work experience.
    """

    def __init__(self):

        self.company = ""
        self.designation = ""
        self.duration = ""
        self.description = []

    def __repr__(self):

        return (
            f"Experience("
            f"designation='{self.designation}', "
            f"company='{self.company}', "
            f"duration='{self.duration}')"
        )