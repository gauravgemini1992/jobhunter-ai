from typing import List


class JobRanker:
    """
    Smart Job Ranking Engine

    Scores jobs using multiple signals:

    • Resume Skills
    • Job Title
    • Job Description
    • Job Skills

    Final score is capped at 100.
    """

    # --------------------------------------------------

    def rank_jobs(
        self,
        jobs,
        resume_skills: List[str],
    ):

        resume_terms = {
            skill.lower().strip()
            for skill in resume_skills
        }

        for job in jobs:

            score = 0

            searchable = " ".join(

                [
                    job.title,
                    job.description,
                    " ".join(job.skills),
                ]

            ).lower()

            # ------------------------------------------
            # Skill Match
            # ------------------------------------------

            matched = 0

            for term in resume_terms:

                if term in searchable:

                    matched += 1

            if resume_terms:

                skill_score = int(
                    (matched / len(resume_terms)) * 60
                )

            else:

                skill_score = 0

            score += skill_score

            # ------------------------------------------
            # Job Title Bonus
            # ------------------------------------------

            title = job.title.lower()

            title_keywords = [

                "customer success",
                "customer success manager",
                "account manager",
                "key account",
                "enterprise",
                "client success",
                "technical account",
                "customer experience",

            ]

            for keyword in title_keywords:

                if keyword in title:

                    score += 20
                    break

            # ------------------------------------------
            # SaaS Bonus
            # ------------------------------------------

            description = job.description.lower()

            saas_keywords = [

                "saas",
                "crm",
                "customer",
                "renewal",
                "retention",
                "enterprise",
                "stakeholder",

            ]

            matches = sum(

                1

                for keyword in saas_keywords

                if keyword in description

            )

            score += matches * 3

            # ------------------------------------------
            # Cap score
            # ------------------------------------------

            job.ats_match_score = min(score, 100)

        jobs.sort(

            key=lambda job: job.ats_match_score,

            reverse=True,

        )

        return jobs