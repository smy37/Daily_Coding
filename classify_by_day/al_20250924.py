import sys
import math

N = int(sys.stdin.readline())

if N == 1:
    print(0)
else:
    print(int(math.ceil(N/2)))