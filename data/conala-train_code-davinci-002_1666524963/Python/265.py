import numpy as np

data = np.recfromcsv('data/data.csv')

print data.dtype

print data[0]

print data[-1]