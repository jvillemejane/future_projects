# MIDO package - First test

import mido
from mido import Message
import time

def all_black(midi_out):
    for k in range(128):
        msg = mido.Message('note_off', note=k, velocity=0, channel=0)
        midi_out.send(msg)

# Find MIDI devices (USB)
print('MIDI Inputs')
inputs = mido.get_input_names()
for k, midi_in in enumerate(inputs):
    print(f'({k+1}) {midi_in}')
input_select = inputs[int(input('Select Midi input')) - 1]

print('MIDI Outputs')
outputs = mido.get_output_names()
for k, midi_out in enumerate(outputs):
    print(f'({k+1}) {midi_out}')
output_select = outputs[int(input('Select Midi output')) - 1]


midi_out = mido.open_output(output_select)
midi_in = mido.open_input(input_select)


if input_select is not None and output_select is not None :
    print('Test MIDI')
        
    all_black(midi_out)
        
    # Sending note
    for k in range(128):
        msg = mido.Message('note_on', note=k, velocity=k, channel=0)
        midi_out.send(msg)
        time.sleep(0.01)
        
## LISTENING MIDI IN
with midi_in as port:
    print(f"Écoute de : {midi_in}")

    for msg in port:
        print(msg)
        
        if msg.type == "control_change":
            if msg.control == 98:  # User keys
                break

all_black(midi_out)