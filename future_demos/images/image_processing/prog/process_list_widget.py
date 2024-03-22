# -*- coding: utf-8 -*-
"""*process_list_widget* file.

*process_list_widget* file that contains :

    * :class::ProcessListWidget

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""
from supoptools.pyqt6.widget_slider import WidgetSlider
from process_list import *
from process_item import ProcessItem

from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QCheckBox,
    QGridLayout, QVBoxLayout
)
from PyQt6.QtCore import Qt, pyqtSignal


class ProcessListWidget(QWidget):
    """Generate a widget to select a process to do on the initial image.

    :param main_layout: Main layout of the widget.
    :type main_layout: QVBoxLayout
    
    """

    clicked = pyqtSignal(str)
    checked = pyqtSignal(str)
    changed = pyqtSignal(str)

    def __init__(self) -> None:
        """Default constructor of the class.
        """
        super().__init__(parent=None)
        self.params_dict = {'init': True}

        # Main Layout
        self.main_layout = QVBoxLayout()

        # Graphical elements of the interface
        self.selected = None
        self.processes_dict = {}
        for i, (item_name, item_function) in enumerate(process_list.items()):
            self.processes_dict[item_name] = ProcessItem(item_name)
            self.processes_dict[item_name].checked.connect(self.check_options_list)
            self.processes_dict[item_name].clicked.connect(self.click_on_options_list)
            self.processes_dict[item_name].changed.connect(self.update_process)
            self.processes_dict[item_name].enable()
            self.main_layout.addWidget(self.processes_dict[item_name])

        self.setLayout(self.main_layout)

    def check_options_list(self, event) -> None:
        """Action performed when a process is checked
        """
        is_checked = False
        if self.processes_dict[event].check_item.isChecked():
            is_checked = True
        self.uncheck_all()
        if is_checked:
            self.processes_dict[event].check_item.setChecked(True)
            self.processes_dict[event].enable()
        self.checked.emit(event)

    def click_on_options_list(self, event) -> None:
        """Action performed when an "Options" button is clicked.
        """
        self.clicked.emit(event)

    def update_process(self, event):
        """Action performed when an option of a parameter changed.
        """
        self.changed.emit(event)


    def uncheck_all(self) -> None:
        """Uncheck all the checkbox.
        """
        for i, (item_name, item_function) in enumerate(process_list.items()):
            self.processes_dict[item_name].check_item.setChecked(False)
            self.processes_dict[item_name].enable()

    def enable(self):
        """Set enabled the process list."""
        for i, (item_name, item_function) in enumerate(process_list.items()):
            self.processes_dict[item_name].enable()

    def disable(self):
        """Set disabled the process list."""
        for i, (item_name, item_function) in enumerate(process_list.items()):
            self.processes_dict[item_name].disable()


if __name__ == "__main__":
    def action_checked(event):
        print(f'Checked {event}')

    def action_clicked(event):
        print(f'Clicked {event}')

    def action_changed(event):
        print(f'Changed {event}')

    import sys
    from PyQt6.QtWidgets import (QApplication, QMainWindow)

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("Source_Widget test")
    main_window.setGeometry(500, 100, 400, 600)
    central_widget = ProcessListWidget()
    main_window.setCentralWidget(central_widget)

    central_widget.clicked.connect(action_clicked)
    central_widget.checked.connect(action_checked)
    central_widget.changed.connect(action_changed)

    main_window.show()
    sys.exit(app.exec())
