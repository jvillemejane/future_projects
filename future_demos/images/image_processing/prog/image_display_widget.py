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
    QVBoxLayout
)
from PyQt6.QtGui import QPixmap, QImage, QColor, QPalette

class ImageDisplayWidget(QWidget):
    """Generate a widget to display an image. Children of QWidget.
    
    :param image: Image to display.
    :type image: Image
    :param image_display: Graphical object to contain the image.
    :type image_display: QLabel
    :param main_layout: Main layout of the widget.
    :type main_layout: QVBoxLayout
    
    """
    
    def __init__(self, name: str = '', height: int = 0, width: int = 0,
                 bg: tuple[int, int, int] = (0, 0, 0)) -> None:
        """
        Default constructor of the class.

        :param name: Name to display.
        :type name: str           
        :param height: Height of the area. Default 0.
        :type height: int   
        :param width: Width of the area. Default 0.
        :type width: int
        :param bg: Background of the widget. Default (0, 0, 0).
        :type bg: tuple[int, int, int]
        
        """
        super().__init__(parent=None)
        # Set background color for the entire widget
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(bg[0], bg[1], bg[2]))
        self.setPalette(palette)

        self.height = height
        self.width = width
        
        self.image = Image()  # Initial image
        self.image_resized = Image() # Resized image
        self.image_display = QLabel(name)
        blank_image = np.ones((self.height, self.width, 3))
        blank_image[:,:,0] = bg[0]*blank_image[:,:,0]
        blank_image[:,:,1] = bg[1]*blank_image[:,:,1]
        blank_image[:,:,2] = bg[2]*blank_image[:,:,2]
        self.set_image_from_array(blank_image)
                
        # Graphical elements of the interface
        self.main_layout = QVBoxLayout() 
        self.main_layout.addWidget(self.image_display)
        
        self.setLayout(self.main_layout)

    def set_image_from_image(self, image) -> None:
        """
        Open an image file from an image.

        :param image: Image to display.
        :type image: Image

        """
        self.image = image
        self.image_resized = image
        self.display_image()

    def set_image_from_path(self, filename: str, h: int = 0, w: int = 0) -> bool:
        """
        Open an image file from its path and filename.

        :param filename: Name of the file.
        :type filename: str
        :param h: Height of the area.
        :type h: int   
        :param w: Width of the area.
        :type w: int    
        
        :return: True if the file was successfully read, False otherwise.
        :rtype: bool

        """
        success = self.image.open(filename)
        if w != 0 or h != 0:
            self.image_resized = self.image.resize_image_ratio(h, w)
        elif self.width != 0 or self.height != 0:
            self.image_resized = self.image.resize_image_ratio(self.height, self.width)
        else:
            self.image_resized = self.image
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
        self.image.create(pixels)
        self.image_resized = self.image
        self.display_image()

    def set_size_display(self, h: int, w: int) -> None:
        """
        Set the size of the widget.
        
        :param h: Maximum height of the area.
        :type h: int   
        :param w: Maximum width of the area.
        :type w: int 
        
        """
        self.width = w
        self.height = h
      
    def get_image(self) -> Image:
        """
        Return the displayed image.
        
        :return: Image displayed in the widget.
        :rtype: Image
        
        """
        return self.image

    def resize_image(self, h: int, w: int) -> None:
        """
        Resize the image.
        
        :param h: New height of the area.
        :type h: int   
        :param w: New width of the area.
        :type w: int 
        
        """
        max_height, max_width = self.image.getSize()
         
        if h > max_height or w > max_width:
            # Resize at the maximum initial image size
            self.image_resized = self.image
        if h > 20 and w > 20:
            self.image_resized = self.image.resize_image_ratio(h-20, w-20)
        else:
            self.image_resized = self.image.resize_image_ratio(h, w)
        self.display_image()

    def display_image(self) -> None:
        """
        Display the image.

        """    
        height, width = self.image_resized.getSize()
        channels = self.image_resized.getChannels() 
        
        # Convert OpenCV image to QImage
        bytes_per_line = channels * width
        if channels == 1:
            format = QImage.Format.Format_Grayscale8
        else:
            format = QImage.Format.Format_BGR888
        q_image = QImage(self.image_resized.getPixels(), width, height, bytes_per_line, format)
        
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