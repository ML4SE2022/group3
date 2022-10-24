import numpy as np

a = [('a', np.nan), ('b', 2.0), ('c', 1.0)]

min(a, key=lambda x: x[1])