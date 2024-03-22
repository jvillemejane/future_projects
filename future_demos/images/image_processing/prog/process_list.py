# -*- coding: utf-8 -*-
"""*process_list* file.

*process_list* file that contains :

    * :class::ProcessList  ??

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""

from image_process import ImageProcess

# List of parameters for all the available process
binarize_params = {
    "function": ImageProcess.binarize,
    "params": 'threshold',
    "threshold": 'int:0:255:100'
}
blur_params = {
    "function": ImageProcess.blur,
    "params": 'kernel;size',
    "size": 'odd:1:25:5'
}
dilate_params = {
    "function": ImageProcess.dilate,
    "params": 'kernel'
}
erode_params = {
    "function": ImageProcess.erode,
    "params": 'kernel'
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

