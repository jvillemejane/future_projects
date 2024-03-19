Image processing Demo
#####################

This demonstration...

Requirements
************

This demonstration requires:

* Python 3.9 or higher
* opencv2
* PyQt6
* Numpy

Image processing basics
***********************

Linear transforms (blur, ...)

Non-linear transforms (median...)

Morphologic transforms


Development
***********

Image processing
================

* :class:`Image`: to open, write, create and display an image, using opencv2
* :class:`ImageProcess`: to process images (blur, dilate, erode, opening, closing, convolve)

Human-Machine Interface
=======================

* :class:`DemoImageProcessing`: the main container (QMainWindow) of the application.
* :class:`ImageDisplayWidget`: to display an image (from :class:`Image` class)
* :class:`SourceWidget`: to select a source of image (from :class:`Image` class)


Ressources
**********

https://www.iqsdirectory.com/articles/machine-vision-system.html
