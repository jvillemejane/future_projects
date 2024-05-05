# -*- coding: utf-8 -*-
"""*vector* file.

*vector* file that contains :class::Vector. This class modelize a vector in a 3D space.

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""

import numpy as np

class Vector:
    def __init__(self, u_x: float=0, u_y: float=0, u_z: float=1):
        '''

        :param u_x:  float, x-axis coordinate of the vector 
        :param u_y:  float, y-axis coordinate of the vector 
        :param u_z:  float, z-axis coordinate of the vector 
        '''
        self.u_x = u_x
        self.u_y = u_y
        self.u_z = u_z
       
    def get_norm(self) -> float:
        '''Return the norm of the vector.
        
        :return: float, norm of the vector
        '''
        return np.sqrt(self.u_x**2 + self.u_y**2 + self.u_z**2)
        
    def angle_with_vector(self, vect) -> float:
        """
        Calculate the angle between two vectors using the dot product definition.

        :param vect:  Vector, vector for angle calculation
        :return: float, angle (in radian)

        Notes
        -----
        The angle between two vectors can be calculated using the dot product formula:
            angle = arccos((u.v) / (||u|| ||v||))
        where u.v is the dot product of vectors u and v, and ||u|| and ||v|| are the magnitudes of vectors u and v respectively.
        """
        norm_u = self.get_norm()
        norm_v = vect.get_norm()
        dot_product = self.u_x*vect.u_x + self.u_y*vect.u_y + self.u_y*vect.u_y
        return np.arccos(dot_product/norm_u/norm_v)
        
if __name__ == '__main__':
    vect1 = Vector(1,0,0)
    vect2 = Vector(0,0,1)
    angle_1_2 = vect1.angle_with_vector(vect2)
    
    print(f"{angle_1_2} rad, {np.rad2deg(angle_1_2)} deg")