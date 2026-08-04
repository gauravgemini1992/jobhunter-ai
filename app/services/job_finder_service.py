import time

from resume_parser import parse_resume

from app.data.all_skills import ALL_SKILLS
from app.parsers.skill_extractor import SkillExtractor

from app.providers.arbeitnow_provider import ArbeitnowProvider
from app.providers.adzuna_provider import AdzunaProvider
from app.providers.mock_provider import MockProvider
from app.providers.search_link_provider import SearchLinkProvider

from app.services.job_search_service import JobSearchService

from app.utils.job_ranker import JobRanker
from app.utils.role_inference import RoleInference


class JobFinderService:
    """
    JobHunter AI

    Complete Job Finder Workflow

        Resume
            │
            ▼
        Skill Extraction
            │
            ▼
        AI Role Inference
            │
            ▼
        Arbeitnow
            │
            ▼
        Adzuna India
            │
            ▼
        Mock Provider (Fallback)
            │
            ▼
        Smart Job Ranking
            │
            ▼
        Top Matching Jobs
            │
            ▼
        Smart Search Links
    """

    # --------------------------------------------------

    def __init__(self):

        self.search_service = JobSearchService()
        self.search_links = SearchLinkProvider()
        self.job_ranker = JobRanker()

        # --------------------------------------------------
        # Register Providers
        # --------------------------------------------------

        # Primary Live Provider

        self.search_service.add_provider(
            ArbeitnowProvider()
        )

        # India Jobs

        self.search_service.add_provider(
            AdzunaProvider()
        )

        # Fallback

        self.search_service.add_provider(
            MockProvider()
        )

    # --------------------------------------------------

    def _extract_role(self, resume):

        experiences = resume.get("experience", [])

        if experiences:

            latest = experiences[0]

            if getattr(latest, "designation", ""):

                return latest.designation

        return "Professional"

    # --------------------------------------------------

    def _extract_skills(self, resume):

        extractor = SkillExtractor(
            ALL_SKILLS
        )

        return extractor.extract(

            resume.get("skills", "")

        )

    # --------------------------------------------------

    def run(self):

        print()
        print("=" * 70)
        print("JOB FINDER")
        print("=" * 70)

        print()
        print("Reading Resume...")

        resume = parse_resume("resume.docx")

        role = self._extract_role(resume)

        resume_skills = self._extract_skills(
            resume
        )

        print()
        print("Detected Skills")

        if resume_skills:

            print(
                ", ".join(resume_skills)
            )

        else:

            print(
                "No matching skills detected."
            )

        # --------------------------------------------------
        # AI Role Recommendation
        # --------------------------------------------------

        inferred_roles = RoleInference.infer_roles(
            resume_skills
        )

        print()
        print("=" * 70)
        print("AI RECOMMENDED ROLES")
        print("=" * 70)

        for index, role_name in enumerate(

            inferred_roles,

            start=1,

        ):

            print(
                f"{index}. {role_name}"
            )

        primary_role = (

            inferred_roles[0]

            if inferred_roles

            else role

        )

        print()
        print("Generating Search Query...")
        print("Searching Jobs...")

        # --------------------------------------------------
        # Search
        # --------------------------------------------------

        start_time = time.time()

        jobs = self.search_service.search(

            keywords=resume_skills

        )

        jobs = self.job_ranker.rank_jobs(

            jobs,

            resume_skills,

        )

        elapsed = round(

            time.time() - start_time,

            2,

        )

        # --------------------------------------------------
        # Statistics
        # --------------------------------------------------

        arbeitnow_jobs = sum(

            1

            for job in jobs

            if job.source == "Arbeitnow"

        )

        adzuna_jobs = sum(

            1

            for job in jobs

            if job.source == "Adzuna"

        )

        mock_jobs = sum(

            1

            for job in jobs

            if job.source == "Mock Provider"

        )

        live_jobs = arbeitnow_jobs + adzuna_jobs

        provider_count = (

            self.search_service.provider_count()

        )

        jobs = jobs[:10]

        print()
        print("=" * 70)
        print("JOB SEARCH SUMMARY")
        print("=" * 70)

        print(
            f"🔎 Providers Used  : {provider_count}"
        )

        print(
            f"🌍 Arbeitnow Jobs  : {arbeitnow_jobs}"
        )

        print(
            f"🇮🇳 Adzuna Jobs    : {adzuna_jobs}"
        )

        print(
            f"🧪 Mock Jobs       : {mock_jobs}"
        )

        print(
            f"📦 Live Jobs Total : {live_jobs}"
        )

        print(
            f"🏆 Displayed Jobs  : {len(jobs)}"
        )

        print(
            f"⏱ Search Time     : {elapsed} sec"
        )

        # --------------------------------------------------
        # Display Jobs
        # --------------------------------------------------

        print()
        print("=" * 70)
        print("TOP MATCHING JOBS")
        print("=" * 70)

        if not jobs:

            print()
            print(
                "No matching jobs found."
            )

            return

        for index, job in enumerate(

            jobs,

            start=1,

        ):

            print()

            print(
                f"Rank #{index}"
            )

            job.display()

        # --------------------------------------------------
        # Smart Search Links
        # --------------------------------------------------

        links = self.search_links.generate_links(

            primary_role,

            resume_skills,

        )

        print()
        print("=" * 70)
        print("SMART SEARCH LINKS")
        print("=" * 70)

        print()
        print("Generated Search Query")
        print("-" * 70)

        print(
            links["query"]
        )

        print()

        for platform in [

            "LinkedIn",
            "Naukri",
            "Indeed",
            "Foundit",
            "Wellfound",
            "Google Jobs",

        ]:

            print(platform)

            print(
                links[platform]
            )

            print()