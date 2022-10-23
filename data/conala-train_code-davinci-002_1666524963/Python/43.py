import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])
a[a>5] = 0
print(a)