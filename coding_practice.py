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