class ATSReportGenerator:
    """
    Generates a professional console report
    from ATS Report + Resume Optimizer output.
    """

    BAR_LENGTH = 30

    # ----------------------------------------------------

    def progress_bar(self, score):

        filled = int((score / 100) * self.BAR_LENGTH)

        return "█" * filled + "░" * (self.BAR_LENGTH - filled)

    # ----------------------------------------------------

    def stars(self, score):

        if score >= 90:
            return "★★★★★"

        elif score >= 80:
            return "★★★★☆"

        elif score >= 70:
            return "★★★☆☆"

        elif score >= 60:
            return "★★☆☆☆"

        return "★☆☆☆☆"

    # ----------------------------------------------------

    def recruiter_recommendation(self, score):

        if score >= 90:
            return "Excellent Match"

        elif score >= 80:
            return "Strong Match"

        elif score >= 70:
            return "Good Match"

        elif score >= 60:
            return "Average Match"

        return "Needs Improvement"

    # ----------------------------------------------------

    def print_report(self, ats_report, optimization):

        print()
        print("=" * 70)
        print("                     JOBHUNTER AI REPORT")
        print("=" * 70)

        print()

        print("Overall ATS Score")
        print(
            f"{self.progress_bar(ats_report.overall_score)} "
            f"{ats_report.overall_score}%"
        )

        print()

        print("Estimated Score After Optimization")

        print(
            f"{self.progress_bar(optimization['estimated_score'])} "
            f"{optimization['estimated_score']}%"
        )

        print()

        print("-" * 70)

        print(f"Skill Match          : {ats_report.skill_score}%")
        print(f"Experience Match     : {ats_report.experience_score}%")
        print(f"Education Match      : {ats_report.education_score}%")
        print(f"Responsibility Match : {ats_report.responsibility_score}%")
        print(f"Keyword Match        : {ats_report.keyword_score}%")

        print()
        print("-" * 70)

        print("STRENGTHS")

        if ats_report.strengths:

            for item in ats_report.strengths:
                print(f"✔ {item}")

        else:

            print("No major strengths identified.")

        print()
        print("-" * 70)

        print("WEAKNESSES")

        if ats_report.weaknesses:

            for item in ats_report.weaknesses:
                print(f"✘ {item}")

        else:

            print("No major weaknesses identified.")

        print()
        print("-" * 70)

        print("HIGH PRIORITY")

        if optimization["high_priority"]:

            for item in optimization["high_priority"]:
                print(f"🔴 {item}")

        else:

            print("None")

        print()
        print("MEDIUM PRIORITY")

        if optimization["medium_priority"]:

            for item in optimization["medium_priority"]:
                print(f"🟡 {item}")

        else:

            print("None")

        print()
        print("LOW PRIORITY")

        if optimization["low_priority"]:

            for item in optimization["low_priority"]:
                print(f"🟢 {item}")

        else:

            print("None")

        print()
        print("-" * 70)

        # =====================================================
        # AI RESUME OPTIMIZER
        # =====================================================

        print("AI RESUME OPTIMIZER")

        print()
        print("Professional Summary")
        print()

        print(
            optimization["professional_summary"]
        )

        print()

        print("Suggested Experience Improvements")
        print()

        for bullet in optimization["experience_bullets"]:

            print(f"✔ {bullet}")

        print()

        print("Recommended Skills To Add")
        print()

        for skill in optimization["skills_to_add"]:

            print(f"✔ {skill}")

        print()

        print("-" * 70)

        print("SUMMARY SUGGESTION")
        print()

        print(
            optimization["summary_suggestion"]
        )

        print()

        print("-" * 70)

        print("ACTION ITEMS")
        print()

        for i, item in enumerate(
            optimization["action_items"],
            start=1,
        ):

            print(f"{i}. {item}")

        print()

        print("-" * 70)

        print("RECRUITER RECOMMENDATION")
        print()

        print(
            self.stars(
                ats_report.overall_score
            )
        )

        print(
            self.recruiter_recommendation(
                ats_report.overall_score
            )
        )

        print("=" * 70)
        print()