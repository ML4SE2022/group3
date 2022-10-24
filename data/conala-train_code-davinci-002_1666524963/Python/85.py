import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5], [1,2,3,4,5])
plt.plot([1,2,3,4,5], [1,2,3,4,5])

print(plt.gca().lines[-1].get_color())