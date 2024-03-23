# -*- coding: utf-8 -*-
"""*widget_inc_dec_step* file.

*widget_inc_dec_step* file that contains :class::WidgetIncDec

.. module:: WidgetIncDecStep
   :synopsis: class to display an incremental system in PyQt6, with a fixed step.

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""

import sys
import numpy

# Third pary imports
from PyQt6.QtWidgets import QMainWindow, QWidget, QLineEdit
from PyQt6.QtWidgets import (QGridLayout, QVBoxLayout,
                             QLabel, QPushButton, QMessageBox, QComboBox)
from PyQt6.QtGui import QCursor

from PyQt6.QtCore import Qt, pyqtSignal


class WidgetIncDecStep(QWidget):
    """
    IncDecWidget class to create a widget with two buttons to increase and decrease
    a value. The incremental step is fixed. Children of QWidget.

    """

    increased = pyqtSignal(str)
    decreased = pyqtSignal(str)

    def __init__(self, name="", integer: bool = False,
                 inc: float = 1.0) -> None:
        """Default constructor of the class.

        :param name: Name of the increment. Default to "".
        :type name: str, optional
        :param integer: Specify if the increment is an integer, defaults to False.
        :type integer: bool, optional
        :param inc: Increment value. Default to 0.
        :type inc: float, optional

        """
        super().__init__()

        ''' Global Values '''
        self.name = name
        self.real_value = 0.0
        self.enabled = True
        self.integer = integer
        if self.integer:
            self.ratio_gain = int(inc)
        else:
            self.ratio_gain = inc
        ''' Layout Manager '''
        self.main_layout = QGridLayout()
        ''' Graphical Objects '''
        self.name_label = QLabel(name)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.user_value = QLineEdit()
        self.user_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.user_value.returnPressed.connect(self.new_value_action)
        self.limits = None

        self.units = ''
        self.units_label = QLabel('')
        self.units_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.inc_button = QPushButton('+ ' + str(self.ratio_gain))
        self.inc_button.clicked.connect(self.increase_value)
        self.inc_button.setStyleSheet("background:#F3A13C; color:white; font-size:14px; font-weight:bold;")
        self.dec_button = QPushButton('- ' + str(self.ratio_gain))
        self.dec_button.clicked.connect(self.decrease_value)
        self.dec_button.setStyleSheet("background:#3EE4FD;font-size:14px; font-weight:bold;")

        self.main_layout.setColumnStretch(0, 2)  # Dec button
        self.main_layout.setColumnStretch(1, 4)  # Name
        self.main_layout.setColumnStretch(2, 1)  # Value
        self.main_layout.setColumnStretch(3, 2)  # Units

        ''' Adding GO into the widget layout '''
        self.main_layout.addWidget(self.dec_button, 1, 0)
        self.main_layout.addWidget(self.name_label, 0, 0, 1, 4)  # Position 1,0 / 3 cells
        self.main_layout.addWidget(self.user_value, 1, 1)  # Position 1,1 / 3 cells
        self.main_layout.addWidget(self.units_label, 1, 2)
        self.main_layout.addWidget(self.inc_button, 1, 3)
        self.setLayout(self.main_layout)
        self.update_display()

    def increase_value(self):
        if self.limits is not None:
            if self.real_value + self.ratio_gain <= self.limits[1]:
                self.real_value += self.ratio_gain
        else:
            self.real_value += self.ratio_gain
        self.update_display()
        self.increased.emit(self.name)

    def decrease_value(self):
        if self.limits is not None:
            if self.real_value - self.ratio_gain >= self.limits[0]:
                self.real_value -= self.ratio_gain
        else:
            self.real_value -= self.ratio_gain
        self.update_display()
        self.decreased.emit(self.name)

    def new_value_action(self):
        value = self.user_value.text()
        if value.isnumeric():
            if self.integer:
                self.real_value = float(value)
            else:
                self.real_value = int(value)
            self.update_display()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name.setText(name)

    def set_enabled(self, value):
        self.enabled = value
        self.inc_button.setEnabled(value)
        self.dec_button.setEnabled(value)
        self.user_value.setEnabled(value)

    def value_changed(self, event):
        value = self.user_value.text()
        value2 = value.replace('.', '', 1)
        value2 = value2.replace('e', '', 1)
        value2 = value2.replace('-', '', 1)
        if value2.isdigit():
            self.real_value = float(value)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText(f"Not a number")
            msg.setWindowTitle("Not a Number Value")
            msg.exec()
            self.real_value = 0
            self.user_value.setText(str(self.real_value))
        self.update_display()

    def set_units(self, units):
        self.units = units
        self.update_display()

    def update_display(self):
        try:
            if self.integer:
                self.real_value = int(self.real_value)
            negative_nb = False
            if self.real_value < 0:
                negative_nb = True
                self.real_value = -self.real_value
            if self.real_value / 1000.0 >= 1:
                display_value = self.real_value / 1000.0
                display_units = 'k' + self.units
            elif self.real_value / 1e6 >= 1:
                display_value = self.real_value / 1e6
                display_units = 'M' + self.units
            else:
                display_value = self.real_value
                display_units = self.units
            self.units_label.setText(f'{display_units}')
            if negative_nb:
                display_value = -display_value
                self.real_value = -self.real_value
            display_value = numpy.round(display_value, 3)
            self.user_value.setText(f'{display_value}')
        except Exception as e:
            print("Exception - update_display: " + str(e) + "")

    def get_real_value(self):
        if self.integer:
            return int(self.slider.value() / self.ratio_slider)
        else:
            return self.slider.value() / self.ratio_slider

    def set_value(self, value):
        self.real_value = value
        self.update_display()

    def set_gain(self, value):
        self.ratio_gain = value
        self.update_display()

    def clear_value(self):
        self.real_value = 0
        self.gain_changed()
        self.update_display()
        self.updated.emit('rst')

    def wheelEvent(self, event):
        if self.enabled:
            mouse_point = QCursor().pos()
            # print(f'Xm={mouse_point.x()} / Ym={mouse_point.y()}')
            num_degrees = event.angleDelta() / 8 / 15
            if num_degrees.y() > 0:
                self.increase_value()
            elif num_degrees.y() < 0:
                self.decrease_value()

    def set_limits(self, limits):
        """
        Sets the limits of the value of the widget

        :param limits: Limits for the value of the increment.
        :type limits: tuple[float, float]

        """
        try:
            self.limits = limits
        except Exception as e:
            print("Exception - set_limits: " + str(e) + "")

if __name__ == '__main__':
    from PyQt6.QtWidgets import QApplication


    class MyWindow(QMainWindow):
        def __init__(self):
            super().__init__()

            self.setWindowTitle("Widget Slider test")
            self.setGeometry(300, 300, 200, 100)

            self.centralWid = QWidget()
            self.layout = QVBoxLayout()

            self.incdec_widget = WidgetIncDecStep(name='Test', integer=True, inc=2)
            self.incdec_widget.set_limits((1, 25))
            self.incdec_widget.set_value(1)
            self.layout.addWidget(self.incdec_widget)

            self.centralWid.setLayout(self.layout)
            self.setCentralWidget(self.centralWid)


    app = QApplication(sys.argv)
    main = MyWindow()
    main.show()
    sys.exit(app.exec())
