import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4*np.pi, 10000)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

