import matplotlib.pyplot as plt
import numpy as np

# Create a simple spectrogram
spectrogram = np.random.rand(10, 10)

# Create a figure and add a subplot with an image plot of the spectrogram
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.imshow(spectrogram)

# Add a colorbar to the image plot
fig.colorbar(ax1.imshow(spectrogram))

# Show the figure
fig.show()