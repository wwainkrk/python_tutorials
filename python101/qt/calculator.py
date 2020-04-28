from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout
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

        # assign labels to the grid layout
        layout_tab = QGridLayout()
        layout_tab.addWidget(label1, 0, 0)
        layout_tab.addWidget(label2, 0, 1)
        layout_tab.addWidget(label3, 0, 2)

        # add lines to put some number
        number1_edit = QLineEdit()
        number2_edit = QLineEdit()
        result_edit = QLineEdit()

        # special settings for result edit line
        result_edit.setReadOnly(True)
        result_edit.setToolTip("Write <b>numbers</b> and select action")

        # assign edit labels to the grid layout
        layout_tab.addWidget(number1_edit, 1, 0)
        layout_tab.addWidget(number2_edit, 1, 1)
        layout_tab.addWidget(result_edit, 1, 2)

        # assign grid layout to window
        self.setLayout(layout_tab)

        # Create buttons for actions
        add_btn = QPushButton("&Add", self)
        sub_btn = QPushButton("&Substract", self)
        multi_btn = QPushButton("&Multiple", self)
        div_btn = QPushButton("&Divide", self)
        fin_btn = QPushButton("&Finish", self)
        fin_btn.resize(fin_btn.sizeHint())

        # Create all panel with buttons, horizontal system
        system_h = QHBoxLayout()
        system_h.addWidget(add_btn)
        system_h.addWidget(sub_btn)
        system_h.addWidget(multi_btn)
        system_h.addWidget(div_btn)

        # add finish button and panel with buttons to the main grid layout
        layout_tab.addLayout(system_h, 2, 0, 1, 3)
        layout_tab.addWidget(fin_btn, 3, 0, 1, 3)

        self.setGeometry(20, 20, 300, 100)
        self.setWindowIcon(QIcon("calculator.png"))
        self.setWindowTitle("Simply calculator")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
