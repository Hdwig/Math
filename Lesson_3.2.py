import numpy as np
import matplotlib.pyplot as plt
import math

r = 1000
xm = []
xp = []
yp = []
ym = []
for i in range(1001):
    x1 = i
    xp.append(x1)
    xm.append(-1 * x1)
    yp.append(math.sqrt(r ** 2 - x1 ** 2))
    ym.append(-math.sqrt(r ** 2 - (-x1) ** 2))
plt.plot(xm, yp)
plt.plot(xp, yp)
plt.plot(xm, ym)
plt.plot(xp, ym)
plt.xlabel("x")
plt.ylabel("y")
