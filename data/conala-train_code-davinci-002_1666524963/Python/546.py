import numpy as np

a = np.array([[1, 2, 3], [4, 5, np.nan], [7, 8, 9]])

a[~np.isnan(a).any(axis=1)]