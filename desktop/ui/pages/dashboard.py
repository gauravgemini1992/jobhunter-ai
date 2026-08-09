from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)

from desktop.ui.components.stat_card import StatCard


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)

        # -------------------------
        # Heading
        # -------------------------

        heading = QLabel("Career Command Center")
        heading.setObjectName("heading")

        subtitle = QLabel(
            "Welcome back! Your AI Career Copilot is ready."
        )

        subtitle.setObjectName("desc")

        layout.addWidget(heading)
        layout.addWidget(subtitle)

        # -------------------------
        # Dashboard Cards
        # -------------------------

        cards = QHBoxLayout()

        cards.setSpacing(20)

        cards.addWidget(
            StatCard(
                "Career Health",
                "92%",
                "Excellent"
            )
        )

        cards.addWidget(
            StatCard(
                "ATS Score",
                "91%",
                "Strong Resume"
            )
        )

        cards.addWidget(
            StatCard(
                "Job Matches",
                "147",
                "Available"
            )
        )

        cards.addWidget(
            StatCard(
                "Reports",
                "18",
                "Generated"
            )
        )

        layout.addLayout(cards)

        layout.addStretch()