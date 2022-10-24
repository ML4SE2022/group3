import numpy as np

a = np.array([1, 2, 3])
print(a)

# [1 2 3]

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# [[1 2 3]
#  [4 5 6]]

c = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)
print(c)

# [[1. 2. 3.]
#  [4. 5. 6.]]

d = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.complex)
print(d)

# [[1.+0.j 2.+0.j 3.+0.j]
#  [4.+0.j 5.+0.j 6.+0.j]]

e = np.zeros((3, 4))
print(e)

# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

f = np.ones((2, 3, 4), dtype=np.int16)
print(f)

# [[[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]
#
#  [[1 1 1 1]
#   [1 1 1 1]
#   [1 1 1 1]]]

g = np.empty((2, 3))
print(g)

# [[1. 1. 1.]
#  [1. 1. 1.]]

h = np.arange(10, 30, 5)
print(h)

# [10 15 20 25]

i = np.arange(0, 2, 0.3)
print(i)

# [0.  0.3 0.6 0.9 1.2 1.5 1.8]

j = np.linspace(0, 2, 9)
print(j)

# [