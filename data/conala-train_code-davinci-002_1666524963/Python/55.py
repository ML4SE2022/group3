# In[ ]:


# Python

# Create a list of lists of lists
list_of_lists_of_lists = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

# Sum the 2nd list items in the list of lists of lists
sum([item[1] for item in [item for item in list_of_lists_of_lists]])


#