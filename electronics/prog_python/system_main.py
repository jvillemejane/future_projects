#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LEnsE.tech Ressources and Training / Institut d'Optique

System characterization and modeling. Main program.

@see : https://iogs-lense.github.io/lense.tech/

Created on 08/Sep/2024

.. note:: LEnsE - Institut d'Optique - version 1.0

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

see : https://www.youtube.com/watch?v=rlSXT3MOcSk
"""

import numpy as np
import control as ctl
from matplotlib import pyplot as plt

# System paremeters
K0 = 10
m = 1
w0 = 1e3

time_vect = np.linspace(0, 0.01, 1001)

system_num = [K0]
system_den = [1/(w0*w0), 2*m/w0, 1]

system1 = ctl.tf(system_num, system_den)
print(system1)

t1, y1 = ctl.step_response(system1, time_vect)
t1, y1 = ctl.impulse_response(system1, time_vect)

fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
ax.plot(t1, y1, label='signal', color='blue', linewidth=2)
ax.set_title('Signal', fontsize=16)
ax.set_xlabel('Time (s)', fontsize=14)
ax.set_ylabel('Signal (V)', fontsize=14)
ax.grid(True)
# ax.legend(fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)
# plt.tight_layout()  # Adjust layout to avoid overlap
plt.show()