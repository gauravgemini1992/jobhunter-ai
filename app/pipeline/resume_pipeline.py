from app.engines.ats_engine import ATSEngine
from app.optimizer.resume_optimizer import ResumeOptimizer
from app.reports.ats_report_generator import ATSReportGenerator
from app.reports.pdf_report_generator import PDFReportGenerator


class ResumePipeline:
    """
    End-to-end Resume Review Pipeline.

    Flow:
        Resume
            ↓
        ATS Engine
            ↓
        Resume Optimizer
            ↓
        Console ATS Report
            ↓
        PDF ATS Report
    """

    def __init__(self):

        self.engine = ATSEngine()
        self.optimizer = ResumeOptimizer()
        self.report_generator = ATSReportGenerator()
        self.pdf_generator = PDFReportGenerator()

    # ----------------------------------------------------
    # ATS Analysis
    # ----------------------------------------------------

    def analyze(self, resume, jd):

        return self.engine.calculate_match(
            resume,
            jd,
        )

    # ----------------------------------------------------
    # Resume Optimization
    # ----------------------------------------------------

    def optimize(self, ats_report):

        return self.optimizer.optimize(
            ats_report,
        )

    # ----------------------------------------------------
    # Console Report
    # ----------------------------------------------------

    def generate_console_report(
        self,
        ats_report,
        optimization,
    ):

        self.report_generator.print_report(
            ats_report,
            optimization,
        )

    # ----------------------------------------------------
    # PDF Report
    # ----------------------------------------------------

    def generate_pdf_report(
        self,
        ats_report,
        resume,
    ):

        candidate_name = "Candidate"

        personal = resume.get("personal")

        if personal and getattr(personal, "name", None):
            candidate_name = personal.name

        pdf_path = self.pdf_generator.generate(
            ats_report,
            candidate_name,
        )

        print()
        print("=" * 70)
        print("📄 PDF Report Generated Successfully")
        print("=" * 70)
        print(pdf_path)
        print("=" * 70)

        return pdf_path

    # ----------------------------------------------------
    # Complete Pipeline
    # ----------------------------------------------------

    def run(
        self,
        resume,
        jd,
    ):

        # ATS Analysis
        ats_report = self.analyze(
            resume,
            jd,
        )

        # ---------------- DEBUG ----------------

        print()
        print("=" * 70)
        print("DEBUG - ATS REPORT")
        print("=" * 70)
        print("Matched Skills            :", ats_report.matched_skills)
        print("Missing Skills            :", ats_report.missing_skills)
        print("Strengths                :", ats_report.strengths)
        print("Weaknesses               :", ats_report.weaknesses)
        print("Matched Responsibilities :", ats_report.matched_responsibilities)
        print("Missing Responsibilities :", ats_report.missing_responsibilities)
        print("=" * 70)
        print()

        # Resume Optimization
        optimization = self.optimize(
            ats_report,
        )

        # Console Report
        self.generate_console_report(
            ats_report,
            optimization,
        )

        # PDF Report
        self.generate_pdf_report(
            ats_report,
            resume,
        )

        return ats_report