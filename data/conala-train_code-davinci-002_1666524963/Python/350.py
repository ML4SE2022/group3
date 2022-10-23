I have a list of lists, and I want to apply itertools.product to each of the lists.

For example, if I have:

<code>
list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
</code>

I want to get:

<code>
[[1,4,7], [1,4,8], [1,4,9], [1,5,7], [1,5,8], [1,5,9], [1,6,7], [1,6,8], [1,6,9], [2,4,7], [2,4,8], [2,4,9], [2,5,7], [2,5,8], [2,5,9], [2,6,7], [2,6,8], [2,6,9], [3,4,7], [3,4,8], [3,4,9], [3,5,7], [3,5,8], [3,5,9], [3,6,7], [3,6,8], [3,6,9]]
</code>

I tried:

<code>
list(itertools.product(*list_of_lists))
</code>

but it gives me:

<code>
[(1, 4, 7), (1, 4, 8), (1, 4, 9), (1, 5, 7), (1, 5, 8), (1, 5, 9), (1, 6, 7), (1, 6, 8), (1, 6, 9), (2, 4, 7), (2, 4, 8), (2, 4, 9), (2, 5, 7), (2, 5, 8), (2, 5, 9), (2, 6, 7), (2, 6, 8), (2, 6, 9), (3, 4, 7), (3, 4, 8), (3, 4, 9), (3, 5, 7), (3, 5, 8), (3, 5, 9), (3, 6, 7), (3, 6,