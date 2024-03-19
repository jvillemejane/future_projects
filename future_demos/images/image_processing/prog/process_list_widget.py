# -*- coding: utf-8 -*-
"""*process_list_widget* file.

*process_list_widget* file that contains :

    * :class::ProcessListWidget

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""
import numpy as np
from image import Image
from image_process import ImageProcess

from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QCheckBox,
    QGridLayout, QVBoxLayout,
    QMessageBox, QFileDialog
)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt, pyqtSignal

from image_process import ImageProcess

# List of parameters for all the available process
binarize_params = {
    "function": ImageProcess.binarize,
    "params": 'treshold;',
    "treshold": 'int:0:255:'
}
blur_params = {
    "function": ImageProcess.blur,
    "params": 'kernel;size;',
    "size": 'odd:1:25;'
}
dilate_params = {
    "function": ImageProcess.dilate,
    "params": 'kernel;'
}
erode_params = {
    "function": ImageProcess.erode,
    "params": 'kernel;'
}

# List of the available process / filters
process_list = {
    "binarize": binarize_params,
	"blur": blur_params,
    "dilate": dilate_params,
    "erode": erode_params
}
'''
    "opening": ImageProcess.opening,
    "closing": ImageProcess.closing,
    "convolve": ImageProcess.convolve
}
'''


class ProcessListWidget(QWidget):
    """Generate a widget to select a process to do on the initial image.

    :param main_layout: Main layout of the widget.
    :type main_layout: QVBoxLayout
    
    """
    
    changed = pyqtSignal(str)
    
    def __init__(self) -> None:
        """Default constructor of the class.
        """
        super().__init__(parent=None)
        self.params_dict = {}
        self.params_dict['init'] = True
        
        # Main Layout
        self.main_layout = QVBoxLayout()
        
        # Graphical elements of the interface
        self.selected = None
        self.processes_dict = {}
        for i, (item_name, item_function) in enumerate(process_list.items()):
            self.processes_dict[item_name] = ProcessItem(item_name)
            self.processes_dict[item_name].changed.connect(self.action_checked)
            self.processes_dict[item_name].check_item.setEnabled(False)
            self.processes_dict[item_name].params_item.setEnabled(False)
            self.main_layout.addWidget(self.processes_dict[item_name])
        
        self.setLayout(self.main_layout)
    
    def action_checked(self, event) -> None:
        """Action performed when a process is checked
        """
        self.changed.emit(event)
        
    
    def enable(self) -> None:
        """Activate all the checkbox and button of the interface
        """
        for i, (item_name, item_function) in enumerate(process_list.items()):
            self.processes_dict[item_name].check_item.setEnabled(True)
            self.processes_dict[item_name].params_item.setEnabled(True)

    def disable(self) -> None:
        """Unactivate all the checkbox and button of the interface
        """
        for i, (item_name, item_function) in enumerate(process_list.items()):
            self.processes_dict[item_name].check_item.setEnabled(False)
            self.processes_dict[item_name].params_item.setEnabled(False)

    def uncheck_all(self) -> None:
        """Uncheck all the checkbox.
        """
        for i, (item_name, item_function) in enumerate(process_list.items()):
            self.processes_dict[item_name].check_item.setChecked(False)   
        
    
class ProcessItem(QWidget):
    """Generate an item of image process.
    
    :param main_layout: Main layout of the widget.
    :type main_layout: QVBoxLayout
    
    """
    
    changed = pyqtSignal(str)
    
    def __init__(self, name='') -> None:
        """Default constructor of the class.
        
        :param name: Name of the item.
        :type name: str
        
        """
        super().__init__(parent=None)        
        self.name_label = QLabel(name)
        self.check_item = QCheckBox()
        self.check_item.clicked.connect(self.action_checked)
        self.params_item = QPushButton('Options')
        self.params_item.clicked.connect(self.action_params)
        
        # Graphical elements of the interface
        self.main_layout = QGridLayout() 

        self.main_layout.addWidget(self.check_item, 0, 0)
        self.main_layout.addWidget(self.name_label, 0, 1)
        self.main_layout.addWidget(self.params_item, 0, 2)
        
        self.setLayout(self.main_layout)   

    def action_checked(self, event) -> None:
        """
        Action performed when a process is checked
        """
        self.changed.emit(self.name_label.text())
        
    def action_params(self, event) -> None:
        if self.check_item.isChecked():
            self.params_window = ProcessParams(self.name_label.text())
            self.params_window.show()


class ProcessParams(QWidget):
    """ProcessParams class, children of QWidget.
    
    Class to display and to change the available parameters of a process.
    
    """
    
    def __init__(self, name:str =''):
        """Default constructor of the class.
        
        :param name: Name of the process.
        :type name: str
        
        """
        super().__init__(parent=None)
        # Main layout
        self.main_layout = QVBoxLayout()
        # Graphical objects
        self.name_label = QLabel('Parameters of '+name)
        self.main_layout.addWidget(self.name_label)
        
        
        self.setFixedSize(300, 400)
        self.setLayout(self.main_layout)

if __name__ == "__main__":

    def action_loaded(event):
        print(event)

    import sys
    from PyQt6.QtWidgets import (QApplication, QMainWindow)
    
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("Source_Widget test")
    main_window.setGeometry(100, 100, 1000, 600)
    central_widget = ProcessListWidget()
    main_window.setCentralWidget(central_widget)
    
    central_widget.loaded.connect(action_loaded)
    
    main_window.show()
    sys.exit(app.exec())