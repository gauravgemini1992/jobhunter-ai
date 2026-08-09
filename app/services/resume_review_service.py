"""
============================================================
JobHunter AI
Resume Review Service
============================================================
"""

from app.session import Session

from app.parsers.jd_parser import JDParser
from app.pipeline.resume_pipeline import ResumePipeline


class ResumeReviewService:
    """
    Resume Review Service

    Uses the resume already loaded into the
    application session.
    """

    def __init__(self):

        self.pipeline = ResumePipeline()

        self.jd_parser = JDParser()

    # ----------------------------------------------------

    def _get_resume(self):
        """
        Return the parsed resume stored
        in the application session.
        """

        if Session.resume is None:

            print()
            print("❌ Resume not loaded.")
            print("Please restart JobHunter AI.")
            print()

            return None

        return Session.resume

    # ----------------------------------------------------

    def read_job_description(self):
        """
        Read the Job Description from the user.
        """

        print()

        print("=" * 70)
        print("PASTE THE JOB DESCRIPTION")
        print("Press ENTER twice when finished.")
        print("=" * 70)

        lines = []

        blank = 0

        while True:

            line = input()

            if not line.strip():

                blank += 1

                if blank == 2:

                    break

            else:

                blank = 0

            lines.append(line)

        return "\n".join(lines)

    # ----------------------------------------------------

    def run(self):

        print()
        print("=" * 70)
        print("RESUME REVIEW")
        print("=" * 70)

        # --------------------------------------------------
        # Load Resume From Session
        # --------------------------------------------------

        resume = self._get_resume()

        if resume is None:

            return

        print()
        print("Using Resume Loaded In Session...")

        # --------------------------------------------------
        # Read Job Description
        # --------------------------------------------------

        jd_text = self.read_job_description()

        if not jd_text.strip():

            print()
            print("❌ Job Description cannot be empty.")
            print()

            return

        # --------------------------------------------------
        # Parse JD
        # --------------------------------------------------

        jd = self.jd_parser.parse(
            jd_text
        )

        # --------------------------------------------------
        # Temporary Debug Output
        # --------------------------------------------------

        print()
        print("=" * 70)
        print("DEBUG - JD OBJECT")
        print("=" * 70)

        print(
            "Job Title        :",
            jd.job_title,
        )

        print(
            "Skills           :",
            jd.skills,
        )

        print(
            "Responsibilities :",
            jd.responsibilities,
        )

        print(
            "Education        :",
            jd.education,
        )

        print(
            "Experience       :",
            jd.experience,
        )

        print("=" * 70)
        print()

        # --------------------------------------------------
        # Run Resume Review Pipeline
        # --------------------------------------------------

        self.pipeline.run(

            resume,

            jd,

        )

        print()
        print("=" * 70)
        print("✅ Resume Review Completed")
        print("=" * 70)