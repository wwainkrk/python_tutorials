from enum import Enum
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRect


class UIWidget(object):
    """Class responsible for building User Interface"""

    def setup_ui(self, Widget):
        """

        :param Widget: UIWidget object for execute in main class
        """
        self.shape = Shapes.Ellipse             # hardcoded shape to draw
        self.rect = QRect(1, 1, 101, 101)

        self.colorP = QColor(0, 0, 0)
        self.colorB = QColor(200, 30, 40)

        #self.resize(150, 150)
        #print("setup_ui")
        self.setWindowTitle("Widgets App")

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        #print("paintEvent")
        self.draw_figures(e, qp)                # function to build shape in Painter
        qp.end()

    def draw_figures(self, e, qp):
        # print("drawFigures")

        #print("draw_figures")
        qp.setPen(self.colorP)
        qp.setBrush(self.colorB)
        qp.setRenderHint(QPainter.Antialiasing)

        if self.shape == Shapes.Rect:
            qp.drawRect(self.rect)              # the same argument as in drawEllipse, for surface
        elif self.shape == Shapes.Ellipse:
            qp.drawEllipse(self.rect)


class Shapes(Enum):
    # Rect, Ellipse, Polygon, Line = range(4)    # similar way to simulate enum type
    Rect = 0
    Ellipse = 1
    Polygon = 2
    Line = 3
