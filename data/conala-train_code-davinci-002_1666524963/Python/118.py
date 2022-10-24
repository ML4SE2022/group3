import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
y = np.random.randn(1000)

plt.hist2d(x, y, bins=40)
plt.colorbar()
plt.show()