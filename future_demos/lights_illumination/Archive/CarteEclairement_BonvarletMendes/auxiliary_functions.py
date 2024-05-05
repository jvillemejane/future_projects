#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Outils Numériques pour l'Ingénieur.e en Physique.

Mini-Project: Illuminance Map
File Name: auxiliary_functions.py

This file contains auxiliary functions for various mathematical calculations.

These functions serve various purposes such as vector operations, mathematical computations, etc., and are utilized in the broader context of the mini-project "Illuminance Map."

This Python script allows modeling and visualizing 3D lighting systems by calculating the illuminance distribution
on flat surfaces under the influence of various light sources.

It is part of the course project "Outils Numériques pour l'Ingénieur.e en Physique" and was developed by Marion Bonvarlet and Dorian Mendes.

Created on Thi Apr 11, 2024

@author:
    - Marion Bonvarlet
    - Dorian Mendes
"""

from numpy import sqrt, arccos, rad2deg


def angle_between_two_vectors(u_x: float, u_y: float, u_z: float, v_x: float, v_y: float, v_z: float) -> float:
    """
    Calculate the angle between two vectors using the dot product definition.

    Parameters
    ----------
    u_x, u_y, u_z : float or ndarray
        Coordinates of the first vector.
    v_x, v_y, v_z : float or ndarray
        Coordinates of the second vector.

    Returns
    -------
    float or ndarray
        Returns the angle in radians.

    Notes
    -----
    The angle between two vectors can be calculated using the dot product formula:
        angle = arccos((u.v) / (||u|| ||v||))
    where u.v is the dot product of vectors u and v, and ||u|| and ||v|| are the magnitudes of vectors u and v respectively.
    """
    norm_u = sqrt(u_x**2+u_y**2+u_z**2)
    norm_v = sqrt(v_x**2+v_y**2+v_z**2)
    dot_product = u_x*v_x + u_y*v_y + u_z*v_z
    return arccos(dot_product/norm_u/norm_v)


if __name__ == '__main__':
    print(f"{angle_between_two_vectors(1,0,0,0,0,1)} rad, {rad2deg(angle_between_two_vectors(1,0,0,0,0,1))} deg")
