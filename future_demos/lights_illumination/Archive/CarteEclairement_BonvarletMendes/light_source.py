#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Outils Numériques pour l'Ingénieur.e en Physique.

Mini-Project: Illuminance Map
File Name: light_source.py

This file contains the implementation of the LightSource class, which represents a light source in a 3D lighting system.
The LightSource class provides functionality for modeling and visualizing 3D lighting systems by calculating the illuminance distribution
on flat surfaces under the influence of various light sources.

It is part of the course project "Outils Numériques pour l'Ingénieur.e en Physique" and was developed by Marion Bonvarlet and Dorian Mendes.

Created on Thi Apr 11, 2024

@author:
    - Marion Bonvarlet
    - Dorian Mendes
"""

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from numpy import sin, cos, deg2rad, rad2deg, exp, log
from auxiliary_functions import angle_between_two_vectors


class LightSource():
    """
    Represents a light source in the system.

    Attributes
    ----------
    instances : list
        List containing all instances of LightSource created.
    intensity_max : float
        Maximum intensity among all light sources.
    x, y, z : float
        Coordinates of the position of the light source.
    elevation_angle : float
        Angle in radians measured from the negative z-axis to the direction of the light.
    azimuth_angle : float
        Angle in radians measured from the x-axis in the xy-plane towards the y-axis, representing the azimuthal angle.
    intensity : float
        Maximum intensity of the light emitted by the source, given in candela.
    beam_divergence_angle : float
        Angle in degrees representing the divergence of the light beam.

    Methods
    -------
    __init__(self, x, y, z, elevation_angle, azimuth_angle, intensity, beam_divergence_angle)
        Initializes a LightSource object with the given parameters.

    get_light_direction(self) -> np.ndarray
        Returns the direction vector of the light emitted by the source.

    get_intensity(self, x_P, y_P, z_P) -> np.ndarray
        Calculates the intensity of light in the direction given by the point point due to the source.

    Notes
    -----
    - `elevation_angle` is measured in degrees and is given for the negative z-axis.
    - `azimuth_angle` is measured in degrees and is given for the xy-plane.

    """

    instances = []
    intensity_max = 0

    def __init__(self, x: float, y: float, z: float, elevation_angle: float, azimuth_angle: float, intensity: float, beam_divergence_angle: float) -> None:
        """
        Initialize a LightSource object with the given parameters.

        Parameters
        ----------
        x, y, z : float
            Coordinates of the position of the light source.
        elevation_angle : float
            Angle in degrees measured from the negative z-axis to the direction of the light.
        azimuth_angle : float
            Angle in degrees measured from the x-axis in the xy-plane towards the y-axis, representing the azimuthal angle.
        intensity : float
            Maximum intensity of the light emitted by the source, given in candela.
        beam_divergence_angle : float
            Angle in degrees representing the divergence of the light beam.

        Notes
        -----
        - `elevation_angle` is measured in degrees and is given for the negative z-axis.
        - `azimuth_angle` is measured in degrees and is given for the xy-plane.
        """
        # Add the newly created instance to 'instances'
        self.__class__.instances.append(self)

        # Initialize attributes
        self.x = x
        self.y = y
        self.z = z

        # Convert angles to radians
        self.elevation_angle = deg2rad(180 - elevation_angle)
        self.azimuth_angle = deg2rad(azimuth_angle)

        # Calculate light direction
        self.x_dir = sin(self.elevation_angle) * cos(self.azimuth_angle)
        self.y_dir = sin(self.elevation_angle) * sin(self.azimuth_angle)
        self.z_dir = cos(self.elevation_angle)

        #  Calculate intensity and update maximum intensity
        self.intensity = intensity
        self.__class__.intensity_max = max(
            self.__class__.intensity_max, self.intensity)

        # Angle of divergence of the light beam
        self.beam_divergence_angle = beam_divergence_angle

    def get_light_direction(self) -> np.ndarray:
        """
        Get the direction vector of the light emitted by the source.

        Returns
        -------
        ndarray
            Numpy array representing the direction vector of the emitted light.
        """
        return np.array([self.x_dir, self.y_dir, self.z_dir])

    def get_intensity(self, x_P: np.ndarray, y_P: np.ndarray, z_P: np.ndarray) -> np.ndarray:
        """
        Calculate the intensity of light in the direction given by the point point due to the source.

        Parameters
        ----------
        x_P, y_P, z_P : ndarray
            Coordinates of the point(s) where the intensity is calculated.

        Returns
        -------
        ndarray
            Returns the intensity of light in candela at the specified point(s).
        """
        angle_alpha = angle_between_two_vectors(
            x_P - self.x, y_P - self.y, z_P - self.z, self.x_dir, self.y_dir, self.z_dir)
        return self.intensity * exp(-4 * log(2) * (rad2deg(angle_alpha) / self.beam_divergence_angle)**2)


if __name__ == '__main__':
    # Define the first light source: at the origin of the coordinate system, altitude of 1.50m, oriented towards the center of the Earth, with nominal intensity of 100 lux and divergence of 60°
    source1 = LightSource(x=0, y=0, z=1.5, elevation_angle=0,
                          azimuth_angle=0, intensity=100, beam_divergence_angle=60)

    # Set up the first subplot
    ax1 = plt.figure(
        num="LightSource test - Source 1").add_subplot(projection='3d')

    # Configure plot labels and limits
    ax1.view_init(30, 30)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_xlim(-1, 1)
    ax1.set_ylim(-1, 1)
    ax1.set_zlim(0, 2)

    # Plot the position and direction of the first light source
    ax1.scatter(source1.x, source1.y, source1.z, color='blue')
    ax1.quiver(source1.x, source1.y, source1.z, *
               source1.get_light_direction(), color='blue')

    # Generate grid points for the illuminance map
    x = np.linspace(*ax1.get_xlim())
    y = np.linspace(*ax1.get_ylim())
    xx, yy = np.meshgrid(x, y)
    zz_00cm = 0*np.ones_like(xx)
    zz_50cm = .5*np.ones_like(xx)

    # Calculate intensities at different heights for the first light source
    intensity_z_00cm = source1.get_intensity(xx, yy, zz_00cm)
    intensity_z_50cm = source1.get_intensity(xx, yy, zz_50cm)
    intensity_z_max = max(intensity_z_00cm.max(), intensity_z_50cm.max())

    # Plot the surfaces representing illuminance at different heights for the first light source
    ax1.plot_surface(xx, yy, zz_00cm, facecolors=cm.Oranges(
        intensity_z_00cm/intensity_z_max), edgecolor='none', rstride=1, cstride=1, alpha=.7)
    ax1.plot_surface(xx, yy, zz_50cm, facecolors=cm.Oranges(
        intensity_z_50cm/intensity_z_max), edgecolor='none', rstride=1, cstride=1, alpha=.7)

    # Create a color bar for the first subplot
    sm = cm.ScalarMappable(cmap=cm.Oranges, norm=plt.Normalize(
        vmin=0, vmax=intensity_z_max))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax1, orientation='vertical')
    cbar.set_label('Intensity (lux)')

    # Show the first subplot
    plt.show()

    # Define the second light source: at (-.5, .7, 1.5), oriented with theta=20° and phi=45°, with nominal intensity of 1000 lux and divergence of 10°
    source2 = LightSource(x=-.5, y=.7, z=1.5, elevation_angle=20,
                          azimuth_angle=45, intensity=1000, beam_divergence_angle=10)

    # Set up the second subplot
    ax2 = plt.figure(
        num="LightSource test - Source 2").add_subplot(projection='3d')

    # Configure plot labels and limits for the second subplot
    ax2.view_init(30, 30)
    ax2.set_xlabel('X (m)')
    ax2.set_ylabel('Y (m)')
    ax2.set_zlabel('Z (m)')
    ax2.set_xlim(-.8, .25)
    ax2.set_ylim(.4, 1.5)
    ax2.set_zlim(0, 2)

    # Plot the position and direction of the second light source
    ax2.scatter(source2.x, source2.y, source2.z, color='blue')
    ax2.quiver(source2.x, source2.y, source2.z, *
               source2.get_light_direction(), color='blue')

    # Generate grid points for the illuminance map
    x = np.linspace(*ax2.get_xlim())
    y = np.linspace(*ax2.get_ylim())
    xx, yy = np.meshgrid(x, y)
    zz_00cm = 0*np.ones_like(xx)
    zz_50cm = .5*np.ones_like(xx)

    # Calculate intensities at different heights for the second light source
    intensity_z_00cm = source2.get_intensity(xx, yy, zz_00cm)
    intensity_z_50cm = source2.get_intensity(xx, yy, zz_50cm)
    intensity_z_max = max(intensity_z_00cm.max(), intensity_z_50cm.max())

    # Plot the surfaces representing illuminance at different heights for the second light source
    ax2.plot_surface(xx, yy, zz_00cm, facecolors=cm.Oranges(
        intensity_z_00cm/intensity_z_max), edgecolor='none', rstride=1, cstride=1, alpha=.7)
    ax2.plot_surface(xx, yy, zz_50cm, facecolors=cm.Oranges(
        intensity_z_50cm/intensity_z_max), edgecolor='none', rstride=1, cstride=1, alpha=.7)

    # Create a color bar for the second subplot
    sm = cm.ScalarMappable(cmap=cm.Oranges, norm=plt.Normalize(
        vmin=0, vmax=intensity_z_max))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax2, orientation='vertical')
    cbar.set_label('Intensity (lux)')

    # Show the second subplot
    plt.show()
