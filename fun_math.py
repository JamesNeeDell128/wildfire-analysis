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
# integrals - opposite of derivative - finds area under curve for given range
# approximating an integral
# a = min of x range
# b = max of range
# n = number of rectangles
# f = function = x**2 + 1

def approx_integral(a, b, n, f):
    delta_x = (b - a) / n # width of rectangle
    sum_area = 0
    for i in range(1, n + 1):
        # midpoint = b - ((delta_x * i) - .5 * (delta_x)) # to plug into f(x), get right most point then move left .5 width
        midpoint = a + ((delta_x * i) - .5 * (delta_x)) # both work
        area = delta_x * f.subs(x, midpoint) # width * height
        sum_area += area
    return sum_area

approx_integral(0, 1, 10000,  (x**2 + 1))

# %%
# more exact integration with sympy
x = symbols('x')
f = x**2 + 1
area = integrate(f, (x, 0, 1)) # integrate f with respect to x between x = 0 and x = 1
print(area) # fraction  
print(float(area)) # decimal
# %%
# using limits to calculate integrals
# Declare variables to SymPy
x, i, n = symbols('x i n')
# Declare function and range
f = x**2 + 1
lower, upper = 0, 1
# Calculate width and each rectangle height at index "i"
delta_x = ((upper - lower) / n)
x_i = (lower + delta_x * i)
fx_i = f.subs(x, x_i)
# Iterate all "n" rectangles and sum their areas
n_rectangles = Sum(delta_x * fx_i, (i, 1, n)).doit()
# Calculate the area by approaching the number
# of rectangles "n" to infinity
area = limit(n_rectangles, n, oo)
print(area) # prints 4/3
# %%
# what is the area under the curve of 3x**2 + 1 between 0 and 1
x = symbols('x')
f = 3*x**2 + 1
area = integrate(f, (x, 0, 2))
print(area)
# %%
# approximating square root with guess and check
# use epsilon: given x we want to find r such that |r**2 -x| < epsilon
# start with a guess known to be too small > g
# increment by a small value > a to give a new guess g
# check if g**2 is within epsilon
# continue until satisfied

# set 2 parameters
# epsilon and increment
# performance will vary in speed and accuracy

x = 54321
epsilon = .01
num_guesses = 0
guess = 0.0
increment = 1

# this works too and way better for some reason. why???

while epsilon >= .01:
    num_guesses += 1
    epsilon = x - guess**2
    guess += increment
print(guess)
print(num_guesses)

# can fail if increment is too big

# while abs(guess**2 - x) >= epsilon and guess**2 <= x:
#     guess += increment
#     num_guesses += 1
# print(guess)
# print(num_guesses) 
# %%
# bisection search
x = 54321
epsilon = .01
num_guesses = 0
guess = x / 2



# while abs(x - guess**2) >= epsilon:
#     num_guesses += 1
#     if guess**2 > x:
#         guess -= .5 * guess
#     else:
#         guess += .5 * guess

# print(guess)
# print(num_guesses) no high or low boundaries
# print in a loop if its not stopping
x = .5
epsilon = .01
num_guesses = 0
low = 0.0
high = x
guess = (high + low) / 2

if x < 1 and x > 0:
    high = 1
    low = x
while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1
print(guess)
print(num_guesses)

# %%
x = 27
epsilon = .01
num_guesses = 0
low = 0.0
high = x
guess = (high + low) / 2

if x < 1 and x > 0:
    high = 1
    low = x
while abs(guess**3 - x) >= epsilon:
    if guess**3 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1
print(guess)
print(num_guesses)

# %%
# newton rhapson rootfinder
k = 24
epsilon = .01
guess = 1
num_guesses = 0
root = 3 # can do any root

while abs(guess**root - k) >= epsilon:
    num_guesses += 1
    # formula
    guess = guess - (((guess**root) - k)/ (root*guess**(root-1)))
print(guess)
print(num_guesses)


# %%

# %%
# probability - theoretical study of measuring certainty that an event will happen
# P not x = 1- p

# probability and odds

# P(x) = O(x) / 1 + O(x)
# O(x) = P(x) / 1 - P(x)

# joint probability is like an and operator
# P(A and B) = P(A) * P(B) product rule

# union probabilities - prob of getting event A or B - or operation
# with a die > chances of getting a 4 or 6
# P(4 or 6) = 1/6 + 1/6 = 1/3

# events that NOT mutually exclusive - events that can occur simultaneously

# but with a coin flip and die roll chances of getting heads and a 6 is not 1/2 + 1/6
# it is 1/2 + 1/12
# to remove double count use sum rule of probability
# P(A or B) = P(A) + P(B) - P(A) * P(B) # subtract joint probability
# if events are mutually exclusive - only one outcome is allowed - joint probability (P(A and B) is 0)

# %%
# conditional probability - probability of event A occuring given event B has occured
# P(A given B) or P(A|B)
# Bayes Theorem - can use to flip conditional probabilities
# P(A|B) = P(B|A)*P(A) / P(B)

# abstraction and avoiding magic numbers
p_coffee_drinker = .65
p_cancer = .005
p_coffee_drinker_given_cancer = .85
p_cancer_given_coffee_drinker = p_coffee_drinker_given_cancer * p_cancer / p_coffee_drinker

# prints 0.006538461538461539
print(p_cancer_given_coffee_drinker)

# %%
# joint and union conditional probabilities
# P(A and B) = P(B) * P(A|B)

