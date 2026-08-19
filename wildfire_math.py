#%%
import numpy as np
import sympy as sp
import math
import matplotlib
from sympy.plotting import plot3d

# %%
# chain rule
# can be useful for inferring the relationship between 2 variables when you have linked functions
# dz/dx = dz/dy * dy/dx # y is output and input here so you can use that to infer output of z with respect to x
# real example:
# if you know d(temp) / d(day of year) and d(fire risk) / d(temp) then you could infer d(fire risk) / d(day of year)
# then you'd have to integrate and find C to get the graph

# example of using chain rule:

from sympy import*

x, y = symbols('x y')
# y = x**2 + 1
# z = y**3 - 2

# take derivative for both functions
_y = x**2 + 1 # using y twice
dy_dx = diff(_y)
z = y**3 - 2
dz_dy = diff(z)

# calc derivative with chain rule, sub in x**2 + 1 for y
dz_dx_chain = (dy_dx * dz_dy).subs(y, _y) 
dz_dx_no_chain = diff(z.subs(y, _y)) 

# both should be equal
print(dz_dx_chain) # take the deriv of each, multiply then sub
print(dz_dx_no_chain) # sub then take deriv
# %%
