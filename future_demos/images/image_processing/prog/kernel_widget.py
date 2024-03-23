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
    QWidget, QLineEdit, QLabel, QPushButton
)

import numpy as np
from image_display_widget import *
from process_list import *


def expand_array(initial_array: np.ndarray, n_size: int) -> np.ndarray:
    """
    Expand the initial array where each value is deployed on a square of N cells.

    Args:
    initial_array (numpy.ndarray): The initial array.
    N (int): The size of the square.

    Returns:
    numpy.ndarray: The expanded array.
    """
    # Determine the size of the expanded array
    expanded_size = n_size * initial_array.shape[0]

    # Create an expanded array filled with zeros
    expanded_array = np.zeros((expanded_size, expanded_size), dtype=initial_array.dtype)

    # Iterate over the initial array and deploy each value on a square of N cells
    for i in range(initial_array.shape[0]):
        for j in range(initial_array.shape[1]):
            value = initial_array[i, j]
            expanded_array[i * n_size:(i + 1) * n_size, j * n_size:(j + 1) * n_size] = value
    return expanded_array


def add_border(array, n_cells, value=0):
    """
    Add a border of N cells around a NumPy array.

    Args:
    array (numpy.ndarray): The input array.
    n_cells (int): The width of the border (number of cells).
    value: The value to fill the border cells with. Default is 0.

    Returns:
    numpy.ndarray: The array with the border added.
    """
    height, width = array.shape

    # Create a larger array to accommodate the border
    bordered_array = np.full((height + 2 * n_cells, width + 2 * n_cells), value, dtype=array.dtype)

    # Copy the original array into the center of the bordered array
    bordered_array[n_cells:n_cells + height, n_cells:n_cells + width] = array

    return bordered_array


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
        self.params_window = None
        # Graphical elements
        self.name_label = QLabel(self.name)
        self.name_label.setStyleSheet("color: purple; font-size: 12px;")
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.size_label = QLabel('Size = ' + str(self.size))
        self.size_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.modify_button = QPushButton('Modify')
        self.modify_button.clicked.connect(self.action_modify)
        self.kernel = np.ones((size, size))
        # square of display_size pixels for each coefficient of the kernel
        self.display_size = 20
        self.kernel_display = []
        self.kernel_display_widget = ImageDisplayWidget(name=self.name,
                                                        height=self.display_size * self.size + 20,
                                                        width=self.display_size * self.size + 20,
                                                        bg=(220, 230, 210)
                                                        )
        self.update_display()
        ''' Layout Manager '''
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.name_label, 0, 0)
        self.main_layout.addWidget(self.size_label, 1, 0)
        self.main_layout.addWidget(self.kernel_display_widget, 2, 0)
        self.main_layout.addWidget(self.modify_button, 3, 0)
        self.main_layout.setRowStretch(0, 1)
        self.main_layout.setRowStretch(1, 1)
        self.main_layout.setRowStretch(2, 5)
        self.main_layout.setRowStretch(3, 1)

        self.setLayout(self.main_layout)

    def update_display(self):
        """Update the displayed kernel."""
        try:
            max_ker = np.max(self.kernel)
            min_ker = np.min(self.kernel)
            if max_ker == min_ker:
                new_array = 255 * (self.kernel / max_ker)
            else:
                delta = (max_ker - min_ker) + 1
                new_array = 255 * (self.kernel - min_ker / delta)
            new_disp_array = expand_array(new_array, self.display_size)
            new_disp_array = np.array(new_disp_array, dtype=np.uint8)
            self.kernel_display = new_disp_array
            display_with_border = add_border(new_disp_array, 10, 200)
            self.kernel_display_widget.set_image_from_array(display_with_border)
        except Exception as e:
            print("Exception - update_display: " + str(e) + "")

    def set_kernel(self, kernel: np.ndarray, display_size: int = 0) -> None:
        """Set a new kernel.
        
        :param kernel: Kernel to update.
        :type kernel: np.ndarray
        :param display_size: Size of each cell of the kernel, for display. In pixels. Default 0, no change.
        :type display_size: int
        
        """
        if display_size != 0 and display_size > 0:
            self.display_size = display_size
        self.kernel = kernel
        self.size = kernel.shape[0]
        self.update_display()

    def action_modify(self, event):
        """Action performed when the "Modify" button is clicked."""
        print(f'Modify {event}')
        self.params_window = ProcessOptions(self.name_label.text())
        self.params_window.changed.connect(self.action_changed_params)
        self.params_window.show()

if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import (QApplication, QMainWindow)

    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("KernelWidget test")
    main_window.setGeometry(800, 100, 300, 400)
    central_widget = KernelWidget("Test Kernel")
    main_window.setCentralWidget(central_widget)
    kernel_init = np.array([[1, 5, 2], [3, 8, 1], [1, 5, 2]])

    # Init from process_list file
    type_k = "blur"
    options = get_process_options(type_k)
    type_param = get_options_type(type_k, options)
    print(type_param)

    if type_param == 'ker':
        kernel_init = get_options_ker_kernel(type_k, options)
        print(f'widget : {kernel_init}')

    central_widget.set_kernel(kernel_init)

    main_window.show()
    sys.exit(app.exec())
