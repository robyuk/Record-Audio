#! /usr/bin/env /usr/bin/python3
#
# This python script records audio
#
# DOES NOT WORK in Replit. Pull using git at https://github.com/robyuk/Record-Audio to a PC with a michrophone

# pip install sounddevice
# pip install scipy

import sounddevice
from scipy.io.wavfile import write

outfile='recording.mp3'
seconds=5
samplerate=44100

# myrecording is a numpy array containing values at the sample times.  number of rows in the array is samplerate*seconds, and as we have channels=1, the array has 1 column
myrecording=sounddevice.rec(frames=seconds*samplerate, samplerate=samplerate, channels=1)
sounddevice.wait()  # Wait for the recording to complete (otherwise recording happens in the background)
write(outfile,samplerate,myrecording)