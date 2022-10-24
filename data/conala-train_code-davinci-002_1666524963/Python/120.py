from collections import Counter

my_list = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]

Counter(my_list)

Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

Counter(my_list).items()

dict_items([(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)])

Counter(my_list).keys()

dict_keys([1, 2, 3, 4, 5])

Counter(my_list).values()

dict_values([3, 4, 4, 2, 1])