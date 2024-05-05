#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Digital Tools for Engineers in Physics.

Mini-Project: Illuminance Map

File Name: illuminance_map.py

This Python script serves as the main file for modeling and visualizing 3D lighting systems by calculating the illuminance distribution
on flat surfaces under the influence of various light sources.

It is part of the course project "Digital Tools for Engineers in Physics" and was developed by Marion Bonvarlet and Dorian Mendes.

Created on Thi Apr 11, 2024

@author:
    - Marion Bonvarlet
    - Dorian Mendes
"""

from system import System
from numpy import cos, sin, rad2deg
from numpy import pi as PI


def example_1() -> None:
    """
    First example.

    Returns
    -------
    None.

    """
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


def example_2() -> None:
    """
    Second example.

    Returns
    -------
    None.

    """
    # Create an instance of the System class
    syst = System()

    z0 = 3
    N = 10

    for k in range(N):
        syst.add_light_source(cos(2*PI*k/N), sin(2*PI*k/N), z0,
                              30, rad2deg(2*PI*k/N)+180, 100, 10)
    syst.add_light_source(0, 0, z0, 0, 0, 1000, 40)

    syst.add_surface([-1, 1], [-1, 0], [.1, .3, 1], [0, 0, 0], N_x=20, N_y=20)
    syst.add_surface([-1, 1], [0, 1], [-.1, -.3, 1],
                     [0, 0, .3], N_x=20, N_y=20)

    # Plot the light sources
    syst.plot_sources()

    # Plot the illuminance distribution
    syst.plot_illuminance()


def example_3() -> None:
    """
    Third example.

    Returns
    -------
    None.

    """
    # Create an instance of the System class
    syst = System()

    # Add light sources to the System class
    syst.add_light_source(x=-.5, y=-.5, z=2, elevation_angle=0,
                          azimuth_angle=45, intensity=100, beam_divergence_angle=10)
    syst.add_light_source(x=-.5, y=.5, z=2, elevation_angle=30,
                          azimuth_angle=-45, intensity=1000, beam_divergence_angle=5)
    syst.add_light_source(x=.5, y=-.5, z=2, elevation_angle=30,
                          azimuth_angle=45+90, intensity=800, beam_divergence_angle=50)
    syst.add_light_source(x=.5, y=.5, z=2, elevation_angle=0,
                          azimuth_angle=-45-90, intensity=100, beam_divergence_angle=10)

    # Add surfaces to the System class
    syst.add_surface([-1, 1], [-1, 1], [.1, .9, 1], [0, 0, 0])
    syst.add_surface([-1, 1], [.5, 1], [-.4, -1.9, 1], [0, 0, -1])

    # Plot the light sources
    syst.plot_sources()

    # Plot the illuminance distribution
    syst.plot_illuminance()


if __name__ == '__main__':
    # Create an instance of the System class
    syst = System()

    # Add light sources to the System class
    syst.add_light_source(x=0, y=0, z=1, elevation_angle=0,
                          azimuth_angle=0, intensity=100, beam_divergence_angle=10)

    # Add surfaces to the System class
    syst.add_surface([-1, 1], [-1, 1], [0,0,1], [0, 0, 0])

    # Plot the light sources
    syst.plot_sources()

    # Plot the illuminance distribution
    syst.plot_illuminance()