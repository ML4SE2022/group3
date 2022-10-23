import matplotlib.pyplot as plt

plt.figure()
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('title')
ax = plt.gca()
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')
plt.show()