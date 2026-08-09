import sys

from PySide6.QtWidgets import QApplication

from desktop.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("JobHunter AI")
    app.setApplicationVersion("2.0")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()