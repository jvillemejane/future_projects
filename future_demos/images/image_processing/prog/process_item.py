# -*- coding: utf-8 -*-
"""*process_item* file.

*process_item* file that contains :class::ProcessItem class that generates
an item of a :class::ProcessListWidget object

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""
from supoptools.pyqt6.widget_slider import WidgetSlider
from process_list import *
from process_options import ProcessOptions

from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QCheckBox,
    QGridLayout, QVBoxLayout
)
from PyQt6.QtCore import pyqtSignal


class ProcessItem(QWidget):
    """Generate an item of image process.

    :param main_layout: Main layout of the widget.
    :type main_layout: QGridLayout

    """

    clicked = pyqtSignal(str)
    checked = pyqtSignal(str)
    changed = pyqtSignal(str)

    def __init__(self, name='') -> None:
        """Default constructor of the class.

        :param name: Name of the item.
        :type name: str

        """
        super().__init__(parent=None)
        self.params_window = None
        self.name_label = QLabel(name)
        self.check_item = QCheckBox()
        self.check_item.clicked.connect(self.check_options)
        self.params_item = QPushButton('Options')
        self.params_item.clicked.connect(self.click_on_options)

        # Graphical elements of the interface
        self.main_layout = QGridLayout()

        self.main_layout.addWidget(self.check_item, 0, 0)
        self.main_layout.addWidget(self.name_label, 0, 1)
        self.main_layout.addWidget(self.params_item, 0, 2)
        try:
            self.disable()
        except Exception as e:
            print(e)
        self.setLayout(self.main_layout)

    def check_options(self, event) -> None:
        """Action performed when a process is checked
        """
        if self.check_item.isChecked():
            self.params_item.setEnabled(True)
        else:
            self.params_item.setEnabled(False)
        self.checked.emit(self.name_label.text())

    def click_on_options(self, event) -> None:
        """Action performed when 'Options' button is clicked.
        """
        try:
            if self.check_item.isChecked():
                pass
                self.params_window = ProcessOptions(self.name_label.text())
                self.params_window.changed.connect(self.action_changed_params)
                self.params_window.show()
            self.clicked.emit(self.name_label.text())
        except Exception as e:
            print("Exception - click_on_options: " + str(e) + "")

    def action_changed_params(self, event):
        """Action performed when an option parameter is changed.
        """
        self.changed.emit(event)

    def enable(self):
        """Set enabled the interactive objects.
        """
        self.check_item.setEnabled(True)
        if self.check_item.isChecked():
            self.params_item.setEnabled(True)
        else:
            self.params_item.setEnabled(False)

    def disable(self):
        """Set disabled the interactive objects.
        """
        self.check_item.setEnabled(False)
        self.params_item.setEnabled(False)


if __name__ == "__main__":
    def action_checked(event):
        print(f'Checked {event}')

    def action_clicked(event):
        print(f'Clicked {event}')
        if event == "binarize":
            dict = {"threshold": 28}
            central_widget.params_window.set_values(dict)

    def action_changed(event):
        print(f'Changed {event}')

    import sys
    from PyQt6.QtWidgets import (QApplication, QMainWindow)

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("Source_Widget test")
    main_window.setGeometry(500, 100, 400, 600)
    central_widget = ProcessItem(name="binarize")
    main_window.setCentralWidget(central_widget)

    central_widget.checked.connect(action_checked)
    central_widget.clicked.connect(action_clicked)
    central_widget.changed.connect(action_changed)
    central_widget.enable()

    main_window.show()
    sys.exit(app.exec())