from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QFrame,
)


class ResumePage(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(25)

        # ======================================================
        # Header
        # ======================================================

        title = QLabel("Resume Intelligence")
        title.setObjectName("heading")

        subtitle = QLabel(
            "Upload, analyze and optimize your resume with AI-powered ATS insights."
        )
        subtitle.setObjectName("desc")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # ======================================================
        # Upload Area
        # ======================================================

        upload_frame = QFrame()
        upload_frame.setObjectName("uploadFrame")

        upload_layout = QVBoxLayout(upload_frame)
        upload_layout.setContentsMargins(40, 40, 40, 40)
        upload_layout.setSpacing(15)

        upload_icon = QLabel("📄")
        upload_icon.setAlignment(Qt.AlignCenter)
        upload_icon.setObjectName("uploadIcon")

        upload_title = QLabel("Drag & Drop Resume Here")
        upload_title.setAlignment(Qt.AlignCenter)
        upload_title.setObjectName("uploadTitle")

        upload_subtitle = QLabel(
            "Supported formats: PDF, DOCX"
        )
        upload_subtitle.setAlignment(Qt.AlignCenter)
        upload_subtitle.setObjectName("uploadSubtitle")

        browse_button = QPushButton("Browse Resume")
        browse_button.setFixedWidth(180)
        browse_button.setCursor(Qt.PointingHandCursor)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(browse_button)
        button_layout.addStretch()

        upload_layout.addWidget(upload_icon)
        upload_layout.addWidget(upload_title)
        upload_layout.addWidget(upload_subtitle)
        upload_layout.addLayout(button_layout)

        main_layout.addWidget(upload_frame)

        # ======================================================
        # Future Results Area
        # ======================================================

        placeholder = QLabel(
            "Resume analysis results will appear here after uploading your resume."
        )
        placeholder.setAlignment(Qt.AlignCenter)
        placeholder.setObjectName("placeholder")

        main_layout.addWidget(placeholder)

        main_layout.addStretch()

        # ======================================================
        # Styling
        # ======================================================

        self.setStyleSheet("""
            QFrame#uploadFrame {
                background: #1E293B;
                border: 2px dashed #334155;
                border-radius: 20px;
            }

            QLabel#uploadIcon {
                font-size: 60px;
            }

            QLabel#uploadTitle {
                font-size: 24px;
                font-weight: bold;
                color: white;
            }

            QLabel#uploadSubtitle {
                font-size: 15px;
                color: #94A3B8;
            }

            QLabel#placeholder {
                color: #64748B;
                font-size: 15px;
            }

            QPushButton {
                background: #2563EB;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px 24px;
                font-size: 14px;
                font-weight: bold;
            }

            QPushButton:hover {
                background: #1D4ED8;
            }
        """)