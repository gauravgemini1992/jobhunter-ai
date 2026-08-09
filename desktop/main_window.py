from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFrame
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("JobHunter AI • AI Career Copilot")
        self.resize(1500,900)

        self.build_ui()

    def build_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        layout.setContentsMargins(0,0,0,0)

        layout.setSpacing(0)

        # Sidebar

        sidebar = QFrame()

        sidebar.setFixedWidth(250)

        sidebar.setObjectName("sidebar")

        sidebar_layout = QVBoxLayout(sidebar)

        sidebar_layout.setContentsMargins(20,20,20,20)

        title = QLabel("JobHunter AI")

        title.setObjectName("logo")

        sidebar_layout.addWidget(title)

        subtitle = QLabel("AI Career Copilot")

        subtitle.setObjectName("subtitle")

        sidebar_layout.addWidget(subtitle)

        sidebar_layout.addSpacing(30)

        menu = [

            "Dashboard",

            "Resume Intelligence",

            "ATS Intelligence",

            "Smart Job Match",

            "Company Intelligence",

            "AI Career Coach",

            "Reports",

            "Analytics",

            "Settings"

        ]

        for item in menu:

            button = QPushButton(item)

            button.setCursor(Qt.PointingHandCursor)

            sidebar_layout.addWidget(button)

        sidebar_layout.addStretch()

        # Content

        content = QWidget()

        content_layout = QVBoxLayout(content)

        heading = QLabel("Career Command Center")

        heading.setObjectName("heading")

        content_layout.addWidget(heading)

        desc = QLabel(

            "Welcome back! Your AI Career Copilot is ready."

        )

        desc.setObjectName("desc")

        content_layout.addWidget(desc)

        content_layout.addStretch()

        layout.addWidget(sidebar)

        layout.addWidget(content)

        self.setStyleSheet("""

        QMainWindow{

            background:#0F172A;

        }

        QWidget{

            background:#0F172A;

            color:white;

            font-size:14px;

            font-family:Segoe UI;

        }

        #sidebar{

            background:#111827;

        }

        #logo{

            font-size:28px;

            font-weight:700;

        }

        #subtitle{

            color:#94A3B8;

        }

        QPushButton{

            background:transparent;

            color:white;

            border:none;

            text-align:left;

            padding:14px;

            border-radius:8px;

        }

        QPushButton:hover{

            background:#1E293B;

        }

        #heading{

            font-size:34px;

            font-weight:700;

        }

        #desc{

            color:#94A3B8;

            font-size:16px;

        }

        """)