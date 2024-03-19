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

class SourceWidget(QWidget):
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

    


if __name__ == "__main__":
    
    import sys
    from PyQt6.QtWidgets import (QApplication, QMainWindow)
    
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("Source_Widget test")
    main_window.setGeometry(100, 100, 500, 400)
    central_widget = SourceWidget()
    main_window.setCentralWidget(central_widget)
    
    main_window.show()
    sys.exit(app.exec())