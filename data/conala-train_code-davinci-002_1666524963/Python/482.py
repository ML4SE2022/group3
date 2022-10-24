import random

def print_random_variable(variables):
    """
    Print a variable selected by a random number
    """
    print(variables[random.randint(0, len(variables) - 1)])

variables = ['a', 'b', 'c', 'd', 'e']
print_random_variable(variables)