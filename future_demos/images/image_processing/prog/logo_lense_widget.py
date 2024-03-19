# -*- coding: utf-8 -*-
"""*logo_lense_widget* file.

    *logo_lense_widget* file that contains :

    * :class::LogoLEnsEWidget

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""
import numpy as np
from image import Image
import cv2 as cv

from PyQt6.QtWidgets import (
    QWidget, QLabel,
    QVBoxLayout
)
from PyQt6.QtGui import QPixmap, QImage



class LogoLEnsEWidget(QWidget):
    """Display the LEnsE logo. Children of QWidget.
    
    :param image: Image to display.
    :type image: Image
    :param image_display: Graphical object to contain the image.
    :type image_display: QLabel
    :param main_layout: Main layout of the widget.
    :type main_layout: QVBoxLayout
    
    """
    
    def __init__(self, height:int, width:int) -> None:
        """
        Default constructor of the class.
        
        :param height: Height of the displayed image.
        :type height: int  
        :param width: Width of the displayed image.
        :type width: int       
        
        """
        super().__init__(parent=None)
        self.image = Image()
        self.image.open("./assets/logo_lense.png")
        self.image_display = QLabel()
        
        self.image.resize_image_ratio(height, width)
        
        image_height, image_width = self.image.getSize()
        channels = self.image.getChannels()    
        # Convert OpenCV image to QImage
        bytes_per_line = channels * image_width
        q_image = QImage(self.image.getPixels(), image_width, image_height, bytes_per_line, QImage.Format.Format_BGR888)
        
        # Display QImage in QLabel
        self.image_display.setPixmap(QPixmap.fromImage(q_image))
                
        # Graphical elements of the interface
        self.main_layout = QVBoxLayout() 
        self.main_layout.addWidget(self.image_display)
        
        self.setLayout(self.main_layout)      



if __name__ == "__main__":
    
    import sys
    from PyQt6.QtWidgets import (QApplication, QMainWindow)
    
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("Image_Display_Widget test")
    main_window.setGeometry(100, 100, 500, 400)
    central_widget = LogoLEnsEWidget(200,500)
    main_window.setCentralWidget(central_widget)
    
    main_window.show()
    sys.exit(app.exec())