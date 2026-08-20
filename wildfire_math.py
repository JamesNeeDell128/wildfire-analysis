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
# could use beta distribution to create app that tells people the 
# probability on a given day that the chances of a fire are high med low etc
# note: high, med, low is arbitrary for now

# note: could include fire size. Ask what is the probability that the 
# probability of a big fire will be high on a given day?


# use to calculate the probability that probability is a certain value given a 
# number of successes and failures out of n trials


from scipy.stats import beta

a = 30 # number of times where fire starts on given day
b = 6 # number of times where fire does not start on a given day

# use cumulative density function to calcultate area under curve which is probability


# tells us that given x_fire_start_days and x_non_fire_start 
# days on a given day of the year what is the probability that fire danger (or fire probability) will 
# be high on that day of the year
high_p = 1 - beta.cdf(0.80, a, b) 
print(high_p) 

# tells us that given x_fire_start_days and x_non_fire_start 
# days on a given day of the year what is the probability that fire danger (or fire probability) will 
# be medium on that day of the year
med_p = beta.cdf(0.79, a, b) - beta.cdf(0.3, a, b)
print(med_p) 

# tells us that given x_fire_start_days and x_non_fire_start 
# days on a given day of the year what is the probability that fire danger (or fire probability) will 
# be low on that day of the year
low_p = beta.cdf(0.29, a, b) 
print(low_p) 

# %%
