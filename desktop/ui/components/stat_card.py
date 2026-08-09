from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout


class StatCard(QFrame):

    def __init__(self, title: str, value: str, status: str):
        super().__init__()

        self.setFixedSize(250, 150)
        self.setObjectName("StatCard")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)

        title_label = QLabel(title)
        title_label.setObjectName("CardTitle")

        value_label = QLabel(value)
        value_label.setAlignment(Qt.AlignCenter)
        value_label.setObjectName("CardValue")

        status_label = QLabel(status)
        status_label.setAlignment(Qt.AlignCenter)
        status_label.setObjectName("CardStatus")

        layout.addWidget(title_label)
        layout.addStretch()
        layout.addWidget(value_label)
        layout.addWidget(status_label)

        self.setStyleSheet("""
            QFrame#StatCard {
                background: #1E293B;
                border: 1px solid #334155;
                border-radius: 18px;
            }

            QLabel#CardTitle {
                color: #CBD5E1;
                font-size: 14px;
            }

            QLabel#CardValue {
                color: white;
                font-size: 36px;
                font-weight: bold;
            }

            QLabel#CardStatus {
                color: #22C55E;
                font-size: 13px;
            }
        """)