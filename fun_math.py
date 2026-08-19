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
x = symbols('x')
f = log(x)
plot(f) # x = e**f # e = ~2.718
# %%
f = 2**x
plot(f)
# %%
for i in range(1,6):
    f = x**i
    print("f(x) = x **",i)
    plot(f)
# %%

x = symbols('x')
for i in range(2, 6): # logbase 1 is undefined because there are infinite solutions
    f = log(x, i)
    print("f(x) = log base:", i, "(x)") # x = i**y
    plot(f)

# %%
# using sympy to calculate limits
x = symbols('x')
f = 1 / x
result = limit(f, x, oo) # oo is infinity, limit as x approaches infinity
print(result)
# %%
# derivatives > tells the slope of a function and useful to 
# measure rate of change of function at any point
# slope = 0 is min or max (concavity etc)

# derivative calculator
# f(x) = x**2

def derivative_x(f, x, step_size):
    m = (f(x + step_size) - f(x)) / ((x + step_size) - x)
    return m
def my_function(x):
    return x**2

slope_at_2 = derivative_x(my_function, 2, .00001)
print(slope_at_2)


# %%
# derivative calculator with sympy
x = symbols('x')
# Now just use Python syntax to declare function
f = x**2
# calculate the derivative of the function
dx_f = diff(f) # diff() calculates derivative and creates dx_f object in sympy
print(dx_f) # 2x
# then use substitution feature in sympy
print(dx_f.subs(x, 2)) # subing 2 for x in f

# %%
# partial derivatives or derivs of functions that have multiple input variables
# d/dx, d/dy, hold other variable constant, slopes referred to as gradients

from sympy import *
from sympy.plotting import plot3d
# Declare x and y to SymPy
x,y = symbols('x y')
# Now just use Python syntax to declare function
f = 2*x**3 + 3*y**3
# Calculate the partial derivatives for x and y
dx_f = diff(f, x) # second paremter is derivative with respect to
dy_f = diff(f, y)
print(dx_f) # prints 6*x**2
print(dy_f) # prints 9*y**2
# plot the function
plot3d(f) 
# %%
# using limits to calculate derivatives
# slope calculation: x**2
# using s in place of h
x,s = symbols('x s') # s is step size

# declare function
f = x**2

# sub into rise/run formula
slope_f = (f.subs(x, x + s) - f) / ((x + s) - x)
print(slope_f)

# calculate slope at x = 2
# substitute 2 for x
slope_2 = slope_f.subs(x, 2)
print(slope_2)

# infinitely approach step size s to 0
result = limit(slope_2, s, 0) # slope as step size approaches 0
print(result)

# don't assign a specific value to x
result2 = limit(slope_f, s, 0)
print(result2) # 2*x
# %%
# chain rule
# can be useful for inferring the relationship between 2 variables when you have linked functions
# dz/dx = dz/dy * dy/dx # y is output and input here so you can use that to infer output of z with respect to x
# real example:
# if you know d(temp) / d(day of year) and d(fire risk) / d(temp) then you could infer d(fire risk) / d(day of year)
# then you'd have to integrate and find C to get the graph

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

