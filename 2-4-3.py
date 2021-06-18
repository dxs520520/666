from thinkdsp import TriangleSignal
from thinkdsp import decorate
import matplotlib.pyplot as plt
triangle = TriangleSignal().make_wave(duration=0.01)
spectrum = triangle.make_spectrum()
spectrum.hs[0] = 100
triangle.plot(color='gray')
spectrum.make_wave().plot()
plt.show()
