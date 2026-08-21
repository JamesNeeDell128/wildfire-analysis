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
# how can I do using a data dict?
# put each in to a dictionary where key gets b - a
# check key against a
# return spot in key and spot in a?

# data dictionary example

# mode

# import allows us to fill an empty dictionary and increment at the same time
from collections import defaultdict 

sample = [1, 3, 2, 5, 7, 0, 2, 3]
counts = defaultdict(int) # create counts dictionary
for s in sample: # every time through sample counts is loaded with each key(value in sample) but if key already exists it will not be loaded twice
    counts[s] += 1 # value associated with key(s) gets + 1
print(counts)
print(counts[7]) 
max_count = max(counts.values())
print(counts.items()) # gives seq of key-value pairs in tuple form
modes = [] # set empty array for modes
for key, value in counts.items(): # split tuples created into 2. key grabs first, value grabs second
    if value == max_count: # value is number of times key repeats
        modes.append((key, value)) # adds key into empty modes list, append only accepts 1 arg
print(modes) # prints modes as first entry then frequency as second

# modes.append(f"{key} (appears {value} times)") f string inside the loop ***sick!!

# %%
# mutates list
def square_list(L): # iterate over length of list
    for i in range(len(L)):
        L[i] = L[i]**2 # no return value for mutating functions
# %%
lst = [2, 6, 8]
square_list(lst)
# %%
