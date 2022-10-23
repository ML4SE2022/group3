from sympy import *

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

solve(x**2 - 1, x)