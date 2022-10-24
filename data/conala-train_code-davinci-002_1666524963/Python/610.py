# In[ ]:


# Python

# Select alternate characters

# Method 1

# Using list slicing

# Initializing string
test_str = "geeksforgeeks"

# Printing original string
print("The original string is : " + str(test_str))

# Using list slicing to select alternate characters
# Selecting alternate characters
res = test_str[::2]

# Printing result
print("The alternate characters of string are : " + str(res))


# In[ ]:


# Method 2

# Using loop

# Initializing string
test_str = "geeksforgeeks"

# Printing original string
print("The original string is : " + str(test_str))

# Using loop to select alternate characters
# Selecting alternate characters
res = ""
for i in range(0, len(test_str), 2):
    res += test_str[i]

# Printing result
print("The alternate characters of string are : " + str(res))


# In[ ]:


# Method 3

# Using list comprehension

# Initializing string
test_str = "geeksforgeeks"

# Printing original string
print("The original string is : " + str(test_str))

# Using list comprehension to select alternate characters
# Selecting alternate characters
res = [test_str[i] for i in range(0, len(test_str), 2)]

# Printing result
print("The alternate characters of string are : " + str(res))


# In[ ]:


# Method 4

# Using filter() + lambda

# Initializing string
test_str = "geeksforgeeks"

# Printing original string
print("The original string is : " + str(test_str))

# Using filter() + lambda to select alternate characters
# Selecting alternate characters
res = filter(lambda x: test_str.index(x) % 2 == 0, test_str)

# Printing result
print("The alternate characters of string are : " + str(res))


# In[ ]:


# Method 5

# Using join() + list comprehension