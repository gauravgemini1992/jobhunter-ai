class ATSDashboard:
    """
    Displays a recruiter-friendly ATS dashboard.
    """

    BAR_LENGTH = 25

    # ----------------------------------------------------

    def progress_bar(self, score):

        filled = int((score / 100) * self.BAR_LENGTH)

        return (
            "█" * filled
            + "░" * (self.BAR_LENGTH - filled)
        )

    # ----------------------------------------------------

    def recruiter_rating(self, score):

        if score >= 90:
            return "★★★★★"

        if score >= 80:
            return "★★★★☆"

        if score >= 70:
            return "★★★☆☆"

        if score >= 60:
            return "★★☆☆☆"

        return "★☆☆☆☆"

    # ----------------------------------------------------

    def interview_probability(self, score):

        if score >= 90:
            return "95%"

        if score >= 80:
            return "85%"

        if score >= 70:
            return "75%"

        if score >= 60:
            return "60%"

        return "35%"

    # ----------------------------------------------------

    def resume_quality(self, score):

        if score >= 90:
            return "Outstanding"

        if score >= 80:
            return "Excellent"

        if score >= 70:
            return "Strong"

        if score >= 60:
            return "Average"

        return "Needs Improvement"

    # ----------------------------------------------------

    def show(self, report, candidate_name):

        print()
        print("=" * 60)
        print("              JOBHUNTER AI DASHBOARD")
        print("=" * 60)

        print()

        print(f"Candidate           : {candidate_name}")
        print(f"Overall ATS Score   : {report.overall_score}%")
        print(f"Recruiter Rating    : {self.recruiter_rating(report.overall_score)}")
        print(f"Interview Chance    : {self.interview_probability(report.overall_score)}")
        print(f"Resume Quality      : {self.resume_quality(report.overall_score)}")

        print()
        print("-" * 60)

        print(
            f"Skills              {self.progress_bar(report.skill_score)} {report.skill_score}%"
        )

        print(
            f"Experience         {self.progress_bar(report.experience_score)} {report.experience_score}%"
        )

        print(
            f"Education          {self.progress_bar(report.education_score)} {report.education_score}%"
        )

        print(
            f"Responsibilities   {self.progress_bar(report.responsibility_score)} {report.responsibility_score}%"
        )

        print(
            f"Keywords           {self.progress_bar(report.keyword_score)} {report.keyword_score}%"
        )

        print()
        print("-" * 60)

        print("Top Strengths")

        if report.strengths:

            for item in report.strengths[:5]:
                print(f"✔ {item}")

        else:

            print("No strengths identified.")

        print()
        print("-" * 60)

        print("Needs Improvement")

        if report.weaknesses:

            for item in report.weaknesses[:5]:
                print(f"🔴 {item}")

        else:

            print("No major weaknesses.")

        print()
        print("=" * 60)