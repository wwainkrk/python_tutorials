from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QIcon
import sys
# from __future__ import unicode_literals             # Polish characters


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()                        # methods for window displaying

    def interface(self):
        # labels
        label1 = QLabel("Number 1:", self)
        label2 = QLabel("Number 2:", self)
        label3 = QLabel("Result:", self)

        # assign labels to grid layout
        layout_tab = QGridLayout()
        layout_tab.addWidget(label1, 0, 0)
        layout_tab.addWidget(label2, 0, 1)
        layout_tab.addWidget(label3, 0, 2)

        # assign grid layout to window
        self.setLayout(layout_tab)

        self.setGeometry(20, 20, 400, 200)
        self.setWindowIcon(QIcon("calculator.png"))
        self.setWindowTitle("Simply calculator")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
