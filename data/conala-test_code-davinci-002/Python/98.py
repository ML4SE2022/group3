import re

# \d is a digit
# \D is not a digit
# \s is a whitespace character
# \S is not a whitespace character
# \w is an alphanumeric character
# \W is not an alphanumeric character

# \d{3} is 3 digits
# \d{3,} is 3 or more digits
# \d{3,5} is 3, 4, or 5 digits

# \D{3} is 3 non-digits
# \D{3,} is 3 or more non-digits
# \D{3,5} is 3, 4, or 5 non-digits

# \s{3} is 3 whitespace characters
# \s{3,} is 3 or more whitespace characters
# \s{3,5} is 3, 4, or 5 whitespace characters

# \S{3} is 3 non-whitespace characters
# \S{3,} is 3 or more non-whitespace characters
# \S{3,5} is 3, 4, or 5 non-whitespace characters

# \w{3} is 3 alphanumeric characters
# \w{3,} is 3 or more alphanumeric characters
# \w{3,5} is 3, 4, or 5 alphanumeric characters

# \W{3} is 3 non-alphanumeric characters
# \W{3,} is 3 or more non-alphanumeric characters
# \W{3,5} is 3, 4, or 5 non-alphanumeric characters

# \d{3}-\d{3}-\d{4} is a phone number
# \d{3}-\d{3}-\d{4} is a phone number
# \d{3}-\d{3}-\d{4} is a phone number
# \d{3}-\d{3}-\d{4} is a phone number
# \d{3}-\d{3}-\d{4} is a phone number
# \d{3}-\d{3}-\d{4} is