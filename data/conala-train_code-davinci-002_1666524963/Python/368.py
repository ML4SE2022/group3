def sum_of_product_of_combinations(lst):
    """
    Given a list of numbers, return the sum of the product of all possible combinations of two numbers.
    """
    return sum([x*y for x in lst for y in lst if x != y])

print(sum_of_product_of_combinations([1,2,3,4,5]))