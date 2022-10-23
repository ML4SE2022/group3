# Python 3.6+

# Method 1
my_dict = {i: i for i in my_list}

# Method 2
my_dict = dict.fromkeys(my_list, 1)

# Method 3
my_dict = dict.fromkeys(my_list)