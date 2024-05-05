#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Outils Numériques pour l'Ingénieur.e en Physique.

Mini-Project: Illuminance Map
File Name: system.py

This file contains the implementation of the System class, which represents a system of light sources and surfaces in a 3D space.
The System class provides functionality for modeling and visualizing 3D lighting systems by calculating the illuminance distribution on flat surfaces under the influence of various light sources.

It is part of the course project "Outils Numériques pour l'Ingénieur.e en Physique" and was developed by Marion Bonvarlet and Dorian Mendes.

Created on Thi Apr 11, 2024

@author:
    - Marion Bonvarlet
    - Dorian Mendes
"""

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import numpy as np

from auxiliary_functions import angle_between_two_vectors
from light_source import LightSource
from plane import Plane


class System():
    """
    Represents a system of light sources and surfaces in 3D space.

    Attributes
    ----------
    ax : Axes3D
        The 3D axes object for visualization.
    x_min, x_max : float
        Minimum and maximum values of the x-coordinate defining the boundaries of the system.
    y_min, y_max : float
        Minimum and maximum values of the y-coordinate defining the boundaries of the system.
    z_min, z_max : float
        Minimum and maximum values of the z-coordinate defining the boundaries of the system.
    irradiance_cmap : LinearSegmentedColormap
        Custom colormap for visualizing irradiance.

    Methods
    -------
    __init__(self)
        Initializes a System object with an empty list of light sources and plans.

    add_light_source(self, x, y, z, elevation_angle, azimuth_angle, intensity, beam_divergence_angle)
        Adds a new light source to the system with the specified parameters.

    add_surface(self, x_lim, y_lim, normal_vector, point_in_plan, N_x=50, N_y=50)
        Adds a new plane to the system with the specified parameters.

    update_boundaries(self, x, y, z)
        Updates the boundaries of the system based on the given coordinates.

    plot_sources(self)
        Plots the light sources in the system on the 3D axes.

    plot_illuminance(self)
        Plots the irradiance distribution in the system on the 3D axes.
    """

    def __init__(self) -> None:
        """
        Initialize a System object with an empty list of light sources and plans.

        Attributes
        ----------
        ax : Axes3D
            The 3D axes object for visualization.
        x_min, x_max : float
            Minimum and maximum values of the x-coordinate defining the boundaries of the system.
        y_min, y_max : float
            Minimum and maximum values of the y-coordinate defining the boundaries of the system.
        z_min, z_max : float
            Minimum and maximum values of the z-coordinate defining the boundaries of the system.
        irradiance_cmap : LinearSegmentedColormap
            Custom colormap for visualizing irradiance.
        """
        # Initialize 3D axes object
        self.ax = plt.figure(
            num="Illuminance map").add_subplot(projection='3d')
        self.ax.view_init(30, 30)
        self.ax.set_xlabel('X (m)')
        self.ax.set_ylabel('Y (m)')
        self.ax.set_zlabel('Z (m)')

        # Initialize boundaries
        self.x_min = np.inf
        self.y_min = np.inf
        self.z_min = 0
        self.x_max = -np.inf
        self.y_max = -np.inf
        self.z_max = -np.inf

        # Custom colormap for visualizing irradiance
        self.irradiance_cmap = mcolors.LinearSegmentedColormap.from_list(
            'lamp_light', [(0, 0, 0), (1, 1, 0.8)], N=256)

    def add_light_source(self, x: float, y: float, z: float, elevation_angle: float, azimuth_angle: float, intensity: float, beam_divergence_angle: float) -> None:
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
        # Create a new LightSource instance
        LightSource(x, y, z, elevation_angle, azimuth_angle,
                    intensity, beam_divergence_angle)

    def add_surface(self, x_lim: list, y_lim: list, normal_vector: list, point_in_plan: list, N_x=50, N_y=50) -> None:
        """
        Add a planar surface to the system with the given parameters.

        Parameters
        ----------
        x_lim : list
            List containing the minimum and maximum values of the x-coordinate defining the boundaries of the plane.
        y_lim : list
            List containing the minimum and maximum values of the y-coordinate defining the boundaries of the plane.
        normal_vector : list
            List containing the coefficients of the normal vector to the plane's surface equation.
            The plane should not be vertical (a wall), so the coefficient c must not be 0.
        point_in_plan : list
            List containing the coordinates of a point that lies on the plane's surface.
        N_x : int, optional
            Number of points along the x-axis for the meshgrid. Default is 50.
        N_y : int, optional
            Number of points along the y-axis for the meshgrid. Default is 50.
        """
        # Create a new plane instance
        Plane(x_lim, y_lim, normal_vector, point_in_plan, N_x, N_y)

    def update_boundaries(self, x: float, y: float, z: float) -> None:
        """
        Update the boundaries of the 3D plot based on the coordinates of a point.

        Parameters
        ----------
        x, y, z : float
            Coordinate of the point.
        """
        # Update the boundaries of the system
        self.x_min = min(self.x_min, x)
        self.y_min = min(self.y_min, y)
        self.z_min = min(self.z_min, z)
        self.x_max = max(self.x_max, x)
        self.y_max = max(self.y_max, y)
        self.z_max = max(self.z_max, z)

        # Set the limits of the axes
        self.ax.set_xlim(self.x_min, self.x_max)
        self.ax.set_ylim(self.y_min, self.y_max)
        self.ax.set_zlim(self.z_min, self.z_max)

    def plot_sources(self) -> None:
        """
        Plot the light sources as cones in the 3D space.

        This method represents the light sources as cones in the 3D space, taking into account their positions, directions, and divergence angles.
        The color of the cones corresponds to the intensity (intensity) of each source.

        Notes
        -----
        The cones representing the light sources are oriented according to the direction of emitted light, and their color is determined by the intensity (intensity) of each source.
        """
        # Plot light sources as cones
        for light in LightSource.instances:
            self.update_boundaries(light.x, light.y, light.z)

            # Function to generate rotation matrix for rotating a vector around a specified axis by a given angle
            def rotate_vector(u: np.ndarray, angle: float) -> np.ndarray:
                """
                Generate the rotation matrix for rotating a vector around a specified axis by a given angle.

                Parameters
                ----------
                u : ndarray
                    3D vector representing the axis of rotation.
                angle : float
                    Angle in radians for the rotation.

                Returns
                -------
                ndarray
                    Rotation matrix corresponding to the specified rotation around the given axis.
                """
                K = np.array([
                    [0, -u[2], u[1]],
                    [u[2], 0, -u[0]],
                    [-u[1], u[0], 0]
                ])
                identity_matrix = np.identity(3)

                return identity_matrix + np.sin(angle) * K + (1 - np.cos(angle)) * np.dot(K, K)

            # Function to generate basis change matrix for rotating vectors from the standard basis to a new basis defined by angles elevation_angle and azimuth_angle
            def generate_basis_change_matrix(elevation_angle: float, azimuth_angle: float) -> np.ndarray:
                """
                Generate the basis change matrix for rotating vectors from the standard basis to a new basis defined by angles elevation_angle and azimuth_angle.

                Parameters
                ----------
                elevation_angle : float
                    Angle in radians for the rotation around the y-axis.
                azimuth_angle : float
                    Angle in radians for the rotation around the z-axis.

                Returns
                -------
                ndarray
                    Basis change matrix for the specified rotation angles elevation_angle and azimuth_angle.
                """
                R1 = rotate_vector([0, 0, 1], azimuth_angle)
                R2 = rotate_vector(
                    [-np.sin(azimuth_angle), np.cos(azimuth_angle), 0], elevation_angle)
                return R2.dot(R1)

            r = np.sin(np.deg2rad(light.beam_divergence_angle))
            elevation_angle = np.linspace(0, 2 * np.pi, 50)
            z = np.linspace(0, -1/2, 50)
            elevation_angle, Z = np.meshgrid(elevation_angle, z)
            X = r * Z * np.cos(elevation_angle)
            Y = r * Z * np.sin(elevation_angle)
            Z = Z

            rot_mat = generate_basis_change_matrix(
                -(np.pi-light.elevation_angle), (light.azimuth_angle))

            X, Y, Z = rot_mat[0, 0]*X+rot_mat[0, 1]*Y+rot_mat[0, 2]*Z, \
                rot_mat[1, 0]*X+rot_mat[1, 1]*Y+rot_mat[1, 2]*Z, \
                rot_mat[2, 0]*X+rot_mat[2, 1]*Y+rot_mat[2, 2]*Z

            self.ax.plot_surface(X + light.x, Y + light.y, Z + light.z, alpha=0.75,
                                 color=cm.Wistia(light.intensity/LightSource.intensity_max))

        # Create a ScalarMappable instance specific to intensity
        sm_intensity = cm.ScalarMappable(cmap=cm.Wistia, norm=plt.Normalize(
            vmin=0, vmax=LightSource.intensity_max))
        sm_intensity.set_array([])

        # Add a colorbar linked to the ScalarMappable instance specific to intensity
        cbar_intensity = plt.colorbar(
            sm_intensity, ax=self.ax, orientation='vertical', shrink=0.5)
        cbar_intensity.set_label('Source intensity (lux)')

        # Remove unnecessary data from the ScalarMappable instance specific to intensity to avoid warnings
        sm_intensity.set_array(None)

        # self.ax.scatter(light.x, light.y, light.z, color='blue')
        # self.ax.quiver(light.x, light.y, light.z, light.x_dir, light.y_dir, light.z_dir, color='blue')

    def plot_illuminance(self) -> None:
        """
        Plot the irradiance distribution over the defined surfaces in the system.

        Calculates and visualizes the irradiance distribution over the surfaces defined in the system,
        taking into account the illumination from all light sources.

        Notes
        -----
        The irradiance distribution is visualized using a color map, where different colors represent
        different irradiance values, with higher irradiance indicated by warmer colors.

        """
        max_irradiance = 0

        # Calculer la valeur maximale de l'irradiance parmi toutes les surfaces
        for plane in Plane.instances:
            self.update_boundaries(plane.x.min(), plane.y.min(), plane.z.min())
            self.update_boundaries(plane.x.max(), plane.y.max(), plane.z.max())

            E = np.zeros_like(plane.x)

            for light in LightSource.instances:
                angle_psi = angle_between_two_vectors(
                    plane.a, plane.b, plane.c, light.x-plane.x, light.y-plane.y, light.z-plane.z)
                d_PS_2 = (light.x - plane.x)**2 + (light.y -
                                                   plane.y)**2 + (light.z - plane.z)**2
                E += light.get_intensity(plane.x, plane.y,
                                         plane.z) * np.cos(angle_psi) / d_PS_2
            max_irradiance = max(max_irradiance, np.max(E))

        # Tracer les surfaces avec une échelle de couleur normalisée
        for plane in Plane.instances:
            E = np.zeros_like(plane.x)

            for light in LightSource.instances:
                angle_psi = angle_between_two_vectors(
                    plane.a, plane.b, plane.c, light.x-plane.x, light.y-plane.y, light.z-plane.z)
                d_PS_2 = (light.x - plane.x)**2 + (light.y -
                                                   plane.y)**2 + (light.z - plane.z)**2
                E += light.get_intensity(plane.x, plane.y,
                                         plane.z) * np.cos(angle_psi) / d_PS_2

            # Tracer la surface avec l'échelle de couleur normalisée
            self.ax.plot_surface(
                plane.x, plane.y, plane.z, facecolors=self.irradiance_cmap(E/max_irradiance), edgecolor='none', rstride=1, cstride=1)

        # Créer une instance de ScalarMappable avec la colormap personnalisée et la valeur maximale de l'éclairement
        sm = cm.ScalarMappable(cmap=self.irradiance_cmap,
                               norm=plt.Normalize(vmin=0, vmax=max_irradiance))
        sm.set_array([])

        # Ajouter une colorbar liée à l'instance ScalarMappable
        cbar = plt.colorbar(sm, ax=self.ax, orientation='vertical')
        cbar.set_label('Illumiance (candela)')

        # Assurer un aspect orthonormé dans l'espace 3D
        self.ax.set_box_aspect([np.ptp([self.x_min, self.x_max]), np.ptp(
            [self.y_min, self.y_max]), np.ptp([self.z_min, self.z_max])])
        plt.show()


if __name__ == '__main__':
    # Create an instance of the System class
    syst = System()

    # Add light sources to the System class
    syst.add_light_source(x=-.5, y=-.5, z=2, elevation_angle=30,
                          azimuth_angle=45, intensity=100, beam_divergence_angle=10)
    syst.add_light_source(x=-.5, y=.5, z=2, elevation_angle=30,
                          azimuth_angle=-45, intensity=100, beam_divergence_angle=10)
    syst.add_light_source(x=.5, y=-.5, z=2, elevation_angle=30,
                          azimuth_angle=45+90, intensity=100, beam_divergence_angle=10)
    syst.add_light_source(x=.5, y=.5, z=2, elevation_angle=30,
                          azimuth_angle=-45-90, intensity=100, beam_divergence_angle=10)

    # Add surfaces to the System class
    syst.add_surface([-1, 1], [-1, 1], [.1, .3, 1], [0, 0, 0])
    syst.add_surface([-1, 1], [-1, 1], [0, 0, 1], [0, 0, .5])

    # Plot the light sources
    syst.plot_sources()

    # Plot the illuminance distribution
    syst.plot_illuminance()
