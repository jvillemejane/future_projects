# -*- coding: utf-8 -*-
"""Test lecture son et cumul plusieurs sons avec Pygame."""

import pygame
import numpy as np

# Pygame init
pygame.init()

# Load wav files - Must have the same sampling frequency - Default 44100 Hz
soundB6 = pygame.mixer.Sound('b6.wav')
soundG6 = pygame.mixer.Sound('g6.wav')
soundC3 = pygame.mixer.Sound('c3.wav')

# Store data as array - 
soundB6_data = pygame.sndarray.array(soundB6).astype(np.int16)
soundG6_data = pygame.sndarray.array(soundG6).astype(np.int16)
soundC3_data = pygame.sndarray.array(soundC3).astype(np.int16)
print(type(soundC3_data[0][0]))

# Find min size of arrays
sizeB6 = soundB6_data.shape[0]
sizeG6 = soundG6_data.shape[0]
sizeC3 = soundC3_data.shape[0]

sizeAll = min(sizeB6, sizeG6, sizeC3)

output_sound = np.zeros((sizeAll-1, 2), dtype=np.int16)

output_sound += soundB6_data[0:sizeAll-1] // 2
output_sound += soundG6_data[0:sizeAll-1] // 2

output_sound = output_sound
print(type(output_sound[0][0]))

# Sound object from array
final_sound = pygame.sndarray.make_sound(output_sound)
final_sound.play()

# Wait end of the sound
pygame.time.wait(int(final_sound.get_length() * 1000))