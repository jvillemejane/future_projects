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
    QMessageBox
)


class DemoImageProcessing(QMainWindow):
    """DemoImageProcessing class, children of QMainWindow.
    
    Main class of the demo.

    """
    def __init__(self) -> None:
        """
        Default constructor of the class.
        """
        super().__init__()
        self.setWindowTitle("Demo Image Processing / LEnsE")
        self.setGeometry(100, 100, 500, 400)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)


    def closeEvent(self, event):
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