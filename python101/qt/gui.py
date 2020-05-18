from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QCheckBox, QButtonGroup
from PyQt5.QtWidgets import QSlider, QLCDNumber, QSplitter
from PyQt5.QtWidgets import QRadioButton, QGroupBox
from PyQt5.QtWidgets import QComboBox, QSpinBox
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
        # Horizontal layout with shapes and CheckBox group
        systemh_1 = QHBoxLayout()
        systemh_1.addWidget(self.shape1)
        systemh_1.addLayout(systemv)
        systemh_1.addWidget(self.shape2)

        # QSlider and QLCDNumber together in QSPlitter in horizontal layout
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)

        self.lcd = QLCDNumber()
        self.lcd.setSegmentStyle(QLCDNumber.Flat)

        systemh_2 = QSplitter(Qt.Horizontal)
        systemh_2.addWidget(self.slider)
        systemh_2.addWidget(self.lcd)
        systemh_2.setSizes((125, 75))

        # QRadioButtion group
        self.group_radiobtn = QGroupBox('RGB Options')                   # Groupbox as separated part with checkbox and radiobuttons
        self.radio_layout = QHBoxLayout()
        for v in ('R', 'G', 'B'):
            radio_btn = QRadioButton(v)
            self.radio_layout.addWidget(radio_btn)
        self.group_radiobtn.setObjectName('Radio')
        self.group_radiobtn.setLayout(self.radio_layout)
        self.group_radiobtn.setCheckable(True)

        systemh_3 = QHBoxLayout()
        systemh_3.addWidget(self.group_radiobtn)

        # ComboBox list and SpinBox for color channel value
        self.combolist_rgb = QComboBox(self)
        for v in ('R', 'G', 'B'):
            self.combolist_rgb.addItem(v)
        self.combolist_rgb.setEnabled(False)
        self.spinvalue = QSpinBox(self)
        self.spinvalue.setMinimum(0)
        self.spinvalue.setMaximum(255)
        self.spinvalue.setEnabled(False)

        # VBox for Combo%Spin widgets
        combo_vlayout = QVBoxLayout()
        combo_vlayout.addWidget(self.combolist_rgb)
        combo_vlayout.addWidget(self.spinvalue)

        # Add new layout to existing
        systemh_3.insertSpacing(1, 25)                  # splitting two layouts
        systemh_3.addLayout(combo_vlayout)

        # Main window layout with all parts
        window_layout = QVBoxLayout()
        window_layout.addLayout(systemh_1)
        window_layout.addWidget(systemh_2)
        window_layout.addLayout(systemh_3)

        self.setLayout(window_layout)
        self.setFixedSize(window_layout.sizeHint())               # automatically window size
        self.setWindowTitle("Widgets App")


