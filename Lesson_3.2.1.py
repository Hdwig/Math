import numpy as np
import matplotlib.pyplot as plt
import math

a = 2
a2 = a ** 2
b = 3
b2 = b ** 2
xm = []
xp = []
yp = []
ym = []
for i in np.linspace(-2, 2, 1000):
    x1 = i
    xp.append(x1)
    xm.append(-1 * x1)
    yp.append(math.sqrt(b2 - (x1 ** 2 * b2) / a2))
    ym.append(-math.sqrt(b2 - (x1 ** 2 * b2) / a2))
plt.plot(xm, yp)
plt.plot(xp, yp)
plt.plot(xm, ym)
plt.plot(xp, ym)
# plt.xlim([-3, 3])
plt.xlabel("x")
plt.ylabel("y")
