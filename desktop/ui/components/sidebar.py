from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from desktop.ui.theme.colors import SIDEBAR


class Sidebar(QWidget):

    page_changed = Signal(int)

    def __init__(self):
        super().__init__()

        self.setFixedWidth(260)
        self.setObjectName("sidebar")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        logo = QLabel("JobHunter AI")
        logo.setObjectName("logo")

        subtitle = QLabel("AI Career Copilot")
        subtitle.setObjectName("subtitle")

        layout.addWidget(logo)
        layout.addWidget(subtitle)
        layout.addSpacing(30)

        menu = [
            ("🏠", "Dashboard"),
            ("📄", "Resume Intelligence"),
            ("🎯", "ATS Intelligence"),
            ("💼", "Smart Job Match"),
            ("🏢", "Companies"),
            ("📑", "Reports"),
            ("⚙", "Settings"),
        ]

        for index, (icon, text) in enumerate(menu):

            button = QPushButton(f"{icon}   {text}")
            button.setCursor(Qt.PointingHandCursor)

            button.clicked.connect(
                lambda checked=False, i=index: self.page_changed.emit(i)
            )

            layout.addWidget(button)

        layout.addStretch()

        self.setStyleSheet(f"""
            QWidget#sidebar {{
                background: {SIDEBAR};
            }}

            QLabel#logo {{
                font-size:28px;
                font-weight:bold;
                color:white;
            }}

            QLabel#subtitle {{
                color:#94A3B8;
                font-size:13px;
            }}

            QPushButton {{
                border:none;
                text-align:left;
                padding:12px;
                border-radius:10px;
                color:white;
                background:transparent;
                font-size:14px;
            }}

            QPushButton:hover {{
                background:#1E293B;
            }}
        """)