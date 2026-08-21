#%%
import numpy as np
import sympy as sp
import math
import matplotlib
from sympy.plotting import plot3d
from scipy.stats import beta

#%%
# note: could use chain rule to predict fire risk for each day of the year

# %%

# could use beta distribution to create app that tells people the 
# probability on a given day that the chances of a fire are high med low etc
# note: high, med, low is arbitrary for now

# note: could include fire size. What is the probability that the 
# probability of a big fire will be high on a given day?

# note: could be by county or state. increases utility

# BETA DISTRIBUTION
# use to calculate the probability that probability is a certain value given a 
# number of successes and failures out of n trials



a = 30 # number of times where fire starts on given day
b = 6 # number of times where fire does not start on a given day

# use cumulative density function to calcultate area under curve which is probability

# tells us that given x_fire_start_days and x_non_fire_start 
# days on a given day of the year what is the probability that fire danger (or fire probability) will 
# be high on that day of the year
high_p = 1 - beta.cdf(0.80, a, b) # re-examine buckets if using Jefreys
print(high_p) 

# tells us that given x_fire_start_days and x_non_fire_start 
# days on a given day of the year what is the probability that fire danger (or fire probability) will 
# be medium on that day of the year
med_p = beta.cdf(0.8, a, b) - beta.cdf(0.3, a, b)
print(med_p) 

# tells us that given x_fire_start_days and x_non_fire_start 
# days on a given day of the year what is the probability that fire danger (or fire probability) will 
# be low on that day of the year
low_p = beta.cdf(0.3, a, b) 
print(low_p) 

#%%
# can use variance and mean behind the scenes to esitmate how confident we are in the prediction of the probabilities
# for each day will have a variance. mean will tell me central estimate of fire probability on that day
# var for beta  = a*b / ((a + b)**2 * (a + b + 1)) # adjust parameters Jefrey's prior

# use arcsine transformation to normalize boundary squeeze if comparing across days
# because days will have the same sample size
# or just report a + b for confidence alongside the mean


# mean
# sum of all values / count = (30 * 1 + 6 * 0) / 36 = a / (a + b) = mean


# also : use Jeffrey's prior here to protect against perfect certainty if a or b = 0
# adjust parameters a' = a + 1/2, b' = b + 1/2
# the 1/2 assumes 1/2 success, 1/2 failure before data arrives
