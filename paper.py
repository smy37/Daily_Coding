from math import gcd
import math
from functools import reduce

# Compute the LCM of a list of numbers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_list(numbers):
    return reduce(lcm, numbers)

# Precompute the time to go from each station i to i+1 for each time t in one cycle
def precompute_times(Train, lcm_cycle):
    dp = []
    for P, T in Train:
        dp_row = []
        for t in range(lcm_cycle):
            if t % P == 0:
                wait_time = 0
            else:
                wait_time = (math.ceil(t / P) * P) - t
            dp_row.append(wait_time + T)
        dp.append(dp_row)
    return dp

# Answer queries using the precomputed dp array
def answer_queries(N, X, dp, Y, Q, Query, lcm_cycle):
    final = []
    for S in Query:
        current_time = S + X
        for i in range(N - 1):
            # Use the dp array to find the time to go from i to i+1
            # taking into account the phase (current_time % lcm_cycle)
            current_time += dp[i][current_time % lcm_cycle]
        current_time += Y
        final.append(current_time)
    return final

# Sample parameters
N = 10
X = 5
Train = [[2,7],[3,3],[5,4],[8,6],[3,7],[6,6],[5,8],[9,4],[7,11]]
Y = 7
Q = 5
Query = [906, 1174, 7, 21, 33]

# Compute the LCM of the P[i] values
lcm_cycle = lcm_list([P for P, _ in Train])

# Precompute times and answer queries
dp = precompute_times(Train, lcm_cycle)
print(answer_queries(N, X, dp, Y, Q, Query, lcm_cycle))




