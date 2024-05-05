# -*- coding: utf-8 -*-
"""*point_source* file.

*point_source* file that contains :class::PointSource. This class modelize a point source in a 3D space.
Point source is described by its 3D coordonates, its radiant intensity and its angle of half intensity.

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""

from matplotlib import pyplot as plt
import numpy as np
from point import Point
from vector import Vector

class PointSource:
    def __init__(self, I0, delta, position=Point(0,0,0), theta=0, zeta=0):
        '''

        :param I0:  float, maximal light intensity 
        :param delta:   float, half-angle of emission (in degree)
        :param position: Point, position in a 3D environment (in meter)
        :param theta:   float, position angle of emission (in degree)
        :param zeta:   float, position angle of emission (in degree)
        '''
        self.I0 = I0
        self.delta_deg = delta
        self.delta = self.delta_deg*np.pi / 180

        self.position = position
        self.theta, self.zeta = np.radians(theta), np.radians(zeta+90)
        # definition of ux, uy, uz = unitary vector of the main source direction
        self.direction_vector = Vector(np.cos(self.theta)*np.cos(self.zeta), np.sin(self.theta)*np.cos(self.zeta), -np.sin(self.zeta))

    def __str__(self):
        out_str = f'LED (I0={self.I0} / delta={self.delta_deg})'
        return out_str

    def led_intensity(self, angle: float):
        """
        indicatrice de rayonnement
        :param angle:   float, angle (in radian)
        :return:
            value of the light intensity in the specific angle
        """
        return self.I0*np.exp(-(4*np.log(2))*(angle / self.delta)**2)

    def led_illumination(self, distance: float, angle: float):
        """

        :param distance:    float, distance (in meter) between light source and the point of view (in meters)
        :param angle:   float, angle (in radian) between normal vector of the light source and the point of view (in degrees)
        :return:
            illumination value at a specific distance and angle

        help from : https://fr.wikibooks.org/wiki/Photographie/Photom%C3%A9trie/Calculs_photom%C3%A9triques_usuels
        """
        angle_new = angle * np.pi / 180
        return self.led_intensity(angle) * np.cos(angle_new) / (distance**2)

    def get_coords(self):
        return self.position.x, self.position.y, self.position.z

    def get_params(self):
        return self.I0, self.zeta, self.theta

    def get_direction_vector(self):
        return self.direction_vector.ux, self.direction_vector.uy, self.direction_vector.uz

    def get_radiation_from_angle(self, alpha=None):
        if alpha is None:
            alpha = np.linspace(0, np.pi, 101)
        led_intens = self.led_intensity(alpha)
        return led_intens


if __name__ == "__main__":
    led1 = PointSource(1, 80)
    led2 = PointSource(2, 40)
    
    alpha = np.linspace(0,np.pi, 101)
    led1_int = led1.get_radiation_from_angle(alpha)
    led2_int = led2.get_radiation_from_angle(alpha)
    
    plt.figure()
    plt.polar(alpha, led1_int, label=f'{led1}')
    plt.polar(alpha, led2_int, label=f'{led2}')
    plt.legend()
    
    plt.figure()
    plt.plot(alpha*180/np.pi, led1_int, label=f'{led1}')
    plt.plot(alpha*180/np.pi, led2_int, label=f'{led2}')
    plt.legend()
    plt.show()
    
    