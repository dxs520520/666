from thinkdsp import TriangleSignal
from thinkdsp import SawtoothSignal
import matplotlib.pyplot as plt
from thinkdsp import decorate


signal = TriangleSignal(200)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
plt.subplot(2,2,1)
segment.plot()
decorate(xlabel='Time (s)')

wave = signal.make_wave(duration=0.5, framerate=10000)
spectrum = wave.make_spectrum()
plt.subplot(2,2,2)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
signal = SawtoothSignal(200)
duration = signal.period*3
sawtooth = signal.make_wave(duration, framerate=10000)
plt.subplot(2,2,3)
sawtooth.plot()
decorate(xlabel='Time (s)')
wave = signal.make_wave(duration=0.5, framerate=10000)
spectrum = wave.make_spectrum()
plt.subplot(2,2,4)
spectrum.plot()
decorate(xlabel='Frequency (Hz)')
plt.show()