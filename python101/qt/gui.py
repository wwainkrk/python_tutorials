# from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QCheckBox, QButtonGroup
from shapes import Shape, Shapes


class UIWidget(object):
    """Class responsible for building User Interface"""

    def setup_ui(self, Widget):
        """

        :param Widget: UIWidget object for execute in main class
        """
        self.shape1 = Shape(self, Shapes.Polygon)            # hardcoded shapes to draw
        self.shape2 = Shape(self, Shapes.Ellipse)
        self.active_shape = self.shape1                      # setting for active shape/area to draw L/R

        systemv = QVBoxLayout()
        self.group_checkbtn = QButtonGroup()
        for i, n in enumerate(Shapes):
            name = str(n)
            name = name.replace("Shapes.", "")
            self.check_box = QCheckBox(name)              # from Shapes Enum classtype to str for CheckBox constructor
            # print(name, i)
            self.group_checkbtn.addButton(self.check_box, i)   # conversion from Shapes class to ButtonGroup method
            systemv.addWidget(self.check_box)

        # print(self.active_shape.shape.value)
        self.group_checkbtn.buttons()[self.active_shape.shape.value].setChecked(True)
        self.shape_check = QCheckBox("<=")                  # checkbox for pointing active shape
        self.shape_check.setChecked(True)
        systemv.addWidget(self.shape_check)

        # self.resize(150, 150)
        # print("setup_ui")
        systemh = QHBoxLayout()
        systemh.addWidget(self.shape1)
        systemh.addLayout(systemv)
        systemh.addWidget(self.shape2)

        self.setLayout(systemh)
        self.setFixedSize(systemh.sizeHint())
        self.setWindowTitle("Widgets App")


