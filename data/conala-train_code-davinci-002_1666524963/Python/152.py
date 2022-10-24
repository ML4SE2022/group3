import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.show()