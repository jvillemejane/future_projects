#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Digital Tools for Physicists.

Mini-Project: Illuminance Map
File Name: plane.py

This file contains the implementation of the Plane class, which represents a plane in a 3D space.
The Plane class provides functionality for modeling and visualizing planes in 3D space.

It is part of the course project "Digital Tools for Physicists" and was developed by Marion Bonvarlet and Dorian Mendes.

Created on Thu Apr 11, 2024

@author:
    - Marion Bonvarlet
    - Dorian Mendes
"""

import matplotlib.pyplot as plt
import numpy as np


class Plane():
    """
    Represents a plane in 3D space.

    Attributes
    ----------
    instances : list
        List containing all instances of planes created.
    x_min, y_min, z_min : float
        Minimum values of the x, y, and z-coordinates defining the boundaries of the plane.
    x_max, y_max, z_max : float
        Maximum values of the x, y, and z-coordinates defining the boundaries of the plane.
    x : ndarray
        Meshgrid array containing x-coordinates of points in the plane.
    y : ndarray
        Meshgrid array containing y-coordinates of points in the plane.
    z : ndarray
        Array containing z-coordinates of points in the plane, calculated based on the plane equation.

    Methods
    -------
    __init__(self, x_lim, y_lim, normal_vector, point_in_plane, N_x, N_y)
        Initializes a plane object with the given parameters.

    Notes
    -----
    The plane should not be vertical (a wall), so the coefficient c in the normal vector must not be 0.
    """

    instances = []

    def __init__(self, x_lim: list, y_lim: list, normal_vector: list, point_in_plane: list, N_x: int, N_y: int) -> None:
        """
        Initialize a plane object with the given parameters.

        Parameters
        ----------
        x_lim : list
            List containing the minimum and maximum values of the x-coordinate defining the boundaries of the plane.
        y_lim : list
            List containing the minimum and maximum values of the y-coordinate defining the boundaries of the plane.
        normal_vector : list
            List containing the coefficients of the normal vector to the plane's surface equation.
            The plane should not be vertical (a wall), so the coefficient c must not be 0.
        point_in_plane : list
            List containing the coordinates of a point that lies on the plane's surface.
        N_x : int
            Number of points along the x-axis for the meshgrid.
        N_y : int
            Number of points along the y-axis for the meshgrid.
        """
        x_min, x_max = x_lim
        y_min, y_max = y_lim
        a, b, c = normal_vector
        x0, y0, z0 = point_in_plane

        if c == 0:
            raise ValueError(
                "The plane should not be vertical (a wall). The coefficient 'c' in the normal vector must not be 0.")

        # Add the newly created instance to 'instances'
        self.__class__.instances.append(self)

        # Initialize attributes
        self.x_min, self.x_max = x_min, x_max
        self.y_min, self.y_max = y_min, y_max
        self.a, self.b, self.c = a, b, c

        # Create meshgrid for x and y coordinates
        x = np.linspace(self.x_min, self.x_max, N_x)
        y = np.linspace(self.y_min, self.y_max, N_y)
        self.x, self.y = np.meshgrid(x, y)

        # Calculate z-coordinates based on the plane equation
        self.z = self.a/self.c*(x0-self.x) + self.b/self.c*(y0-self.y) + z0


if __name__ == '__main__':
    ax = plt.figure(num="Plane test").add_subplot(projection='3d')

    # Configure plot labels and limits
    ax.view_init(30, 30)
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(0, 2)

    # Define plane parameters for visualization
    point1 = [0, 0, 0]
    normal_vector1 = [0, 0, 1]  # Normal vector perpendicular to the plane
    plane1 = Plane(x_lim=[-1, 1], y_lim=[-1, 1],
                   normal_vector=normal_vector1, point_in_plane=point1, N_x=50, N_y=50)
    ax.plot_surface(plane1.x, plane1.y, plane1.z, color='blue')
    ax.scatter(*point1, color='blue')
    ax.quiver(*point1, *normal_vector1, color='blue')

    # Define another plane for visualization
    point2 = [-.5, -.5, .5]
    normal_vector2 = [-.2, .3, 1]
    plane2 = Plane(x_lim=[-2, 0], y_lim=[-2, 0],
                   normal_vector=normal_vector2, point_in_plane=point2, N_x=50, N_y=50)
    ax.plot_surface(plane2.x, plane2.y, plane2.z, color='orange')
    ax.scatter(*point2, color='orange')
    ax.quiver(*point2, *normal_vector2, color='orange')

    plt.show()
