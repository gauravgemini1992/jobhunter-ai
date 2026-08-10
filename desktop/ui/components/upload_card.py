from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QFileDialog,
)


class UploadCard(QFrame):
    """
    Reusable upload widget.

    Emits:
        file_selected(str)
    """

    file_selected = Signal(str)

    def __init__(self):
        super().__init__()

        self.selected_file = None

        self.setAcceptDrops(True)

        self.build_ui()

    def build_ui(self):

        self.setObjectName("uploadCard")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(35, 35, 35, 35)
        layout.setSpacing(18)

        icon = QLabel("📄")
        icon.setAlignment(Qt.AlignCenter)
        icon.setObjectName("uploadIcon")

        title = QLabel("Drag & Drop Resume")
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("uploadTitle")

        subtitle = QLabel(
            "Supported formats: PDF • DOCX"
        )
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setObjectName("uploadSubtitle")

        self.filename = QLabel("No resume selected")
        self.filename.setAlignment(Qt.AlignCenter)
        self.filename.setObjectName("filename")

        self.status = QLabel("Waiting for upload")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setObjectName("status")

        browse = QPushButton("Browse Resume")
        browse.clicked.connect(self.open_dialog)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(browse)
        button_layout.addStretch()

        layout.addWidget(icon)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(10)
        layout.addWidget(self.filename)
        layout.addWidget(self.status)
        layout.addSpacing(10)
        layout.addLayout(button_layout)

        self.setStyleSheet("""
            QFrame#uploadCard{
                background:#1E293B;
                border:2px dashed #334155;
                border-radius:18px;
            }

            QLabel#uploadIcon{
                font-size:52px;
            }

            QLabel#uploadTitle{
                font-size:22px;
                font-weight:bold;
            }

            QLabel#uploadSubtitle{
                color:#94A3B8;
            }

            QLabel#filename{
                color:white;
                font-size:15px;
                font-weight:bold;
            }

            QLabel#status{
                color:#22C55E;
            }

            QPushButton{
                background:#2563EB;
                color:white;
                border:none;
                border-radius:8px;
                padding:12px 24px;
                font-weight:bold;
            }

            QPushButton:hover{
                background:#1D4ED8;
            }
        """)

    def open_dialog(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Resume",
            "",
            "Resume (*.pdf *.docx)"
        )

        if file_path:
            self.update_file(file_path)

    def update_file(self, file_path):

        self.selected_file = file_path

        self.filename.setText(Path(file_path).name)
        self.status.setText("✓ Ready for Analysis")

        self.file_selected.emit(file_path)

    def dragEnterEvent(self, event):

        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):

        urls = event.mimeData().urls()

        if not urls:
            return

        file_path = urls[0].toLocalFile()

        if file_path.lower().endswith((".pdf", ".docx")):
            self.update_file(file_path)