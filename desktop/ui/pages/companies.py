from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class CompaniesPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Company Intelligence")
        title.setObjectName("heading")

        subtitle = QLabel(
            "Research companies before applying."
        )
        subtitle.setObjectName("desc")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()