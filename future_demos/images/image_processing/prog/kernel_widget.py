# -*- coding: utf-8 -*-
"""*kernel_widget* file.

*kernel_widget* file that contains :class::KernelWidget

.. module:: KernelWidget
   :synopsis: class to display a kernel (image processing) information in PyQt6.

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""

from PyQt6.QtWidgets import (
    QGridLayout, QVBoxLayout,
    QWidget, QLineEdit, QLabel, QPushButton, QSlider,
    QMessageBox)
from PyQt6.QtCore import pyqtSignal, Qt

import numpy as np
from image_display_widget import *

class KernelWidget(QWidget):
    """Create a Widget to display a kernel (image processing). Children of QWidget
    """

    def __init__(self, name: str = "", size: int = 3) -> None:
        """
        
        :param name: Name of the kernel. Default "".
        :type name: str, optional
        :param size: Size of the kernel. Default 3.
        :type size: int, optional

        """
        super().__init__(parent=None)

        # Global values
        self.size = size
        self.name = name
        self.kernel = np.ones((size, size))
        # square of display_size pixels for each coefficient of the kernel
        self.display_size = 50
        self.kernel_display = np.ones((self.display_size * self.size, self.display_size * self.size))
        print(f'Kernel Display:{self.kernel_display}')

        self.kernel_display_widget = ImageDisplayWidget(name=self.name,
                                                        height=self.display_size * self.size+20,
                                                        width=self.display_size * self.size+20
                                                        )
        self.kernel_display_widget.set_image_from_array(self.kernel_display)
        ''' Layout Manager '''
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.kernel_display_widget)

        self.setLayout(self.main_layout)




if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import (QApplication, QMainWindow)

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("KernelWidget test")
    main_window.setGeometry(100, 100, 500, 400)
    central_widget = KernelWidget()
    main_window.setCentralWidget(central_widget)

    main_window.show()
    sys.exit(app.exec())
