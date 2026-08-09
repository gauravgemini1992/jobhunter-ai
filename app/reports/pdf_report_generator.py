from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from config.settings import (
    APP_NAME,
    VERSION,
    OUTPUT_DIR,
    PDF_TITLE,
)


class PDFReportGenerator:

    def __init__(self):

        Path(OUTPUT_DIR).mkdir(exist_ok=True)

        self.styles = getSampleStyleSheet()

        self.title_style = self.styles["Heading1"]
        self.title_style.alignment = TA_CENTER
        self.title_style.textColor = HexColor("#0A66C2")

        self.heading_style = self.styles["Heading2"]

        self.body_style = self.styles["BodyText"]

    def generate(self, report, candidate_name="Candidate"):

        filename = (
            f"{OUTPUT_DIR}/ATS_Report_"
            f"{candidate_name.replace(' ', '_')}.pdf"
        )

        doc = SimpleDocTemplate(filename)

        story = []

        # --------------------------
        # Cover
        # --------------------------

        story.append(Paragraph(APP_NAME, self.title_style))
        story.append(Spacer(1, 20))

        story.append(Paragraph(PDF_TITLE, self.heading_style))
        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                f"<b>Candidate:</b> {candidate_name}",
                self.body_style,
            )
        )

        story.append(
            Paragraph(
                f"<b>ATS Score:</b> {report.overall_score}%",
                self.body_style,
            )
        )

        story.append(
            Paragraph(
                f"<b>Version:</b> {VERSION}",
                self.body_style,
            )
        )

        story.append(Spacer(1, 25))

        # --------------------------
        # Strengths
        # --------------------------

        story.append(Paragraph("Strengths", self.heading_style))

        if report.strengths:
            for skill in report.strengths:
                story.append(
                    Paragraph(f"• {skill.title()}", self.body_style)
                )
        else:
            story.append(
                Paragraph("No major strengths identified.", self.body_style)
            )

        story.append(Spacer(1, 20))

        # --------------------------
        # Weaknesses
        # --------------------------

        story.append(Paragraph("Weaknesses", self.heading_style))

        if report.weaknesses:
            for skill in report.weaknesses:
                story.append(
                    Paragraph(f"• {skill.title()}", self.body_style)
                )
        else:
            story.append(
                Paragraph("No major weaknesses.", self.body_style)
            )

        story.append(Spacer(1, 20))

        # --------------------------
        # Recommendations
        # --------------------------

        story.append(
            Paragraph("Recommendations", self.heading_style)
        )

        if report.recommendations:
            for rec in report.recommendations:
                story.append(
                    Paragraph(
                        f"{rec.priority}: {rec.message}",
                        self.body_style,
                    )
                )
        else:
            story.append(
                Paragraph("Resume looks good.", self.body_style)
            )

        doc.build(story)

        return filename