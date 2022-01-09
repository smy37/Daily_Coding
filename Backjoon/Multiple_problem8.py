import sys
import math

num_list = list(map(int, sys.stdin.readline().strip().split()))

print(math.comb(num_list[0], num_list[1])%10007)