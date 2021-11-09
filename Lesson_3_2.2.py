import numpy as np
import matplotlib.pyplot as plt
import math

a = 5
a2 = a ** 2
b = 5
b2 = b ** 2
xm = []
xp = []
yp = []
ym = []
for i in np.linspace(-15, 15, 1000):
    x1 = i
    xp.append(x1)
    xm.append(-1 * x1)
    yp.append(b * math.sqrt((x1 / a) ** 2) - 1)
    ym.append(-b * math.sqrt((x1 / a) ** 2) - 1)
plt.plot(xm, yp)
plt.plot(xp, yp)
plt.plot(xm, ym)
plt.plot(xp, ym)
plt.xlabel("y")
plt.ylabel("x")
