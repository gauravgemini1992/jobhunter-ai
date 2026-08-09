from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
)

from desktop.ui.components.sidebar import Sidebar
from desktop.ui.components.topbar import TopBar
from desktop.ui.pages.dashboard import DashboardPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("JobHunter AI • AI Career Copilot")
        self.resize(1500, 900)
        self.setMinimumSize(1280, 800)

        self.build_ui()

    def build_ui(self):

        # ==========================================
        # Central Widget
        # ==========================================

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ==========================================
        # Sidebar
        # ==========================================

        sidebar = Sidebar()
        main_layout.addWidget(sidebar)

        # ==========================================
        # Main Content Area
        # ==========================================

        content = QWidget()

        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(30, 20, 30, 20)
        content_layout.setSpacing(20)

        # ==========================================
        # Top Navigation
        # ==========================================

        topbar = TopBar()
        content_layout.addWidget(topbar)

        # ==========================================
        # Dashboard Page
        # ==========================================

        dashboard = DashboardPage()
        content_layout.addWidget(dashboard)

        # Add content area to window

        main_layout.addWidget(content)

        # ==========================================
        # Global Styles
        # ==========================================

        self.setStyleSheet("""
            QMainWindow {
                background: #0F172A;
            }

            QWidget {
                background: #0F172A;
                color: white;
                font-family: Arial;
                font-size: 14px;
            }

            QLabel#heading {
                font-size: 34px;
                font-weight: bold;
                color: white;
            }

            QLabel#desc {
                font-size: 16px;
                color: #94A3B8;
            }
        """)