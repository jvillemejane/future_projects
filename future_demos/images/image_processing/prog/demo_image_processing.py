# -*- coding: utf-8 -*-
"""*demo_image_processing* file.

*demo_image_processing* file that contains :

    * :class::DemoImageProcessing

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""

import sys

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QGridLayout,
    QMessageBox
)

from image_display_widget import ImageDisplayWidget
from source_widget import SourceWidget


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
        self.is_image_set = False
        
        self.setWindowTitle("Demo Image Processing / LEnsE")
        self.setGeometry(50, 50, 1200, 750)
        self.central_widget = QWidget()
        
        self.central_layout = QGridLayout()
        
        self.initial_image_display_widget = ImageDisplayWidget(100, 100)
        self.source_widget = SourceWidget()
        self.source_widget.loaded.connect(self.source_loaded)
        self.process_image_display_widget = ImageDisplayWidget(100, 100)
        
        self.central_layout.addWidget(self.source_widget, 0, 0)
        self.central_layout.addWidget(self.initial_image_display_widget, 0, 1)
        self.central_layout.addWidget(self.output_image_display_widget, 1, 1)
        
        # Grid of 2 x 2 widgets with the same size
        self.central_layout.setRowStretch(0, 1)
        self.central_layout.setRowStretch(1, 1)
        self.central_layout.setColumnStretch(0, 1)
        self.central_layout.setColumnStretch(1, 1)
        
        self.central_widget.setLayout(self.central_layout)
        self.setCentralWidget(self.central_widget)

    def source_loaded(self, event) -> None:
        """
        Action performed after a click in the source widget.
        
        :param event: Triggering event.
        """
        event_data = event.split(';')
        if event_data[0] == 'image':
            self.is_image_set = self.initial_image_display_widget.set_image_from_path(event_data[1])
            # TEST TO DO ON SIZE OF THE IMAGE COMPARED TO SIZE OF HALF OF THE WINDOW !! IF NOT OK, RESIZE !!
        elif event_data[0] == 'webcam':
            print('webcam - NOT YET IMPLEMENTED')
        elif event_data[0] == 'sensor':
            print('sensor - NOT YET IMPLEMENTED')
        
    def handle_resize(self, event):
        """
        Action performed when the window is resized.
        """
        # Get the new size of the main window
        new_size = self.size()
        width = new_size.width()
        height = new_size.height()
        
        if self.is_image_set is True:
            self.initial_image_display_widget.resize_display(height//2, width//2)
        
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