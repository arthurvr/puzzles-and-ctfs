import math

# First question: Jack's Birthday Hash

# This is a typical question on the Birthday paradox.
# See https://en.wikipedia.org/wiki/Birthday_problem

N = 11
chance = 0.5
approx = math.log(chance, (2**N - 1)/2**N)
print(math.ceil(approx))

# Second question: Jack's Birthday confusion

# "How many unique secrets would you expect to hash to have (on average) a 75% chance of a collision between two distinct secrets?"

# This one I solved using Mathematica (WolframAlpha): https://www.wolframalpha.com/input?i=Solve%5B1+-+%28e%5E%28%28%28-k%29%28k+-+1%29%29%2F%282%282%5E11%29%29%29%29+%3D%3D+0.75%2C+k%5D

# Basic explanation: when does the probability of getting the same hashes become 0.75?

# The answer (rounded up) is 76.


