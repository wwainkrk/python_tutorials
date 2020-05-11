from __future__ import unicode_literals             # Polish characters
from enum import Enum


class UIWidget(object):
    """Class responsible for building User Interface"""

    def setup_UI(self, Widget):
        print("setup_UI")


class Shapes(Enum):
    Rect = 0
    Ellipse = 1
    Polygon = 2
    Line = 3
