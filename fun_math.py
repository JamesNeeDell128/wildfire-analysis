#%%
import sympy as sp
import numpy as np
# %%
# charting a linear function
from sympy import*
x = symbols('x')
f = 2*x + 1
plot(f)
# %%
# charting exponential function
x = symbols('x')
f = x**2 + 1
plot(f)
# %%
# Declaring a function with 2 independent variables
from sympy import *
from sympy.plotting import plot3d
x, y = symbols('x y')
f = 2*x + 3*y
plot3d(f)
# %%
# summations 
summation = sum(2*i for i in range(1, 6))
print(summation)
# %%
# summation of elements
x = [1, 4, 6, 2]
n = len(x) # length x
summation = sum(10 * x[i] for i in range(n))
print(summation)

# %%
# symplify expressions with sympy
from sympy import*
x = symbols('x')
expr = x**2 / x**5
print(expr)
# %%
# power rule
# (8**3)**2 = 8**6

# %%
import math
# 2**x = 8
x = log(8, 2) # default base is e or ln()
print(x)
# a**x = b
# logbase a (b) = x
# %%
# experiment with exponent and log graphs