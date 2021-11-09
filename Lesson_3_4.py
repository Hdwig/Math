import numpy as np

z = np.array([10, 10, 10]) + np.array([0, 0, -10])
n = np.linalg.norm(z)
print(n)
