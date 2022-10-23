# Create the dictionary of lists
my_dict = {'T1': ['1', '2', '3'], 'T2': ['4', '5'], 'T3': ['6', '7']}

# Create a DataFrame
df = pd.DataFrame(my_dict)

# Create a dictionary of lists to create a MultiIndex
hier_index = df.columns.map(lambda x: my_dict[x])

# Convert the DataFrame to a multi-indexed DataFrame
df.columns = pd.MultiIndex.from_tuples(hier_index)

# Print the output
print(df)