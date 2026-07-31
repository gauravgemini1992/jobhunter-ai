from app.engines.ats_engine import ATSEngine
from app.optimizer.resume_optimizer import ResumeOptimizer
from app.reports.ats_report_generator import ATSReportGenerator


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
        ATS Report Generator
    """

    def __init__(self):

        self.engine = ATSEngine()
        self.optimizer = ResumeOptimizer()
        self.report_generator = ATSReportGenerator()

    # ----------------------------------------------------

    def analyze(self, resume, jd):

        return self.engine.calculate_match(
            resume,
            jd,
        )

    # ----------------------------------------------------

    def optimize(self, ats_report):

        return self.optimizer.optimize(
            ats_report
        )

    # ----------------------------------------------------

    def generate_report(
        self,
        ats_report,
        optimization,
    ):

        self.report_generator.print_report(
            ats_report,
            optimization,
        )

    # ----------------------------------------------------

    def run(
        self,
        resume,
        jd,
    ):

        ats_report = self.analyze(
            resume,
            jd,
        )

        optimization = self.optimize(
            ats_report,
        )

        self.generate_report(
            ats_report,
            optimization,
        )

        return ats_report