# unions but A may affect B
# P(A or B) = P(A) + P(B) - P(A|B) * P(B)
# %%
# Binomial Distributions
# measures how likely k success will happen out of n trails given P (probility of success)
# from scratch

# create factorial function to multiply consec ints down to 1
def factorial(n: int):
    f = 1
    for i in range(n):
        f *= (i + 1)
    return f

print(factorial(5))

# generate coefficient needed for binomial distribution, # select k outcomes from n possibilites
def binomial_coefficient(n: int, k: int):
    return factorial(n) / (factorial(k)* factorial(n - k))

# binomial distribution calculates the probability of k events out of n trials
# given the p probability of k occuring
def binomial_distribution(k: int, n: int, p: float):
    return binomial_coefficient(n, k) * (p ** k) * (1 - p) ** (n - k)




# 10 trials where each has 90% success probability
n = 10
p = 0.9

# print(factorial(n))
# print(binomial_coefficient(n,k))
# print(binomial_distribution(k,n,p))

for k in range(n + 1):
    probability = binomial_distribution(k, n, p)
    print("{0} - {1}".format(k, probability))



#%%
from scipy.stats import binom

n = 10 # number of trials
p = 0.9 # probility of success (given)

for k in range(n + 1):
    probability = binom.pmf(k, n, p) # probability mass function
    print("{0} - {1}".format(k, probability))

# %%
# beta distribution - probabilities of probabilities
# use to calculate the probability that probability is a certain value given a number of successes and failures out of n trials

from scipy.stats import beta
a = 30 # number of successes
b = 6 # number of failures

# use cumulative density function to calcultate area under curve up to a given x value (.90)
p1 = beta.cdf(.90, a, b) # gives us area up to 90% underlying probability of success
print(p1) # there is a 77.5 % chance that given 8 / 10 success the probability of success (or success rate) will be less than 90%

p = 1 - beta.cdf(.90, a, b)
print(p) # tells us there is a 22.5 % chance that given 8 / 10 success the probability of success (or success rate) will be 90% or greater

# calculate if underlying success rate between 80 and 90%

p3 = beta.cdf(.90, a, b) - beta.cdf(.80, a, b)
print(p3)

# to see beta dist from scratch go to appendix A pg 292-293 
# %%
a = .3
b = .4

# P(a and b)
p = a*b
print(p)

# P(!a or b)
# addition - joint prob
p1 = (1 - a) + b  - ((1 - a) * b)
print(p1)

p2 = a * (b - .2)
print(p2)

# %%
# You have 137 passengers booked on a flight from Las Vegas to Dallas. However,
# it is Las Vegas on a Sunday morning and you estimate each passenger is 40%
# likely to not show up.
# You are trying to figure out how many seats to overbook so the plane does not fly
# empty.
# How likely is it at least 50 passengers will not show up?

n = 137 # number of trials
p = 0.4 # probility of success (given)
no_show = 0

# calculate binomial distribution
for k in range(50, n + 1):
    probability = binom.pmf(k, n, p) # probability mass function
    no_show += probability # add up probabilities from 50 to 137
    print("{0} - {1}".format(k, probability))
print(f' There is a {no_show * 100} % chance that at least 50 passengers will not show up')


# %%
# You flipped a coin 19 times and got heads 15 times and tails 4 times.
# Do you think this coin has any good probability of being fair? Why or why not?

# use beta distribution to get probability of fairness (.5)
# what is the probability that given a 15/19 'success' rate the underlying prob of success will be in a close
# range around .5?
from scipy.stats import beta
a = 15 # number of successes
b = 4 # number of failures

# use cumulative density function to calcultate area under curve up to a given a close range (.49 - .51))
p4 = beta.cdf(0.51, a, b) - beta.cdf(0.49, a, b)
print(p4)
# or look at likelihood to be above .5 probability of successes
p5 = 1 - beta.cdf(0.5, a, b)
print(p5)
# intuitively I think it could be fair but beta says it is not. If I could run more tests I would get a better answer
# but beta says don't

# %%
# descriptive statistics

# calculating weighted mean
sample = [90, 80, 63, 87]
weights = [.20, .20, .20, .40]

print(list(zip(sample, weights))) # combines sample and weight arrays

weighted_mean = sum(s * w for s, w in zip(sample, weights)) / sum(weights)
print(weighted_mean)

8 // 2
?len
len(sample)
sample[len(sample) - 1]
# %%
# median
sample = [0, 1, 5, 7, 8, 10, 14, 7, 21, 4, 12, 4]

len(sample) / 2

def median(values):
    ordered = sorted(values) # must sort to calculate median
    print(ordered)
    n = len(ordered)
    if n % 2 == 0:
        mid = (ordered[int(n / 2)] + ordered[int(n / 2) - 1]) / 2
    else:
        mid = ordered[n // 2]
    return mid

print(median(sample))


# %%
# easiest leetcode problem. two sum. took 5 min
a = [3, 6, 8, 12, 7] 
b = 10
 
# find positions in a that sum to b

# check first against rest then update code
def check_first(a, b):
    solution = False # set condition if no elements add to input value
    for j in range(len(a)):
        r = -1 # will need to reset after each loop
        for i in a:
            r += 1
            if i + a[j] == b:
        # how do I return the position in the brackets? r counter, j
                solution = True
                return j , r 
    if solution == False:
        return "no two elements add to input value" 

print(check_first(a, b))
# %%

# %%
