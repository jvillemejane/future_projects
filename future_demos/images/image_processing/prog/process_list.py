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
    min_v = params[1]
    max_v = params[2]
    init_v = params[3]
    return min_v, max_v, init_v


def get_options_ker_kernel(process_name, option_name) -> np.ndarray:
    """Get the initial kernel if exists."""
    options_values = process_list[process_name][option_name].split(':')
    if len(options_values) > 1:
        kernel_init = process_list[process_name][option_name + '_init']
        return kernel_init
    init_size = (3, 3)
    return np.ones(init_size, dtype=np.uint8)


def get_options_ker(process_name) -> str:
    """Get the initial kernel if exists."""
    options_values = process_list[process_name]['kernel'].split(':')
    return options_values
def get_options_ker_param(process_name, option_name) -> str:
    """Get the initial kernel if exists."""
    options_values = process_list[process_name]['kernel_'+option_name].split(':')
    return options_values

'''
"kernel": "ker:size",
"kernel_init": np.ones((3, 3)),
"kernel_size": 'odd:1:7:3'
'''

# List of parameters for all the available process
binarize_params = {
    "function": ImageProcess.binarize,
    "params": 'threshold',
    "threshold": 'int:0:255:40'
}
blur_params = {
    "function": ImageProcess.blur,
    "params": 'kernel',
    "kernel": "ker:size",
    "kernel_init": np.ones((3, 3)),
    "kernel_size": 'odd:1:7:3'
}
dilate_params = {
    "function": ImageProcess.dilate,
    "params": 'kernel',
    "kernel": "ker"
}
erode_params = {
    "function": ImageProcess.erode,
    "params": 'kernel',
    "kernel": "ker"
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
