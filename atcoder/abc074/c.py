import numpy as np
from scipy.optimize import linprog


c = [-3, -2]
A = [[2, 1], [1, 1]]
b = [6, 4]
x0_bounds = (None, None)
x1_bounds = (1, None)
res = linprog(c, A_ub=A, b_ub=b, bounds=(x0_bounds, x1_bounds))

res
