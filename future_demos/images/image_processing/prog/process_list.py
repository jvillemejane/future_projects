# -*- coding: utf-8 -*-
"""*process_list* file.

*process_list* file that contains :

    * :class::ProcessList  ??

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""

import numpy as np
from image_process import ImageProcess


def get_process_options(process_name) -> str:
    """Return the list of available options for a process.

    Each parameters are separated by ;
    """
    return process_list[process_name]['params']


def get_options_type(process_name, option_name) -> str:
    """Return the type of an option for a process."""
    return process_list[process_name][option_name].split(':')[0]


def get_options_int(process_name, option_name) -> tuple[int, int, int]:
    """Return the list of available options for a process.

    :return: A tuple corresponding to minimum, maximum, init value
    :rtype: tuple[int, int, int]
    """
    params = process_list[process_name][option_name].split(':')
    min = params[1]
    max = params[2]
    init = params[3]
    return min, max, init


# List of parameters for all the available process
binarize_params = {
    "function": ImageProcess.binarize,
    "params": 'threshold',
    "threshold": 'int:0:255:40'
}
blur_params = {
    "function": ImageProcess.blur,
    "params": 'kernel;size',
    "kernel": "ker:blur:",
    "kernel_blur": np.ones((25, 25)),
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

if __name__ == "__main__":
    type = get_options_type("binarize", "threshold")
    print(f'Type = {type}')