# -*- coding: utf-8 -*-
"""*process_options* file.

*process_options* file that contains :class::ProcessOptions class that generates
a window to set the options of a process.

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""

from supoptools.pyqt6.widget_slider import WidgetSlider
from process_list import *

from PyQt6.QtWidgets import (
    QWidget, QLabel,
    QVBoxLayout
)
from PyQt6.QtCore import Qt, pyqtSignal


class ProcessOptions(QWidget):
    """ProcessOptions class, children of QWidget.

    Class to display and to change the available parameters of a process.

    """

    changed = pyqtSignal(str)

    def __init__(self, name: str = '') -> None:
        """Default constructor of the class.

        :param name: Name of the process.
        :type name: str

        """
        super().__init__(parent=None)
        # Main layout
        self.main_layout = QVBoxLayout()
        # Object information
        self.name = name
        # Graphical objects
        self.name_label = QLabel('Parameters of ' + self.name)
        self.name_label.setStyleSheet("color: darkblue; font-size: 15px;")
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.name_label)
        self.elem = {}
        try:
            # Create all the subitem from list of params
            all_options = process_list[name]['params']
            for id, option in enumerate(all_options.split(';')):
                option_items = process_list[name][option]
                item = option_items.split(':')
                if item[0] == 'int':
                    self.elem[option] = WidgetSlider(name=option, integer=True, signal_name=option)
                    self.elem[option].set_min_max_slider(float(item[1]), float(item[2]))
                    self.elem[option].slider_changed_signal.connect(self.update_options)
                    self.main_layout.addWidget(self.elem[option])
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


if __name__ == "__main__":
    def action_changed(event):
        print(f'Changed {event}')


    import sys
    from PyQt6.QtWidgets import (QApplication, QMainWindow)

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("Source_Widget test")
    main_window.setGeometry(500, 100, 400, 600)
    central_widget = ProcessOptions(name="binarize")
    main_window.setCentralWidget(central_widget)

    central_widget.changed.connect(action_changed)

    main_window.show()
    sys.exit(app.exec())
