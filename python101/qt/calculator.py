from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
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
        self.number1_edit = QLineEdit()
        self.number2_edit = QLineEdit()
        self.result_edit = QLineEdit()

        # special settings for result edit line
        self.result_edit.setReadOnly(True)
        self.result_edit.setToolTip("Write <b>numbers</b> and select action")

        # assign edit labels to the grid layout
        layout_tab.addWidget(self.number1_edit, 1, 0)
        layout_tab.addWidget(self.number2_edit, 1, 1)
        layout_tab.addWidget(self.result_edit, 1, 2)

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

        # Connect function with button
        fin_btn.clicked.connect(self.close)

        add_btn.clicked.connect(self.operation)
        sub_btn.clicked.connect(self.operation)
        multi_btn.clicked.connect(self.operation)
        div_btn.clicked.connect(self.operation)

#    def finish(self):
#        self.close()

    def closeEvent(self, event):
        """
        Create additional window to confirm close app
        """
        odp = QMessageBox.question(
            self,
            "Confirmation",
            "Are you sure to close app?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # Handling ESC key press
    def key_press_event(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def operation(self):
        """
        Funtion for making mathematical operation
        """

        try:
            sender = self.sender()

            number1 = float(self.number1_edit.text())
            number2 = float(self.number2_edit.text())
            result = ""
            print(sender.objectName())

            if sender.text() == "&Add":
                result = number1 + number2
            elif sender.text() == "&Substract":
                result = number1 - number2
            elif sender.text() == "&Multiple":
                result = number1 * number2
            elif sender.text() == "&Divide":
                try:
                    result = round(number1 / number2, 9)
                except ZeroDivisionError:
                    QMessageBox.critical(self, "Error !", "You cannot divide by zero !")

            self.result_edit.setText(str(result))

        except ValueError:
            QMessageBox.warning(self, "Error", "Wrong data", QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
