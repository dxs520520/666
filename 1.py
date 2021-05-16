import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
t = np.arange(-10,10+1)

x=2*np.cos(t*np.pi/4)+3*np.sin(t*np.pi/6)-np.cos(t*np.pi/2)

plt.title('3200442073')
plt.subplot(111)
plt.stem(t,x)
plt.show()