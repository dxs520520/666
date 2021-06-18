# -*- coding: utf-8 -*-
from thinkdsp import decorate
from thinkdsp import SquareSignal
import matplotlib.pyplot as plt
signal = SquareSignal(1100)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(1,2,1)
segment.plot()
decorate(xlabel='Time (s)')
wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()
spectrum = wave.make_spectrum()
plt.subplot(1,2,2)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
plt.show()