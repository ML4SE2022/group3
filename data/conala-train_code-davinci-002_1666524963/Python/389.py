import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, ax = plt.subplots()
ax.plot(x, np.sin(x), '-', label='Sine')
ax.plot(x, np.cos(x), '--', label='Cosine')
ax.axis('equal')
leg = ax.legend()

# Remove frame of legend
leg.get_frame().set_linewidth(0.0)

# Remove border of frame of legend
#leg.get_frame().set_edgecolor('white')

# Remove background of frame of legend
#leg.get_frame().set_facecolor('white')

plt.show()