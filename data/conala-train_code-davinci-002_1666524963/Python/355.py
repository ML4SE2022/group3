# Python code

# Importing the required libraries
import pandas as pd

# Creating a dataframe
df = pd.DataFrame({'Name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
                   'Score': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   'Age': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]})

# Sorting the dataframe by Score and Age
df.sort_values(by=['Score', 'Age'], ascending=[True, False])