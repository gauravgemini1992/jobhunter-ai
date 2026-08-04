import time

from resume_parser import parse_resume

from app.data.all_skills import ALL_SKILLS
from app.parsers.skill_extractor import SkillExtractor

from app.providers.arbeitnow_provider import ArbeitnowProvider
from app.providers.remoteok_provider import RemoteOKProvider
from app.providers.mock_provider import MockProvider
from app.providers.search_link_provider import SearchLinkProvider

from app.services.job_search_service import JobSearchService

from app.utils.job_ranker import JobRanker


class JobFinderService:
    """
    Handles the complete Job Finder workflow.

    Workflow

        Resume
            │
            ▼
        Skill Extraction
            │
            ▼
        Live Providers
            │
            ├── Arbeitnow
            ├── RemoteOK
            └── Mock Provider (Fallback)
            │
            ▼
        Smart Ranking
            │
            ▼
        Top 10 Jobs
            │
            ▼
        Smart Search Links
    """

    def __init__(self):

        self.search_service = JobSearchService()
        self.search_links = SearchLinkProvider()
        self.job_ranker = JobRanker()

        # --------------------------------------------------
        # Register Providers
        # --------------------------------------------------

        # Live Provider 1
        self.search_service.add_provider(
            ArbeitnowProvider()
        )

        # Live Provider 2
        self.search_service.add_provider(
            RemoteOKProvider()
        )

        # Fallback Provider
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

        extractor = SkillExtractor(ALL_SKILLS)

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

        resume_skills = self._extract_skills(resume)

        print()
        print("Detected Skills")

        if resume_skills:

            print(", ".join(resume_skills))

        else:

            print("No matching skills detected.")

        print()
        print("Generating Search Query...")
        print("Searching Jobs...")

        # --------------------------------------------------
        # Start Timer
        # --------------------------------------------------

        start_time = time.time()

        jobs = self.search_service.search(
            keywords=resume_skills
        )

        jobs = self.job_ranker.rank_jobs(
            jobs,
            resume_skills,
        )

        search_time = round(
            time.time() - start_time,
            2,
        )

        # --------------------------------------------------
        # Statistics
        # --------------------------------------------------

        live_jobs = sum(
            1
            for job in jobs
            if job.source != "Mock Provider"
        )

        mock_jobs = sum(
            1
            for job in jobs
            if job.source == "Mock Provider"
        )

        provider_count = self.search_service.provider_count()

        # --------------------------------------------------
        # Show only Top 10
        # --------------------------------------------------

        jobs = jobs[:10]

        print()
        print("=" * 70)
        print("JOB SEARCH SUMMARY")
        print("=" * 70)

        print(f"🔎 Providers Used : {provider_count}")
        print(f"🌍 Live Jobs Found : {live_jobs}")
        print(f"🧪 Mock Jobs Added : {mock_jobs}")
        print(f"🏆 Displayed Jobs  : {len(jobs)}")
        print(f"⏱ Search Time     : {search_time} sec")

        print()
        print("=" * 70)
        print("TOP MATCHING JOBS")
        print("=" * 70)

        if not jobs:

            print()
            print("No matching jobs found.")
            return

        for index, job in enumerate(
            jobs,
            start=1,
        ):

            print()
            print(f"Rank #{index}")

            job.display()

        # --------------------------------------------------
        # Smart Search Links
        # --------------------------------------------------

        links = self.search_links.generate_links(
            role,
            resume_skills,
        )

        print()
        print("=" * 70)
        print("SMART SEARCH LINKS")
        print("=" * 70)

        print()
        print("Generated Search Query")
        print("-" * 70)
        print(links["query"])

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
            print(links[platform])
            print()