from resume_parser import parse_resume

from app.parsers.jd_parser import JDParser
from app.pipeline.resume_pipeline import ResumePipeline


class ResumeReviewService:

    def __init__(self):

        self.pipeline = ResumePipeline()
        self.jd_parser = JDParser()

    def read_job_description(self):

        print()

        print("=" * 70)
        print("Paste the Job Description")
        print("Press ENTER twice when finished.")
        print("=" * 70)

        lines = []

        blank = 0

        while True:

            line = input()

            if not line.strip():

                blank += 1

                if blank == 2:
                    break

            else:

                blank = 0

            lines.append(line)

        return "\n".join(lines)

    def run(self):

        print()

        print("=" * 70)
        print("Reading Resume...")
        print("=" * 70)

        resume = parse_resume("resume.docx")

        jd_text = self.read_job_description()

        jd = self.jd_parser.parse(jd_text)

        self.pipeline.run(
            resume,
            jd,
        )