from typing import List


class JobRanker:
    """
    Ranks jobs based on skill similarity
    between the resume and the job.
    """

    # --------------------------------------------------

    def score_job(
        self,
        resume_skills: List[str],
        job_skills: List[str],
    ) -> int:

        if not resume_skills:
            return 0

        resume = {
            skill.lower().strip()
            for skill in resume_skills
        }

        job = {
            skill.lower().strip()
            for skill in job_skills
        }

        matched = resume.intersection(job)

        return int(
            (len(matched) / len(resume)) * 100
        )

    # --------------------------------------------------

    def rank_jobs(
        self,
        jobs,
        resume_skills: List[str],
    ):

        for job in jobs:

            job.ats_match_score = self.score_job(
                resume_skills,
                job.skills,
            )

        jobs.sort(
            key=lambda job: job.ats_match_score,
            reverse=True,
        )

        return jobs