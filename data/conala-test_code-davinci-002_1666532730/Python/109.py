import pandas as pd
import matplotlib.pyplot as plt

# create a data frame
df = pd.DataFrame({'lab':['A', 'B', 'C'], 'val':[10, 30, 20]})

# create a figure and axis
fig, ax = plt.subplots()

# plot each data-point
for i in range(len(df['val'])):
    ax.bar(df['lab'][i], df['val'][i], label=df['lab'][i])

# set the x tick labels
ax.set_xticklabels(df['lab'])

# set the legend
ax.legend()

# show the plot
plt.show()