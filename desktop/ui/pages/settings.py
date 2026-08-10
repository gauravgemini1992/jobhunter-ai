from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class SettingsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Settings")
        title.setObjectName("heading")

        subtitle = QLabel(
            "Configure JobHunter AI preferences."
        )
        subtitle.setObjectName("desc")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()