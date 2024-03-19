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
from process_list_widget import ProcessListWidget, process_list


class DemoImageProcessing(QMainWindow):
    """DemoImageProcessing class, children of QMainWindow.
    
    Main class of the demo.

    """
    def __init__(self) -> None:
        """
        Default constructor of the class.
        """
        super().__init__()
        self.resizeEvent = self.handle_resize
        self.is_image_set = False       # If an image is selected
        self.is_live_set = False        # If a live source is selected
        self.is_process_set = False     # If a process is selected
        
        self.setWindowTitle("Demo Image Processing / LEnsE")
        self.setGeometry(50, 50, 1200, 750)
        self.central_widget = QWidget()
        
        self.central_layout = QGridLayout()
        
        self.initial_image_display_widget = ImageDisplayWidget(name='Initial Image', height=100, width=100) 
        self.process_image_display_widget = ImageDisplayWidget(name='Output Image', height=100, width=100)
        
        self.source_widget = SourceWidget() 
        # TO DO : resize logo and widget on window resizing
        self.source_widget.loaded.connect(self.source_loaded)
        self.source_widget.webcam_source_button.setEnabled(False)
        self.source_widget.sensor_source_button.setEnabled(False)
        self.process_list_widget = ProcessListWidget()
        self.process_list_widget.changed.connect(self.action_process_changed)
        
        self.central_layout.addWidget(self.source_widget, 0, 0)
        self.central_layout.addWidget(self.process_list_widget, 1, 0)
        self.central_layout.addWidget(self.initial_image_display_widget, 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.central_layout.addWidget(self.process_image_display_widget, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Grid of 2 x 2 widgets with the same size
        self.central_layout.setRowStretch(0, 1)
        self.central_layout.setRowStretch(1, 1)
        self.central_layout.setColumnStretch(0, 2)
        self.central_layout.setColumnStretch(1, 3)
        
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

    def source_loaded(self, event) -> None:
        """
        Action performed after a click in the source widget.
        
        :param event: Triggering event.
        """
        event_data = event.split(';')
        if event_data[0] == 'image':
            self.is_image_set = self.initial_image_display_widget.set_image_from_path(event_data[1], 10, 10)
            self.handle_resize(event)
        elif event_data[0] == 'webcam':
            print('webcam - NOT YET IMPLEMENTED')
        elif event_data[0] == 'sensor':
            print('sensor - NOT YET IMPLEMENTED')
        
        if self.is_image_set:
            self.process_list_widget.enable()
        else:
            self.process_list_widget.disable()
    
    def action_process_changed(self, event):
        """
        Action performed when the process to apply change.
        """
        print('Process changed: '+event)
        is_checked = False
        if self.process_list_widget.processes_dict[event].check_item.isChecked():
            is_checked = True
            input_image = self.initial_image_display_widget.get_image()
            # To get from options - 
            kernel = np.ones((3,3)) 
            self.process_list_widget.params_dict["kernel"] = kernel
            self.process_list_widget.params_dict["size"] = 3
            self.process_list_widget.params_dict["treshold"] = 110
            
            temp_image = process_list[event](input_image, self.process_list_widget.params_dict)
            self.process_image_display_widget.set_image_from_image(temp_image)
            print('Checked')
        
        self.process_list_widget.uncheck_all()
        if is_checked is True:
            self.is_process_set = True
            self.process_list_widget.processes_dict[event].check_item.setChecked(True)
        else:
            self.is_process_set = False
            # Clear process_image display
            pass
        
        self.handle_resize(event)
        
    def handle_resize(self, event):
        """
        Action performed when the window is resized.
        """
        # Get the new size of the main window
        new_size = self.size()
        width = new_size.width()
        height = new_size.height()
        
        if height > 40 and width > 40:
            self.initial_image_display_widget.set_size_display(height//2 - 20, width//2 - 20)
            self.process_image_display_widget.set_size_display(height//2 - 20, width//2 - 20)
            if self.is_image_set is True:
                self.initial_image_display_widget.resize_image(height//2 - 20, width//2 - 20)
            if self.is_process_set is True:
                print('Process Checked 1')
                self.process_image_display_widget.resize_image(height//2 - 20, width//2 - 20)
        else:
            self.initial_image_display_widget.set_size_display(height//2, width//2)
            self.process_image_display_widget.set_size_display(height//2, width//2)
            if self.is_image_set is True:
                self.initial_image_display_widget.resize_image(height//2, width//2)
            if self.is_process_set is True:
                print('Process Checked 2')
                self.process_image_display_widget.resize_image(height//2, width//2)        

        
    def showEvent(self, event):
        """
        showEvent redefinition. Use when the window is loaded
        """
        super().showEvent(event)
        self.handle_resize(event)

    def closeEvent(self, event) -> None:
        """
        closeEvent redefinition. Use when the user clicks 
        on the red cross to close the window
        """
        reply = QMessageBox.question(self, 'Quit', 'Do you really want to close ?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            # self.central_widget.quit_application()
            event.accept()  # L'utilisateur a confirmé la fermeture
        else:
            event.ignore()  # L'utilisateur a annulé la fermeture



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = DemoImageProcessing()
    main_window.show()
    sys.exit(app.exec())