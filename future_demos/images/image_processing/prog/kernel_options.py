# -*- coding: utf-8 -*-
"""*kernel_options* file.

*kernel_options* file that contains :class::KernelOptions class that generates
a window to set the options of a kernel.

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""

from process_list import *

from PyQt6.QtWidgets import (
    QWidget, QLabel,
    QVBoxLayout
)
from PyQt6.QtCore import Qt, pyqtSignal
from supoptools.pyqt6.widget_inc_dec_step import WidgetIncDecStep


class KernelOptions(QWidget):
    """KernelOptions class, children of QWidget.

    Class to display and to change the available parameters of a kernel.

    """

    changed = pyqtSignal(str)

    def __init__(self, name: str = '') -> None:
        """Default constructor of the class.

        :param name: Name of the kernel.
        :type name: str

        """
        super().__init__(parent=None)
        # Main layout
        self.main_layout = QVBoxLayout()
        # Object information
        self.name = name
        # Graphical objects
        self.name_label = QLabel('Kernel Parameters of ' + self.name)
        self.name_label.setStyleSheet("color: darkblue; font-size: 15px;")
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.name_label)
        self.elem = {}
        try:
            # Create all the subitem from list of params
            all_options = get_options_ker(name)
            print(f'ALL options : {all_options}')
            for id, option in enumerate(all_options):
                if option == 'ker':
                    print('Kernel')
                    # TO DO LATER !
                else:
                    kernel_options = get_options_ker_param(name, option)
                    print(f'Option Type = {kernel_options}')

                    if kernel_options[0] == 'odd':  # odd number
                        self.elem[option] = WidgetIncDecStep(option, integer=True,
                                                             inc=2.0)
                        min_v = int(kernel_options[1])
                        max_v = int(kernel_options[2])
                        self.elem[option].set_limits((min_v, max_v))
                        inc_v = int(kernel_options[3])
                        self.elem[option].set_value(inc_v)
                        self.elem[option].increased.connect(self.elem_updated)
                        self.elem[option].decreased.connect(self.elem_updated)
                        self.main_layout.addWidget(self.elem[option])
                '''
                if option_type == 'int':
                    option_vals = get_options_int(name, option)
                    self.elem[option] = WidgetSlider(name=option, integer=True, signal_name=option)
                    self.elem[option].set_min_max_slider(float(option_vals[0]), float(option_vals[1]))
                    self.elem[option].slider_changed_signal.connect(self.update_options)
                    self.main_layout.addWidget(self.elem[option])
                elif option_type == 'ker':
                    print('KERNEL')
                    self.elem[option] = QLabel(option)
                    self.main_layout.addWidget(self.elem[option])
                elif option_type == 'odd':
                    print('ODD')
                    self.elem[option] = QLabel(option)
                    self.main_layout.addWidget(self.elem[option])
                '''
        except Exception as e:
            print("Exception - params_init: " + str(e) + "")

        self.setFixedSize(300, 400)
        self.setLayout(self.main_layout)

    def update_options(self, event):
        try:
            param_event = event.split(':')[-1]
            self.changed.emit(self.name+':'+event)
        except Exception as e:
            print("Exception - update_options: " + str(e) + "")

    def set_values(self, dict_values) -> None:
        """Update displayed values.
        """
        try:
            # Create all the subitem from list of params
            all_options = get_process_options(self.name)
            for id, option in enumerate(all_options.split(';')):
                option_type = get_options_type(self.name, option)
                if option_type == 'int':
                    self.elem[option].set_value(dict_values[option])
        except Exception as e:
            print("Exception - set_values: " + str(e) + "")

    def get_values(self) -> dict:
        """Get the values of the process parameters.
        """
        try:
            result_dict = {}
            # Create all the subitem from list of params
            all_options = get_process_options(self.name)
            for id, option in enumerate(all_options.split(';')):
                option_type = get_options_type(self.name, option)
                if option_type == 'int':
                    result_dict[option] = self.elem[option].get_real_value()
            return result_dict
        except Exception as e:
            print("Exception - set_values: " + str(e) + "")

    def elem_updated(self, event):
        """Action performed when a param is updated."""
        new_value = self.elem[event].get_real_value()
        print(f'elem_updated {event} / New Value = {new_value}')


if __name__ == "__main__":
    def action_changed(event):
        print(f'Changed {event}')

    import sys
    from PyQt6.QtWidgets import (QApplication, QMainWindow)

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("Source_Widget test")
    main_window.setGeometry(500, 100, 400, 600)
    central_widget = KernelOptions(name="blur")
    dict = {"threshold": 100}
    central_widget.set_values(dict)
    main_window.setCentralWidget(central_widget)

    central_widget.changed.connect(action_changed)

    main_window.show()
    sys.exit(app.exec())
