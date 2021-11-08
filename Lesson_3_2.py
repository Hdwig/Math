import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 1)
y = x + 3
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
xn = x * np.cos(np.pi / 2) + y * np.sin(np.pi / 2)
yn = -x * np.sin(np.pi / 2) + y * np.cos(np.pi / 2)
plt.plot(xn, yn, "b*")
plt.plot(x, y, 'o')
# как мы видим из данного графика, расстояния между точками сохраняются, так как соблюдаюся 3 основные правила
# преобразования
