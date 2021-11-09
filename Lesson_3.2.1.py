import numpy as np
import matplotlib.pyplot as plt
import math

a = 10
a2 = a ** 2
b = 2
b2 = b ** 2
xm = []
xp = []
yp = []
ym = []
for i in np.linspace(-10, 10, 1000):
    x1 = i
    xp.append(x1)
    yp.append(math.sqrt(b2 - (x1 ** 2 * b2) / a2))
    ym.append(-math.sqrt(b2 - (x1 ** 2 * b2) / a2))
plt.plot(xp, yp)
plt.plot(xp, ym)
plt.xlabel("x")
plt.ylabel("y")
