# -*- coding: utf-8 -*-
"""*demo_image_processing* file.

*demo_image_processing* file that contains :

    * :class::DemoImageProcessing

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""

import sys
import numpy as np

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout,
    QMessageBox
)
from PyQt6.QtCore import Qt

from image_display_widget import ImageDisplayWidget
from source_widget import SourceWidget
from process_list_widget import ProcessListWidget
from process_list import *


class DemoImageProcessing(QMainWindow):
    """DemoImageProcessing class, children of QMainWindow.
    
    Main class of the demo.

    """

    def __init__(self, height: int, width: int) -> None:
        """
        Default constructor of the class.

        :param height: Height of the window.
        :type height: int
        :param width: Width of the window.
        :type width: int

        """
        super().__init__()
        self.resize_event = self.handle_resize
        # widget state
        self.is_image_set = False  # If an image is selected
        self.is_live_set = False  # If a live source is selected
        self.is_process_set = False  # If a process is selected
        self.actual_values = {}

        self.setWindowTitle("Demo Image Processing / LEnsE")
        # Widget geometry information
        self.border = 30
        self.height = height - 3 * self.border
        self.width = width - 2 * self.border
        self.height_img = self.height // 2 - 1 * self.border
        self.width_img = self.width // 2
        self.setGeometry(self.border, self.border, self.width, self.height)
        self.central_widget = QWidget()

        self.central_layout = QGridLayout()

        self.initial_image_display_widget = ImageDisplayWidget(name='Initial Image',
                                                               height=self.height_img,
                                                               width=self.width_img,
                                                               bg=(200, 200, 200))
        self.process_image_display_widget = ImageDisplayWidget(name='Output Image',
                                                               height=self.height_img,
                                                               width=self.width_img,
                                                               bg=(180, 180, 180))
        # internal right widget
        right_widget = QWidget()
        right_layout = QGridLayout()
        right_layout.addWidget(self.initial_image_display_widget, 0, 0)
        right_layout.addWidget(self.process_image_display_widget, 1, 0)
        right_layout.setRowStretch(0, 1)
        right_layout.setRowStretch(1, 1)
        right_widget.setLayout(right_layout)

        self.source_widget = SourceWidget()
        # TO DO : resize logo and widget on window resizing
        self.source_widget.load_image.connect(self.load_source_image)
        self.source_widget.webcam_source_button.setEnabled(False)
        self.source_widget.sensor_source_button.setEnabled(False)
        self.process_list_widget = ProcessListWidget()
        self.process_list_widget.changed.connect(self.update_process_image)
        self.process_list_widget.checked.connect(self.check_process)
        self.process_list_widget.clicked.connect(self.update_options)
        self.process_list_widget.disable()

        # internal left widget
        left_widget = QWidget()
        left_layout = QGridLayout()
        left_layout.addWidget(self.source_widget, 0, 0)
        left_layout.addWidget(self.process_list_widget, 1, 0)
        left_layout.setRowStretch(0, 1)
        left_layout.setRowStretch(1, 2)
        left_widget.setLayout(left_layout)

        self.central_layout.addWidget(left_widget, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        self.central_layout.addWidget(right_widget, 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        # Grid of 2 x 2 widgets with the same size
        self.central_layout.setColumnStretch(0, 1)
        self.central_layout.setColumnStretch(1, 3)

        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

    def load_source_image(self, event) -> None:
        """
        Action performed after a click in the source widget.
        
        :param event: Triggering event.
        """
        try:
            event_data = event.split(';')
            if event_data[0] == 'image':
                self.is_image_set = self.initial_image_display_widget.set_image_from_path(event_data[1], 10, 10)
                self.process_image_display_widget.set_image_from_path(event_data[1], 10, 10)
                self.handle_resize()
            if self.is_image_set:
                self.process_list_widget.enable()
            else:
                self.process_list_widget.disable()
        except Exception as e:
            print("Exception - source loaded: " + str(e) + "")

    def update_process_image(self, event):
        """Action performed when an option of a process changed."""
        try:
            # Update the local value of a parameter of a process.
            event_split = event.split(':')
            if len(event_split) > 1:
                option_name = event_split[2]
                process_name = event_split[0]
                if self.actual_values.get(process_name + ':' + option_name):
                    values = self.process_list_widget.processes_dict[process_name].params_window.get_values()
                    self.actual_values[process_name + ':' + option_name] = values[option_name]
                else:
                    new_value = process_list[process_name][option_name].split(':')[-1]
                    self.actual_values[process_name + ':' + option_name] = new_value
            else:
                process_name = event
            self.process_image(process_name)
            self.handle_resize()
        except Exception as e:
            print("Exception - update_process_image: " + str(e) + "")

    def update_options(self, event):
        """Action performed when "Options" button is clicked.
        """
        try:
            all_params = process_list[event]['params']
            dict_values = {}
            for id, option_name in enumerate(all_params.split(';')):
                option_type = get_options_type(event, option_name)
                dict_values[option_name] = 127
                # Depending on the type of the option
                if option_type == 'int':
                    # If a value was not already set, take the initial value from process_list.
                    if self.actual_values.get(event + ':' + option_name) is None:
                        new_value = get_options_int()[-1]
                        self.actual_values[event + ':' + option_name] = new_value
                        dict_values[option_name] = new_value
                    # Else get the previous stored value.
                    else:
                        dict_values[option_name] = self.actual_values.get(event + ':' + option_name)
            self.process_list_widget.processes_dict[event].params_window.set_values(dict_values)
        except Exception as e:
            print("Exception - update_options: " + str(e) + "")

    def check_process(self, event):
        """Action performed when a process is checked."""
        print(f'check_process {event}')
        try:
            input_image = self.initial_image_display_widget.get_image()
            # If the process is checked, process the image and display it.
            if self.process_list_widget.processes_dict[event].check_item.isChecked():
                all_options = process_list[event]['params']
                for id, option in enumerate(all_options.split(';')):
                    option_items = process_list[event][option]
                    item = option_items.split(':')
                    option_name = option
                    if self.actual_values.get(event + ':' + option_name) is None:
                        new_value = int(process_list[event][option_name].split(':')[-1])
                        self.actual_values[event + ':' + option_name] = new_value
                self.process_image(event)
            # If the process is not checked, then display initial image in the process display area.
            else:
                self.process_image_display_widget.set_image_from_image(input_image)
            self.handle_resize()
        except Exception as e:
            print("Exception - check_process: " + str(e) + "")

    def process_image(self, event):
        """Process the image with the appropriate function."""
        try:
            input_image = self.initial_image_display_widget.get_image()
            option_event = event.split(':')
            process_name = option_event[0]
            process_dict = {}
            all_options = get_process_options(process_name)
            # For each parameter of the process, collect the value of the parameters.
            for id, option_name in enumerate(all_options.split(';')):
                option_type = get_options_type(process_name, option_name)
                if option_type == 'int':
                    process_dict[option_name] = self.actual_values[process_name + ':' + option_name]
            # Process the new image.
            temp_image = process_list[process_name]["function"](input_image, process_dict)
            self.process_image_display_widget.set_image_from_image(temp_image)
        except Exception as e:
            print("Exception - process_image: " + str(e) + "")

    def handle_resize(self):
        """
        Action performed when the window is resized.
        """
        try:
            # Get the new size of the main window
            new_size = self.size()
            self.width = new_size.width()
            self.height = new_size.height()

            self.height_img = self.height // 2 - 1 * self.border
            self.width_img = self.width // 2

            self.initial_image_display_widget.set_size_display(
                self.height_img, self.width_img)
            self.process_image_display_widget.set_size_display(
                self.height_img, self.width_img)

            if self.is_image_set is True:
                self.initial_image_display_widget.resize_image(
                    self.height_img, self.width_img)
                if self.is_process_set is True:
                    self.process_image_display_widget.resize_image(
                        self.height_img, self.width_img)
                else:
                    self.process_image_display_widget.resize_image(
                        self.height_img, self.width_img)

        except Exception as e:
            print("Exception - handle_resize: " + str(e) + "")

    def showEvent(self, event):
        """
        showEvent redefinition. Use when the window is loaded
        """
        super().showEvent(event)
        self.handle_resize()

    def closeEvent(self, event) -> None:
        """
        closeEvent redefinition. Use when the user clicks 
        on the red cross to close the window
        """
        reply = QMessageBox.question(self, 'Quit', 'Do you really want to close ?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    rect = screen.availableGeometry()
    main_window = DemoImageProcessing(rect.height(), rect.width())
    main_window.show()
    sys.exit(app.exec())
