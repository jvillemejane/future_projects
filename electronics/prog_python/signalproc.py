#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LEnsE.tech Ressources and Training / Institut d'Optique

Signal library for Electronics modeling and simulation.

@see : https://iogs-lense.github.io/lense.tech/

Created on 08/Sep/2024

.. note:: LEnsE - Institut d'Optique - version 1.0

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
"""

import numpy as np

def lintime(start, stop, sampling_period):
    return np.arange(start, stop, sampling_period)

def sine_wave(time, frequency, amplitude=1, phase=0, offset=0):
    return offset+amplitude*np.sin(2*np.pi*frequency*time + phase)

def saturation(signal, max_value, min_value=None):
    if min_value is None:
        min_value = -max_value
    signal[signal > max_value] = max_value
    signal[signal < min_value] = min_value
    return signal

def noise_gauss(sigma, num_samples):
    # https://www.mycompiler.io/view/GlAtZMvbhob
    return np.random.normal(0, sigma, num_samples)

if __name__ == "__main__":
    from matplotlib import pyplot as plt
    ## Simulation parameters
    sampling_frequency = 100e3
    sampling_period = 1 / sampling_frequency
    simulation_duration = 0.05
    time = lintime(0, simulation_duration, sampling_period)

    sine_signal = sine_wave(time, 203, amplitude=15, offset=5, phase=-1)
    noise = noise_gauss(0.3, len(sine_signal))
    sine_signal += noise
    sine_signal_sat = saturation(sine_signal, 13)

    ## Display
    fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
    ax.plot(time, sine_signal_sat, label='signal', color='blue', linewidth=2)
    ax.set_title('Signal', fontsize=16)
    ax.set_xlabel('Time (s)', fontsize=14)
    ax.set_ylabel('Signal (V)', fontsize=14)
    #ax.grid(True)
    #ax.legend(fontsize=12)
    ax.tick_params(axis='both', which='major', labelsize=12)
    #plt.tight_layout()  # Adjust layout to avoid overlap
    plt.show()