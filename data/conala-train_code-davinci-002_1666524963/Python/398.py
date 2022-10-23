import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.xaxis.tick_top()
ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')
ax.plot([1,2,3])
plt.show()