import numpy as np
import matplotlib.pyplot as plt

phi = (1 + np.sqrt(5)) / 2
s = 1 / phi
theta = np.pi / 5
R = np.exp(1j * theta)

z = 0 + 0j
points = []
for _ in range(10000):
    if np.random.random() < 0.5:
        z = s * z
    else:
        z = s * R * z + 1
    points.append(z)

x = [p.real for p in points]
y = [p.imag for p in points]
plt.scatter(x, y, s=0.1, c='black')
plt.axis('equal')
plt.title('Pentagonal Strange Attractor')
plt.show()
