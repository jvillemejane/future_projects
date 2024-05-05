# -*- coding: utf-8 -*-
"""*point* file.

*point* file that contains :class::Point. This class modelize a point in a 3D space.

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""

import numpy as np

class Point:
    def __init__(self, x=0, y=0, z=0):
        '''

        :param x:  float, x-axis coordinate of the point 
        :param y:  float, y-axis coordinate of the point 
        :param z:  float, z-axis coordinate of the point 
        '''
        self.x = x
        self.y = y
        self.z = z
        
