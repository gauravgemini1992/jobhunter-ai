from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QFrame,
)

from desktop.ui.components.upload_card import UploadCard


class ResumePage(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        # ==========================================
        # Main Layout
        # ==========================================

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(25)

        # ==========================================
        # Header
        # ==========================================

        title = QLabel("Resume Intelligence")
        title.setObjectName("heading")

        subtitle = QLabel(
            "Upload, analyze and optimize your resume using AI-powered ATS intelligence."
        )
        subtitle.setObjectName("desc")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # ==========================================
        # Upload Card
        # ==========================================

        self.upload_card = UploadCard()
        self.upload_card.file_selected.connect(self.resume_selected)

        main_layout.addWidget(self.upload_card)

        # ==========================================
        # Quick Actions
        # ==========================================

        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(15)

        self.analyze_btn = QPushButton("Analyze Resume")
        self.analyze_btn.setFixedHeight(45)
        self.analyze_btn.setEnabled(False)

        self.optimize_btn = QPushButton("Optimize Resume")
        self.optimize_btn.setFixedHeight(45)
        self.optimize_btn.setEnabled(False)

        self.export_btn = QPushButton("Export Report")
        self.export_btn.setFixedHeight(45)
        self.export_btn.setEnabled(False)

        actions_layout.addWidget(self.analyze_btn)
        actions_layout.addWidget(self.optimize_btn)
        actions_layout.addWidget(self.export_btn)

        main_layout.addLayout(actions_layout)

        # ==========================================
        # Results Panel (Placeholder)
        # ==========================================

        self.results_panel = QFrame()
        self.results_panel.setObjectName("resultsPanel")

        results_layout = QVBoxLayout(self.results_panel)

        self.results_title = QLabel("Resume Analysis")
        self.results_title.setObjectName("resultsTitle")

        self.results_text = QLabel(
            "Upload your resume to begin AI-powered analysis.\n\n"
            "The following information will appear here:\n\n"
            "• ATS Score\n"
            "• Skills Detected\n"
            "• Missing Skills\n"
            "• Resume Strengths\n"
            "• Improvement Recommendations\n"
            "• AI Career Suggestions"
        )

        self.results_text.setWordWrap(True)
        self.results_text.setAlignment(Qt.AlignTop)

        results_layout.addWidget(self.results_title)
        results_layout.addWidget(self.results_text)

        main_layout.addWidget(self.results_panel)

        main_layout.addStretch()

        # ==========================================
        # Styling
        # ==========================================

        self.setStyleSheet("""
            QFrame#resultsPanel {
                background: #1E293B;
                border-radius: 16px;
                padding: 20px;
            }

            QLabel#resultsTitle {
                font-size: 20px;
                font-weight: bold;
                color: white;
                margin-bottom: 10px;
            }

            QPushButton {
                background: #2563EB;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px 20px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover:enabled {
                background: #1D4ED8;
            }

            QPushButton:disabled {
                background: #334155;
                color: #94A3B8;
            }
        """)

    # ==========================================
    # Signals
    # ==========================================

    def resume_selected(self, file_path):

        print(f"Selected Resume: {file_path}")

        self.analyze_btn.setEnabled(True)
        self.optimize_btn.setEnabled(True)
        self.export_btn.setEnabled(True)

        self.results_text.setText(
            f"Selected Resume\n\n"
            f"{file_path}\n\n"
            f"Status: Ready for AI Analysis.\n\n"
            f"Click 'Analyze Resume' to start."
        )