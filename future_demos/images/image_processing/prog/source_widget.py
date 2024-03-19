# -*- coding: utf-8 -*-
"""*image_display_widget* file.

*image_display_widget* file that contains :

    * :class::ImageDisplayWidget

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""
import numpy as np
from image import Image
from logo_lense_widget import LogoLEnsEWidget

from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QGridLayout,
    QMessageBox
)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt, pyqtSignal

class SourceWidget(QWidget):
    """Generate a widget to display an image. Children of QWidget.
    
    :param image: Image to display.
    :type image: Image
    :param image_display: Graphical object to contain the image.
    :type image_display: QLabel
    :param main_layout: Main layout of the widget.
    :type main_layout: QVBoxLayout
    
    """
    
    loaded = pyqtSignal(str)
    
    def __init__(self) -> None:
        """
        Default constructor of the class.
        """
        super().__init__(parent=None)
        self.logo_widget = LogoLEnsEWidget(200, 300)
        self.title_label = QLabel('Demo Image Processing')
        self.title_label.setStyleSheet("color: purple; font-size: 20px;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # 
        self.image_source_label = QLabel('Image :')
        self.image_source_name_label = QLabel('TO DO')
        self.image_source_button = QPushButton('Load Image')
        self.image_source_button.clicked.connect(self.action_image_button)
        self.webcam_source_label = QLabel('Webcam :')
        self.webcam_source_name_label = QLabel('TO DO')
        self.webcam_source_button = QPushButton('Start Webcam')
        self.webcam_source_button.clicked.connect(self.action_webcam_button)
        self.sensor_source_label = QLabel('Sensor :')
        self.sensor_source_name_label = QLabel('TO DO')
        self.sensor_source_button = QPushButton('Start Sensor')
        self.sensor_source_button.clicked.connect(self.action_sensor_button)
        
        # Graphical elements of the interface
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.logo_widget, 0, 0, 2, 1)
        self.main_layout.addWidget(self.title_label, 2, 0)
        self.main_layout.setColumnStretch(0, 2)
        self.main_layout.setColumnStretch(1, 1)
        self.main_layout.setColumnStretch(2, 1)
        self.main_layout.setColumnStretch(3, 1)
        self.main_layout.setRowStretch(0, 1)
        self.main_layout.setRowStretch(1, 1)
        self.main_layout.setRowStretch(2, 1)
        self.main_layout.addWidget(self.image_source_label, 0, 1)
        self.main_layout.addWidget(self.image_source_name_label, 0, 2)
        self.main_layout.addWidget(self.image_source_button, 0, 3)
        self.main_layout.addWidget(self.webcam_source_label, 1, 1)
        self.main_layout.addWidget(self.webcam_source_name_label, 1, 2)
        self.main_layout.addWidget(self.webcam_source_button, 1, 3)
        self.main_layout.addWidget(self.sensor_source_label, 2, 1)
        self.main_layout.addWidget(self.sensor_source_name_label, 2, 2)
        self.main_layout.addWidget(self.sensor_source_button, 2, 3)
        
        self.setLayout(self.main_layout)

    def action_image_button(self, event):
        print('Image')
        self.loaded.emit('image')

    def action_webcam_button(self, event):
        print('Webcam')
        self.loaded.emit('webcam')

    def action_sensor_button(self, event):
        print('Sensor')
        self.loaded.emit('sensor')

if __name__ == "__main__":

    def action_loaded(event):
        print(event)

    import sys
    from PyQt6.QtWidgets import (QApplication, QMainWindow)
    
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("Source_Widget test")
    main_window.setGeometry(100, 100, 1000, 600)
    central_widget = SourceWidget()
    main_window.setCentralWidget(central_widget)
    
    central_widget.loaded.connect(action_loaded)
    
    main_window.show()
    sys.exit(app.exec())