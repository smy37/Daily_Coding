import sys
import math

N = int(sys.stdin.readline())
num_dict = {i: -1 for i in range(N, 0, -1)}

for n in num_dict:
    if num_dict[n] == -1:
        cri = int(math.log2(n))+1
        upper_bound = 2**cri

        rest = upper_bound-n

        num_dict[n] = rest
        num_dict[rest] = n

for i in range(1, N+1):
    print(num_dict[i])
