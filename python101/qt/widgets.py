from __future__ import unicode_literals             # Polish characters
from PyQt5.QtWidgets import QApplication, QWidget
from gui import UIWidget


class Widgets(QWidget, UIWidget):
    """Main class for application"""

    def __init__(self, parent=None):
        super(Widgets, self).__init__(parent)
        self.setup_ui(self)                     # create user interface

        self.group_checkbtn.buttonClicked[int].connect(self.set_shape)
        self.shape_check.clicked.connect(self.activate_shape)

    def set_shape(self, value):
        # print("set_shape")
        self.active_shape.setShape(value)

    def activate_shape(self, value):
        # print("activate_shape")
        if value:
            self.active_shape = self.shape1
            self.sender().setText("<=")
        else:
            self.active_shape = self.shape2
            self.sender().setText("=>")

        self.group_checkbtn.buttons()[self.active_shape.shape.value].setChecked(True)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Widgets()
    window.show()
    try:
        sys.exit(app.exec_())
    except Exception:
        print("Exception")
