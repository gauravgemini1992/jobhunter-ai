from app.models.ats_report import ATSReport


class ResumeOptimizer:
    """
    Generates resume improvement suggestions
    based on the ATS Report.
    """

    def optimize(self, report: ATSReport):

        return {
            "current_score": report.overall_score,
            "estimated_score": self.estimate_score(report),
            "high_priority": self.get_high_priority(report),
            "medium_priority": self.get_medium_priority(report),
            "low_priority": self.get_low_priority(report),
            "summary_suggestion": self.rewrite_summary(report),
            "action_items": self.generate_action_items(report),
        }

    # ----------------------------------------------------

    def estimate_score(self, report: ATSReport):

        score = report.overall_score

        improvement = min(
            len(report.missing_skills) * 4,
            20
        )

        return min(score + improvement, 100)

    # ----------------------------------------------------

    def get_high_priority(self, report: ATSReport):

        return [
            recommendation.message
            for recommendation in report.recommendations
            if recommendation.priority == "HIGH"
        ]

    # ----------------------------------------------------

    def get_medium_priority(self, report: ATSReport):

        return [
            recommendation.message
            for recommendation in report.recommendations
            if recommendation.priority == "MEDIUM"
        ]

    # ----------------------------------------------------

    def get_low_priority(self, report: ATSReport):

        return [
            recommendation.message
            for recommendation in report.recommendations
            if recommendation.priority == "LOW"
        ]

    # ----------------------------------------------------

    def rewrite_summary(self, report: ATSReport):

        if not report.missing_skills:

            return (
                "Your professional summary already aligns well "
                "with the job description."
            )

        skills = ", ".join(report.missing_skills[:5])

        return (
            "Consider updating your professional summary by "
            f"highlighting experience related to: {skills} "
            "(only if you genuinely have this experience)."
        )

    # ----------------------------------------------------

    def generate_action_items(self, report: ATSReport):

        actions = []

        for skill in report.missing_skills:

            actions.append(
                f"Add measurable achievements demonstrating {skill}."
            )

        for responsibility in report.missing_responsibilities:

            actions.append(
                f"Highlight experience related to '{responsibility}'."
            )

        return actions