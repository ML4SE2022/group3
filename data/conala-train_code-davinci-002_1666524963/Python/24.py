import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# sort by column
arr[arr[:, 1].argsort()]