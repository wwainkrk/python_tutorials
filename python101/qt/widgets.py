from __future__ import unicode_literals             # Polish characters
from PyQt5.QtWidgets import QApplication, QWidget
from gui import UIWidget


class Widgets(QWidget, UIWidget):
    """Main class for application"""

    def __init__(self, parent=None):
        super(Widgets, self).__init__(parent)
        self.setup_UI(self)                     # create user interface


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Widgets()
    window.show()


    sys.exit(app.exec_())
