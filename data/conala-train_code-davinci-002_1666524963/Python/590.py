import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)

# Plot the data
plt.plot(x, x, label='linear')

# Add a legend
plt.legend()

# Add a title
plt.title('Linear vs. Quadratic progression')

# Add X and y Label
plt.xlabel('Input')
plt.ylabel('Output')

# Add a grid
plt.grid(True)

# Add a custom x axis
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Add a custom y axis
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Change the font size of the numbers on the axes
plt.tick_params(axis='both', which='major', labelsize=14)

# Change the font size of the legend
plt.legend(prop={'size': 14})

# Change the font size of the title
plt.title('Linear vs. Quadratic progression', fontsize=20)

# Change the font size of the x and y labels
plt.xlabel('Input', fontsize=14)
plt.ylabel('Output', fontsize=14)

# Show the plot
plt.show()