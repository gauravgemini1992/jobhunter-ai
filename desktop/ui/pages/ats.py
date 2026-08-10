from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class ATSPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("ATS Intelligence")
        title.setObjectName("heading")

        subtitle = QLabel(
            "Analyze ATS compatibility and keyword matching."
        )
        subtitle.setObjectName("desc")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()