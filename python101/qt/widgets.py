from __future__ import unicode_literals             # Polish characters
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QColor
from gui import UIWidget


class Widgets(QWidget, UIWidget):
    """Main class for application"""

    def __init__(self, parent=None):
        super(Widgets, self).__init__(parent)
        self.setup_ui(self)                     # create user interface

        # Signals & slots
        self.group_checkbtn.buttonClicked[int].connect(self.set_shape)
        self.shape_check.clicked.connect(self.activate_shape)

        # Channel and color variables
        self.channel = {'R'}
        self.colorI = QColor(0, 0, 0)

        # Signal/slots mechanism for changing values in LCD and RadioButton group
        for i in range(self.radio_layout.count()):
            self.radio_layout.itemAt(i).widget().toggled.connect(self.set_channel_radiobtn) # toggled = changed
        self.slider.valueChanged.connect(self.change_color)                                  # slider changes

    def set_channel_radiobtn(self, value):
        """
        Reset channels with color and put selected one
        """
        self.channel = set()
        if value:
            self.channel.add(self.sender().text())

    def change_color(self, value):
        """
        Displaying current value on lcd, and take value from slider to setting color method
        """
        self.lcd.display(value)
        if 'R' in self.channel:
            self.colorI.setRed(value)
        elif 'G' in self.channel:
            self.colorI.setGreen(value)
        elif 'B' in self.channel:
            self.colorI.setBlue(value)

        self.active_shape.set_colorI(
            self.colorI.red(),
            self.colorI.green(),
            self.colorI.blue()
        )

    def set_shape(self, value):
        # print("set_shape")
        self.active_shape.setShape(value)

    def activate_shape(self, value):
        # print("activate_shape")
        if value:
            self.active_shape = self.shape1                     # shape on the left side
            self.sender().setText("<=")
        else:
            self.active_shape = self.shape2                     # shape on the right side
            self.sender().setText("=>")

        self.group_checkbtn.buttons()[self.active_shape.shape.value].setChecked(True)   # setter for correct checkbox


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Widgets()
    window.show()
    try:
        sys.exit(app.exec_())
    except Exception:
        print("Exception")
