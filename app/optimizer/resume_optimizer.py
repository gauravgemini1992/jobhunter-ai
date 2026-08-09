from app.models.ats_report import ATSReport


class ResumeOptimizer:
    """
    AI Resume Optimizer

    Generates actionable resume improvement suggestions
    based on the ATS Report.
    """

    # ----------------------------------------------------
    # Main Optimizer
    # ----------------------------------------------------

    def optimize(self, report: ATSReport):

        return {
            "current_score": report.overall_score,
            "estimated_score": self.estimate_score(report),

            # AI Resume Content
            "professional_summary": self.generate_professional_summary(report),
            "experience_bullets": self.generate_experience_bullets(report),
            "skills_to_add": self.generate_skills_to_add(report),

            # Existing Suggestions
            "high_priority": self.get_high_priority(report),
            "medium_priority": self.get_medium_priority(report),
            "low_priority": self.get_low_priority(report),
            "summary_suggestion": self.rewrite_summary(report),
            "action_items": self.generate_action_items(report),
        }

    # ----------------------------------------------------
    # Estimated ATS Score
    # ----------------------------------------------------

    def estimate_score(self, report: ATSReport):

        score = report.overall_score

        improvement = min(
            len(report.missing_skills) * 4,
            20,
        )

        return min(score + improvement, 100)

    # ----------------------------------------------------
    # Priorities
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
    # AI Professional Summary
    # ----------------------------------------------------

    def generate_professional_summary(self, report: ATSReport):

        strengths = report.matched_skills[:5]
        missing = report.missing_skills[:5]

        summary = (
            "Experienced professional with proven expertise in "
        )

        if strengths:
            summary += ", ".join(strengths)

        summary += (
            ", delivering customer-focused solutions, "
            "collaborating with cross-functional teams, "
            "and driving measurable business outcomes."
        )

        if missing:
            summary += (
                " Consider incorporating experience related to "
                + ", ".join(missing)
                + " where it genuinely reflects your background."
            )

        return summary

    # ----------------------------------------------------
    # AI Experience Suggestions
    # ----------------------------------------------------

    def generate_experience_bullets(self, report: ATSReport):

        bullets = []

        for responsibility in report.missing_responsibilities[:5]:

            bullets.append(
                f"Demonstrated experience related to {responsibility}"
            )

        if report.missing_skills:

            bullets.append(
                "Highlighted measurable achievements using "
                + ", ".join(report.missing_skills[:3])
                + "."
            )

        if not bullets:

            bullets.append(
                "Your existing experience already aligns well with the target role."
            )

        return bullets

    # ----------------------------------------------------
    # Skills to Add
    # ----------------------------------------------------

    def generate_skills_to_add(self, report: ATSReport):

        return sorted(report.missing_skills)

    # ----------------------------------------------------
    # Summary Suggestion
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
    # Action Items
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