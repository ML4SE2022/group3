import os
import pandas as pd

# set the path to the directory that contains the files
path = 'C:/Users/User/Desktop/Python/Data/'

# create an empty list to store the data
data = []

# go through all the files and folders in the path
for root, dirs, files in os.walk(path):
    # go through all files
    for file in files:
        # only read files that end with .csv
        if file.endswith('.csv'):
            # create the full path of the file to be read
            filepath = os.path.join(root, file)
            # read the file into a dataframe
            df = pd.read_csv(filepath)
            # add the dataframe to the list
            data.append(df)

# concatenate all data into a single dataframe
df = pd.concat(data)

# print the first 5 rows of the dataframe
print(df.head())