a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
map(lambda x, y: x + y, a, b)
[5, 7, 9]
map(lambda x, y: x + y, a, c)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <lambda>
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'