import numpy as np

# Convert all strings to unique floats
def str_to_float(x):
    return np.float(hash(x))

# Apply the function to the column
df['Fault'] = df['Fault'].apply(str_to_float)