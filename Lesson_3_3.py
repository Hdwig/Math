import numpy as np
import matplotlib.pyplot as plt

# 3.1
r = np.linspace(0, 10)
x = r * np.cos(3 * np.pi / 2)
plt.plot(x, r, "o")
plt.show()
# Этот код переводит полярные величины в Декартовы

# 3.2
# r = np.linspace(5, 5, 1000)
# a = np.linspace(0, 2 * np.pi, 1000)
# plt.polar(a, r)
# Окружность
# 3.3
# r = np.linspace(0, 5, 1000)
# a = np.linspace(2 * np.pi, 2 * np.pi, 1000)
# plt.polar(a, r)
# График отрезка прямой линии
