# coding=utf-8

import wave
import numpy as np
import sys

### define the params of wave
time = sys.argv[1]
samplerate = sys.argv[2]
file_name = sys.argv[3]
channels = 1
sampwidth = 2       ### 16bits
framerate = int(samplerate)   

wave_data = np.zeros(int(time)*int(samplerate))

### generate a wav
f = wave.open(file_name,"wb")
f.setnchannels(channels)
f.setsampwidth(sampwidth)
f.setframerate(framerate)
f.writeframes(wave_data.tostring())
f.close()


