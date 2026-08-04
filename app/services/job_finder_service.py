from resume_parser import parse_resume

from app.providers.mock_provider import MockProvider
from app.providers.search_link_provider import SearchLinkProvider
from app.services.job_search_service import JobSearchService
from app.utils.job_ranker import JobRanker

from app.data.all_skills import ALL_SKILLS
from app.parsers.skill_extractor import SkillExtractor


class JobFinderService:

    def __init__(self):

        self.search_service = JobSearchService()
        self.search_links = SearchLinkProvider()
        self.job_ranker = JobRanker()

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

    def _build_resume_text(self, resume):

        text = []

        text.append(resume.get("summary", ""))

        text.append(resume.get("skills", ""))

        text.append(resume.get("projects", ""))

        text.append(resume.get("certifications", ""))

        for exp in resume.get("experience", []):

            text.append(getattr(exp, "designation", ""))

            text.append(getattr(exp, "company", ""))

            description = getattr(exp, "description", "")

            if isinstance(description, list):

                text.extend(description)

            else:

                text.append(description)

        return "\n".join(
            str(item)
            for item in text
            if item
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

        resume_text = self._build_resume_text(
            resume
        )

        extractor = SkillExtractor(
            ALL_SKILLS
        )

        resume_skills = extractor.extract(
            resume_text
        )

        print()
        print("Detected Skills")

        if resume_skills:

            print(", ".join(resume_skills))

        else:

            print("No production skills detected.")

        print()
        print("Generating Search Query...")
        print("Searching Jobs...")

        jobs = self.search_service.search(
            keywords=resume_skills
        )

        jobs = self.job_ranker.rank_jobs(
            jobs,
            resume_skills,
        )

        print()
        print("=" * 70)
        print("TOP MATCHING JOBS")
        print("=" * 70)

        if not jobs:

            print("No jobs found.")

        else:

            for index, job in enumerate(
                jobs,
                start=1,
            ):

                print()

                print(f"Rank #{index}")

                job.display()

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