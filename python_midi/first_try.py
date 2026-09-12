# MIDO package - First test

import mido

# Find MIDI devices (USB)
print(mido.get_input_names())
print(mido.get_output_names())

# Sending note
out = mido.open_output('Launchpad Pro MIDI Out')

msg = mido.Message('note_on', note=60, velocity=127, channel=0)
out.send(msg)
# Cut the LED of Launchpad Pro
out.send(mido.Message('note_off', note=60, velocity=0, channel=0))