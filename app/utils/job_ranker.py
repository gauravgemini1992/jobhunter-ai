from __future__ import annotations

from typing import Dict, Set


class JobRanker:
    """
    ==========================================================
                     JobHunter AI
                   JobRanker 3.0
    ==========================================================

    Production ATS Ranking Engine

    Ranking Factors
    ---------------

    ✓ Title Intelligence
    ✓ Resume Skills
    ✓ Company Quality
    ✓ Industry
    ✓ Experience
    ✓ Location
    ✓ Employment Type
    ✓ Salary
    ✓ Bonus Engine
    ✓ Penalty Engine

    Maximum Score = 100
    """

    # ======================================================
    # Score Weights
    # ======================================================

    TITLE_WEIGHT = 25

    SKILL_WEIGHT = 25

    COMPANY_WEIGHT = 10

    INDUSTRY_WEIGHT = 10

    LOCATION_WEIGHT = 10

    EXPERIENCE_WEIGHT = 8

    EMPLOYMENT_WEIGHT = 5

    SALARY_WEIGHT = 5

    BONUS_WEIGHT = 2

    # ======================================================
    # Company Intelligence
    # ======================================================

    TIER_A_COMPANIES: Set[str] = {

        "microsoft",
        "google",
        "amazon",
        "aws",
        "salesforce",
        "hubspot",
        "oracle",
        "servicenow",
        "adobe",
        "sap",
        "openai",
        "atlassian",
        "freshworks",
        "stripe",
        "snowflake",
        "databricks",
        "workday",

    }

    TIER_B_COMPANIES: Set[str] = {

        "zoho",
        "browserstack",
        "postman",
        "chargebee",
        "clevertap",
        "moengage",
        "rippling",
        "zendesk",
        "monday",
        "airbase",

    }

    # ======================================================
    # Preferred Roles
    # ======================================================

    TITLE_PRIORITY: Dict[str, int] = {

        "ai customer success manager": 25,

        "enterprise customer success manager": 24,

        "senior customer success manager": 23,

        "customer success manager": 22,

        "enterprise account manager": 22,

        "strategic account manager": 21,

        "technical account manager": 21,

        "key account manager": 20,

        "client partner": 18,

        "customer success lead": 18,

        "customer experience manager": 17,

        "account manager": 16,

    }

    # ======================================================
    # Industry Intelligence
    # ======================================================

    INDUSTRY_KEYWORDS: Set[str] = {

        "saas",

        "b2b",

        "enterprise",

        "customer success",

        "crm",

        "cloud",

        "aws",

        "azure",

        "gcp",

        "artificial intelligence",

        "ai",

        "machine learning",

        "llm",

        "chatgpt",

        "openai",

        "copilot",

        "cybersecurity",

        "devops",

        "platform",

        "api",

    }

    # ======================================================
    # Location Intelligence
    # ======================================================

    LOCATION_PRIORITY: Dict[str, int] = {

        "india": 10,

        "bangalore": 10,

        "bengaluru": 10,

        "hyderabad": 10,

        "pune": 10,

        "mumbai": 10,

        "chennai": 10,

        "gurgaon": 10,

        "noida": 10,

        "remote": 8,

        "singapore": 7,

        "dubai": 7,

        "uae": 7,

        "london": 6,

        "uk": 6,

        "germany": 5,

        "berlin": 5,

        "munich": 5,

    }

    # ======================================================
    # Bonus Keywords
    # ======================================================

    BONUS_KEYWORDS: Set[str] = {

        "enterprise",

        "strategic",

        "global",

        "leadership",

        "remote",

        "hybrid",

        "ai",

        "saas",

        "cloud",

        "customer success",

    }

    # ======================================================
    # Penalty Keywords
    # ======================================================

    PENALTY_KEYWORDS: Set[str] = {

        "intern",

        "internship",

        "graduate",

        "campus",

        "entry level",

        "trainee",

        "junior",

        "apprentice",

    }

    # ======================================================
    # Constructor
    # ======================================================

    def __init__(self):

        pass
        # ======================================================
    # Text Normalization
    # ======================================================

    def _normalize(
        self,
        text: str,
    ) -> str:
        """
        Normalize text for reliable matching.
        """

        if not text:
            return ""

        return text.lower().strip()

    # ======================================================
    # Company Intelligence
    # ======================================================

    def _company_score(
        self,
        company: str,
    ) -> int:
        """
        Scores companies using predefined tiers.

        Tier A : 10
        Tier B : 8
        Others : 2
        """

        company = self._normalize(company)

        if not company:
            return 0

        for name in self.TIER_A_COMPANIES:

            if name in company:

                return 10

        for name in self.TIER_B_COMPANIES:

            if name in company:

                return 8

        return 2

    # ======================================================
    # Title Intelligence
    # ======================================================

    def _title_score(
        self,
        title: str,
    ) -> int:
        """
        Scores job titles based on priority.
        """

        title = self._normalize(title)

        if not title:
            return 0

        highest = 0

        for preferred_title, score in self.TITLE_PRIORITY.items():

            if preferred_title in title:

                highest = max(
                    highest,
                    score,
                )

        return highest

    # ======================================================
    # Industry Intelligence
    # ======================================================

    def _industry_score(
        self,
        job,
    ) -> int:
        """
        Detects SaaS, AI and Enterprise jobs.
        """

        searchable = " ".join(

            [

                job.title,

                job.company,

                job.description,

                " ".join(job.skills),

            ]

        )

        searchable = self._normalize(searchable)

        matches = 0

        for keyword in self.INDUSTRY_KEYWORDS:

            if keyword in searchable:

                matches += 1

        if matches >= 6:

            return 10

        if matches >= 4:

            return 8

        if matches >= 2:

            return 6

        if matches >= 1:

            return 4

        return 0

    # ======================================================
    # Recruiter Confidence
    # ======================================================

    def _confidence_score(
        self,
        job,
    ) -> int:
        """
        Recruiter confidence score.

        High-quality jobs usually contain
        rich metadata.
        """

        score = 0

        if job.company:

            score += 2

        if job.description:

            score += 2

        if job.skills:

            score += 2

        if job.salary and "not disclosed" not in job.salary.lower():

            score += 2

        if job.apply_url:

            score += 2

        return score
        # ======================================================
    # Skill Intelligence
    # ======================================================

    def _skill_score(
        self,
        resume_skills: list[str],
        job,
    ) -> int:
        """
        Calculates the overlap between
        resume skills and job requirements.
        """

        if not resume_skills:
            return 0

        searchable = " ".join(

            [

                job.title,

                job.description,

                " ".join(job.skills),

            ]

        )

        searchable = self._normalize(searchable)

        matched = 0

        for skill in resume_skills:

            if self._normalize(skill) in searchable:

                matched += 1

        ratio = matched / len(resume_skills)

        return round(
            ratio * self.SKILL_WEIGHT
        )

    # ======================================================
    # Experience Intelligence
    # ======================================================

    def _experience_score(
        self,
        experience: str,
    ) -> int:
        """
        Scores the required experience.
        """

        experience = self._normalize(experience)

        if not experience:
            return 4

        if any(
            x in experience
            for x in [

                "10",

                "9",

                "8",

                "7",

                "6",

                "5",

            ]
        ):
            return 8

        if any(
            x in experience
            for x in [

                "4",

                "3",

            ]
        ):
            return 6

        if any(
            x in experience
            for x in [

                "2",

                "1",

            ]
        ):
            return 3

        return 4

    # ======================================================
    # Salary Intelligence
    # ======================================================

    def _salary_score(
        self,
        salary: str,
    ) -> int:
        """
        Scores salary availability and value.
        """

        salary = self._normalize(salary)

        if not salary:
            return 0

        if "not disclosed" in salary:
            return 0

        digits = "".join(

            c

            for c in salary

            if c.isdigit()

        )

        if not digits:

            return 2

        value = int(digits)

        # INR

        if value >= 3000000:

            return 5

        if value >= 1800000:

            return 4

        if value >= 1200000:

            return 3

        if value >= 700000:

            return 2

        return 1

    # ======================================================
    # Location Intelligence
    # ======================================================

    def _location_score(
        self,
        location: str,
    ) -> int:
        """
        Gives preference to India,
        followed by Remote and
        selected international markets.
        """

        location = self._normalize(location)

        if not location:
            return 0

        highest = 0

        for city, score in self.LOCATION_PRIORITY.items():

            if city in location:

                highest = max(
                    highest,
                    score,
                )

        return highest
        # ======================================================
    # Employment Intelligence
    # ======================================================

    def _employment_score(
        self,
        employment_type: str,
    ) -> int:
        """
        Scores employment type.

        Full Time      -> 5
        Permanent      -> 5
        Hybrid         -> 4
        Contract       -> 3
        Internship     -> 0
        """

        employment = self._normalize(
            employment_type
        )

        if not employment:
            return 2

        if "full" in employment:
            return 5

        if "permanent" in employment:
            return 5

        if "hybrid" in employment:
            return 4

        if "contract" in employment:
            return 3

        if "intern" in employment:
            return 0

        return 2

    # ======================================================
    # Bonus Engine
    # ======================================================

    def _bonus_score(
        self,
        job,
    ) -> int:
        """
        Rewards high-quality enterprise,
        AI and SaaS opportunities.
        """

        searchable = " ".join(

            [

                job.title,

                job.company,

                job.description,

                " ".join(job.skills),

            ]

        )

        searchable = self._normalize(
            searchable
        )

        bonus = 0

        for keyword in self.BONUS_KEYWORDS:

            if keyword in searchable:

                bonus += 1

        return min(
            bonus,
            self.BONUS_WEIGHT,
        )

    # ======================================================
    # Penalty Engine
    # ======================================================

    def _penalty_score(
        self,
        job,
    ) -> int:
        """
        Penalizes unsuitable jobs.
        """

        searchable = " ".join(

            [

                job.title,

                job.description,

            ]

        )

        searchable = self._normalize(
            searchable
        )

        penalty = 0

        for keyword in self.PENALTY_KEYWORDS:

            if keyword in searchable:

                penalty += 5

        return penalty

    # ======================================================
    # Recruiter Boost
    # ======================================================

    def _recruiter_boost(
        self,
        job,
    ) -> int:
        """
        Small boost for high-quality
        enterprise roles.
        """

        searchable = " ".join(

            [

                job.title,

                job.company,

                job.description,

            ]

        )

        searchable = self._normalize(
            searchable
        )

        boost = 0

        # Enterprise titles

        if "enterprise" in searchable:
            boost += 2

        if "strategic" in searchable:
            boost += 2

        if "customer success" in searchable:
            boost += 2

        if "account manager" in searchable:
            boost += 1

        if "manager" in searchable:
            boost += 1

        return min(
            boost,
            5,
        )
        # ======================================================
    # Final Ranking Engine
    # ======================================================

    def rank_jobs(
        self,
        jobs,
        resume_skills: list[str],
    ):
        """
        JobHunter AI Production Ranking Engine

        Computes the ATS Match Score for every job
        and returns jobs sorted from best to worst.
        """

        for job in jobs:

            score = 0

            # ------------------------------------------
            # Core Intelligence
            # ------------------------------------------

            score += self._title_score(
                job.title,
            )

            score += self._skill_score(
                resume_skills,
                job,
            )

            score += self._company_score(
                job.company,
            )

            score += self._industry_score(
                job,
            )

            score += self._experience_score(
                job.experience,
            )

            score += self._location_score(
                job.location,
            )

            score += self._employment_score(
                job.employment_type,
            )

            score += self._salary_score(
                job.salary,
            )

            # ------------------------------------------
            # Recruiter Intelligence
            # ------------------------------------------

            score += self._bonus_score(
                job,
            )

            score += self._recruiter_boost(
                job,
            )

            score += (
                self._confidence_score(job) // 2
            )

            score -= self._penalty_score(
                job,
            )

            # ------------------------------------------
            # Score Safety
            # ------------------------------------------

            score = max(0, score)

            score = min(score, 100)

            job.ats_match_score = score

        # --------------------------------------------------
        # Stable Production Sorting
        # --------------------------------------------------

        jobs.sort(

            key=lambda job: (

                job.ats_match_score,

                self._company_score(
                    job.company,
                ),

                self._title_score(
                    job.title,
                ),

                job.company.lower(),

                job.title.lower(),

            ),

            reverse=True,

        )

        return jobs

    # ======================================================
    # Ranking Summary
    # ======================================================

    def statistics(
        self,
        jobs,
    ):
        """
        Returns ranking statistics.
        """

        if not jobs:

            return {

                "highest": 0,

                "lowest": 0,

                "average": 0,

            }

        scores = [

            job.ats_match_score

            for job in jobs

        ]

        return {

            "highest": max(scores),

            "lowest": min(scores),

            "average": round(

                sum(scores) / len(scores),

                1,

            ),

        }