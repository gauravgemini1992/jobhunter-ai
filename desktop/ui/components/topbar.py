from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QLabel,
    QPushButton
)


class TopBar(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedHeight(75)

        layout = QHBoxLayout(self)

        layout.setContentsMargins(25, 15, 25, 15)

        search = QLineEdit()

        search.setPlaceholderText("Search jobs, companies or skills...")

        search.setFixedHeight(42)

        search.setMinimumWidth(420)

        search.setObjectName("search")

        layout.addWidget(search)

        layout.addStretch()

        notification = QPushButton("🔔")
        theme = QPushButton("🌙")
        profile = QPushButton("👤  Gaurav")

        for button in [notification, theme, profile]:

            button.setCursor(Qt.PointingHandCursor)

            button.setFixedHeight(42)

            layout.addWidget(button)

        self.setStyleSheet("""

        QWidget{

            background:#0F172A;

        }

        QLineEdit{

            background:#1E293B;

            border:1px solid #334155;

            border-radius:12px;

            padding-left:15px;

            color:white;

            font-size:14px;

        }

        QPushButton{

            background:#1E293B;

            border:1px solid #334155;

            border-radius:12px;

            padding:10px 18px;

            color:white;

        }

        QPushButton:hover{

            background:#2563EB;

        }

        """)