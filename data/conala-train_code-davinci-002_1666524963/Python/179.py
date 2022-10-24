import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
im = ax.imshow(y.reshape((10, 10)), cmap='viridis')
fig.colorbar(im, ax=ax)

plt.show()