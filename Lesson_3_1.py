import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10)
ys = 5 * x + 3
ym = 7 * x + 4
yl = 0 * x + 7
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.plot(x, ys)
plt.plot(x, ym)
plt.plot(x, yl)
