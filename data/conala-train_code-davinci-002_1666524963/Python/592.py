import numpy as np

def mag_sq(x, y, z):
    return x*x + y*y + z*z

def mag_sq_numpy(x, y, z):
    return np.sum(x*x + y*y + z*z)