"""
============================================================
JobHunter AI
Application Session
============================================================

Stores runtime data while the application is running.

Nothing in this class is saved permanently.
Everything is cleared when the application exits.
============================================================
"""


class Session:
    """
    Runtime session shared across the application.
    """

    # --------------------------------------------------
    # Logged-in User
    # --------------------------------------------------

    profile = None

    # --------------------------------------------------
    # Resume Information
    # --------------------------------------------------

    resume_path = None

    resume = None

    # --------------------------------------------------
    # Current Search State
    # --------------------------------------------------

    current_role = None

    current_skills = []

    current_jobs = []

    # --------------------------------------------------
    # Utility
    # --------------------------------------------------

    @classmethod
    def reset(cls):
        """
        Reset the application session.
        """

        cls.profile = None

        cls.resume_path = None

        cls.resume = None

        cls.current_role = None

        cls.current_skills = []

        cls.current_jobs = []