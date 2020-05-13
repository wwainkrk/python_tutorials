from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtCore import QPoint, QRect, QSize
from enum import Enum


class Shapes(Enum):
    # Rect, Ellipse, Polygon, Line = range(4)    # similar way to simulate enum type
    Rect = 0
    Ellipse = 1
    Polygon = 2
    Line = 3


class Shape(QWidget):
    """Class where we can define which widget we want to draw"""
    rect = QRect(1, 1, 101, 101)
    points = QPolygon([
            QPoint(1, 101),  # begin point (x, y)
            QPoint(51, 1),
            QPoint(101, 101)
    ])

    def __init__(self, parent, shape=Shapes.Rect):
        super(Shape, self).__init__(parent)
        # print("init Shape")
        self.shape = shape                          # shape which will be draw

        # colors of pen which will be inside surface
        self.colorP = QColor(0, 0, 0)
        self.colorB = QColor(255, 255, 255)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        # print("paintEvent")
        self.draw_figures(e, qp)                # function to build shape in Painter
        qp.end()

    def draw_figures(self, e, qp):
        # print("draw_figures")
        qp.setPen(self.colorP)
        qp.setBrush(self.colorB)
        qp.setRenderHint(QPainter.Antialiasing) # more 'smoother' shapes

        if self.shape == Shapes.Rect:
            qp.drawRect(self.rect)              # the same argument as in drawEllipse, for surface
        elif self.shape == Shapes.Ellipse:
            qp.drawEllipse(self.rect)
        elif self.shape == Shapes.Polygon:
            qp.drawPolygon(self.points)
        elif self.shape == Shapes.Line:
            qp.drawLine(self.rect.topLeft(), self.rect.bottomRight())
        else:
            qp.drawRect(self.rect)

    def sizeHint(self):
        return QSize(102, 102)

    def minSizeHint(self):
        return QSize(102, 102)

    def set_shape(self, shape):
        self.shape = shape
        self.update()

    def set_colorB(self, r=0, g=0, b=0):
        self.colorB = QColor(r, g, b)       # arguments provided as RGB
        self.update()
