# -*- coding: utf-8 -*-
"""*image_display_widget* file.

*image_display_widget* file that contains :

    * :class::ImageDisplayWidget

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""
import numpy as np
from image import Image

from PyQt6.QtWidgets import (
    QWidget, QLabel,
    QVBoxLayout,
    QMessageBox
)
from PyQt6.QtGui import QPixmap, QImage

class ImageDisplayWidget(QWidget):
    """Generate a widget to display an image. Children of QWidget.
    
    :param image: Image to display.
    :type image: Image
    :param image_display: Graphical object to contain the image.
    :type image_display: QLabel
    :param main_layout: Main layout of the widget.
    :type main_layout: QVBoxLayout
    
    """
    
    def __init__(self) -> None:
        """
        Default constructor of the class.
        """
        super().__init__(parent=None)
        self.image = Image()
        self.image_display = QLabel()
                
        # Graphical elements of the interface
        self.main_layout = QVBoxLayout() 
        self.main_layout.addWidget(self.image_display)
        
        self.setLayout(self.main_layout)

    def set_image_from_path(self, filename: str) -> bool:
        """
        Open an image file from its path and filename.

        :param filename: Name of the file.
        :type filename: str
        
        :return: True if the file was successfully read, False otherwise.
        :rtype: bool

        """
        success = self.image.open(filename)
        self.display_image()
        return success
        
    def set_image_from_array(self, pixels: np.ndarray) -> None:
        """
        Create an image from an array.

        :param pixels: Array of pixels.
        :type pixels: np.ndarray
        
        :return: True if the file was successfully read, False otherwise.
        :rtype: bool

        """
        self.image.create(filename) 
        

    def display_image(self) -> None:
        """
        Display the image.

        """    
        height, width = self.image.getSize()
        channels = self.image.getChannels()    
        # Convert OpenCV image to QImage
        bytes_per_line = channels * width
        q_image = QImage(self.image.getPixels(), width, height, bytes_per_line, QImage.Format.Format_BGR888)
        
        # Display QImage in QLabel
        self.image_display.setPixmap(QPixmap.fromImage(q_image))

    def display_from_webcam(self) -> None:
        """
        Display image from a live acquisition (webcam).

        """  
        pass

    def display_from_sensor(self) -> None:
        """
        Display image from an industrial sensor.

        """  
        pass


if __name__ == "__main__":
    
    import sys
    from PyQt6.QtWidgets import (QApplication, QMainWindow)
    
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("Image_Display_Widget test")
    main_window.setGeometry(100, 100, 500, 400)
    central_widget = ImageDisplayWidget()
    main_window.setCentralWidget(central_widget)
    
    central_widget.set_image_from_path('../_data/robot.jpg')
    
    main_window.show()
    sys.exit(app.exec())