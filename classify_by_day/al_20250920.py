import sys
import math

upper = 1000000000

sum_l = []

for i in range(1, 30):
    sum_l.append(2**i-1)

print(sum_l)

T = int(sys.stdin.readline())
for _ in range(T):
    cur_n = int(sys.stdin.readline())