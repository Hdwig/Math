import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

fig = figure()
ax = Axes3D(fig)
x = np.arange(-10, 10, 0.5)
y = np.arange(-10, 10, 0.5)
x, y = np.meshgrid(x, y)
z = 2 * x + 3 * y + 10
z1 = 2 * x + 3 * y
ax.plot_wireframe(x, y, z)
ax.plot_wireframe(x, y, z1)
show()







