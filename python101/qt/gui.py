# from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QHBoxLayout
from shapes import Shape, Shapes


class UIWidget(object):
    """Class responsible for building User Interface"""

    def setup_ui(self, Widget):
        """

        :param Widget: UIWidget object for execute in main class
        """
        self.shape = Shape(self, Shapes.Polygon)            # hardcoded shape to draw

        self.resize(150, 150)
        print("setup_ui")
        systemh = QHBoxLayout()
        systemh.addWidget(self.shape)

        self.setLayout(systemh)
        self.setWindowTitle("Widgets App")


