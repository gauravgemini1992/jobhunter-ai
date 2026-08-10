from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class JobsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Smart Job Match")
        title.setObjectName("heading")

        subtitle = QLabel(
            "Find AI-ranked jobs based on your resume."
        )
        subtitle.setObjectName("desc")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()