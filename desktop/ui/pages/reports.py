from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class ReportsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Reports")
        title.setObjectName("heading")

        subtitle = QLabel(
            "Generate and export ATS reports."
        )
        subtitle.setObjectName("desc")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()