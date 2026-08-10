from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
)

from desktop.ui.components.sidebar import Sidebar
from desktop.ui.components.topbar import TopBar

from desktop.ui.pages.dashboard import DashboardPage
from desktop.ui.pages.resume import ResumePage
from desktop.ui.pages.ats import ATSPage
from desktop.ui.pages.jobs import JobsPage
from desktop.ui.pages.companies import CompaniesPage
from desktop.ui.pages.reports import ReportsPage
from desktop.ui.pages.settings import SettingsPage


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

        self.sidebar = Sidebar()
        main_layout.addWidget(self.sidebar)

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

        self.topbar = TopBar()
        content_layout.addWidget(self.topbar)

        # ==========================================
        # Page Stack
        # ==========================================

        self.stack = QStackedWidget()

        self.dashboard = DashboardPage()
        self.resume = ResumePage()
        self.ats = ATSPage()
        self.jobs = JobsPage()
        self.companies = CompaniesPage()
        self.reports = ReportsPage()
        self.settings = SettingsPage()

        self.stack.addWidget(self.dashboard)      # Index 0
        self.stack.addWidget(self.resume)         # Index 1
        self.stack.addWidget(self.ats)            # Index 2
        self.stack.addWidget(self.jobs)           # Index 3
        self.stack.addWidget(self.companies)      # Index 4
        self.stack.addWidget(self.reports)        # Index 5
        self.stack.addWidget(self.settings)       # Index 6

        # ==========================================
        # Connect Sidebar Navigation
        # ==========================================

        self.sidebar.page_changed.connect(self.stack.setCurrentIndex)

        # Show Dashboard by default
        self.stack.setCurrentIndex(0)

        content_layout.addWidget(self.stack)

        main_layout.addWidget(content)

        # ==========================================
        # Global Theme
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