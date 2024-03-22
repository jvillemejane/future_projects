# -*- coding: utf-8 -*-
"""*process_list_widget* file.

*process_list_widget* file that contains :

    * :class::ProcessListWidget

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""
from supoptools.pyqt6.widget_slider import WidgetSlider
from process_list import *

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
            self.processes_dict[item_name].changed.connect(self.action_checked)
            self.processes_dict[item_name].check_item.setEnabled(False)
            self.processes_dict[item_name].params_item.setEnabled(False)
            self.main_layout.addWidget(self.processes_dict[item_name])

        self.setLayout(self.main_layout)

    def action_checked(self, event) -> None:
        """Action performed when a process is checked
        """
        self.changed.emit(event)

    def enable(self) -> None:
        """Activate all the checkbox and button of the interface
        """
        for i, (item_name, item_function) in enumerate(process_list.items()):
            self.processes_dict[item_name].check_item.setEnabled(True)
            self.processes_dict[item_name].params_item.setEnabled(True)

    def disable(self) -> None:
        """Unactivate all the checkbox and button of the interface
        """
        for i, (item_name, item_function) in enumerate(process_list.items()):
            self.processes_dict[item_name].check_item.setEnabled(False)
            self.processes_dict[item_name].params_item.setEnabled(False)

    def uncheck_all(self) -> None:
        """Uncheck all the checkbox.
        """
        for i, (item_name, item_function) in enumerate(process_list.items()):
            self.processes_dict[item_name].check_item.setChecked(False)


class ProcessItem(QWidget):
    """Generate an item of image process.
    
    :param main_layout: Main layout of the widget.
    :type main_layout: QVBoxLayout
    
    """

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
        self.check_item.clicked.connect(self.action_checked)
        self.params_item = QPushButton('Options')
        self.params_item.clicked.connect(self.action_params)
        self.actual_values = {}

        # Graphical elements of the interface
        self.main_layout = QGridLayout()

        self.main_layout.addWidget(self.check_item, 0, 0)
        self.main_layout.addWidget(self.name_label, 0, 1)
        self.main_layout.addWidget(self.params_item, 0, 2)

        self.setLayout(self.main_layout)

    def set_values(self, dict_values: dict) -> None:
        """Set the values of the parameters

        :param dict_values: Dictionary with all the parameters.
        :type dict_values: dict

        """
        self.actual_values = dict_values

    def action_checked(self, event) -> None:
        """
        Action performed when a process is checked
        """
        print('Update Init Value')
        self.changed.emit(self.name_label.text())

    def action_params(self, event) -> None:
        if self.check_item.isChecked():
            self.params_window = ProcessParams(self.name_label.text())
            self.params_window.set_values(self.actual_values)
            self.params_window.show()


class ProcessParams(QWidget):
    """ProcessParams class, children of QWidget.
    
    Class to display and to change the available parameters of a process.
    
    """

    changed = pyqtSignal(str)

    def __init__(self, name: str = ''):
        """Default constructor of the class.
        
        :param name: Name of the process.
        :type name: str
        
        """
        super().__init__(parent=None)
        # Main layout
        self.main_layout = QVBoxLayout()
        # Graphical objects
        self.name_label = QLabel('Parameters of ' + name)
        self.main_layout.addWidget(self.name_label)
        self.elem = {}
        self.actual_values = {}
        try:
            # Create all the subitem from list of params
            all_options = process_list[name]['params']
            for id, option in enumerate(all_options.split(';')):
                option_items = process_list[name][option]
                item = option_items.split(':')
                if item[0] == 'int':
                    self.elem[option] = WidgetSlider(name=option, integer=True, signal_name=option)
                    self.elem[option].set_min_max_slider(float(item[1]), float(item[2]))
                    self.elem[option].slider_changed_signal.connect(self.action_param_changed)
                    self.main_layout.addWidget(self.elem[option])
        except Exception as e:
            print("Exception - params_init: " + str(e) + "")

        self.setFixedSize(300, 400)
        self.setLayout(self.main_layout)

    def set_values(self, dict_values: dict) -> None:
        """Set the values of the parameters

        :param dict_values: Dictionary with all the parameters.
        :type dict_values: dict

        """
        self.actual_values = dict_values

    def action_param_changed(self, event):
        print(f'PROCESS_LIST / ProcessParams {event}')
        param_event = event.split(':')[-1]
        self.actual_values[param_event] = self.elem[param_event].get_real_value()
        print(f'REAL = {self.actual_values[param_event]}')
        self.changed.emit(event)

if __name__ == "__main__":
    def action_loaded(event):
        print(event)


    import sys
    from PyQt6.QtWidgets import (QApplication, QMainWindow)

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("Source_Widget test")
    main_window.setGeometry(500, 100, 400, 600)
    central_widget = ProcessListWidget()
    main_window.setCentralWidget(central_widget)

    central_widget.changed.connect(action_loaded)
    central_widget.enable()

    main_window.show()
    sys.exit(app.exec())
