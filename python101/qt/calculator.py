from PyQt5.QtWidgets import QApplication, QWidget
import sys


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

    def interface(self):
        self.resize(400, 200)
        self.setWindowTitle("Simply calculator")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
