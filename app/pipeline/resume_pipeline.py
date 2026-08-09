from app.dashboard.ats_dashboard import ATSDashboard
from app.engines.ats_engine import ATSEngine
from app.optimizer.resume_optimizer import ResumeOptimizer
from app.reports.ats_report_generator import ATSReportGenerator
from app.reports.pdf_report_generator import PDFReportGenerator


class ResumePipeline:
    """
    End-to-End Resume Review Pipeline

    Flow
    ----
    Resume
        ↓
    ATS Engine
        ↓
    ATS Dashboard
        ↓
    Resume Optimizer
        ↓
    Detailed ATS Report
        ↓
    PDF Report
    """

    def __init__(self):

        self.engine = ATSEngine()
        self.dashboard = ATSDashboard()
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
    # Dashboard
    # ----------------------------------------------------

    def generate_dashboard(
        self,
        ats_report,
        resume,
    ):

        candidate_name = "Candidate"

        personal = resume.get("personal")

        if personal and getattr(personal, "name", None):

            candidate_name = personal.name

        self.dashboard.show(
            ats_report,
            candidate_name,
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

        # Step 1 - ATS Analysis
        ats_report = self.analyze(
            resume,
            jd,
        )

        # Step 2 - ATS Dashboard
        self.generate_dashboard(
            ats_report,
            resume,
        )

        # Step 3 - Resume Optimization
        optimization = self.optimize(
            ats_report,
        )

        # Step 4 - Detailed Console Report
        self.generate_console_report(
            ats_report,
            optimization,
        )

        # Step 5 - PDF Report
        self.generate_pdf_report(
            ats_report,
            resume,
        )

        return ats_report