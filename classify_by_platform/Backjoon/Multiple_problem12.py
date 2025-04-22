import sys

num_list = list(map(int, sys.stdin.readline().rstrip().split()))

# def count_number(n, k):
#     cnt = 0
#     while n!= 0:
#         n //= k
#         cnt += n
#     return cnt
#

import math

def count_number(n, k):
    start = 1
    cnt = 0
    while n// (k**start) != 0:
        cnt += (n//(k**start))
        start +=1

    return cnt


five_cnt = count_number(num_list[0], 5) - count_number(num_list[1], 5) - count_number(num_list[0]-num_list[1], 5)
two_cnt = count_number(num_list[0], 2) - count_number(num_list[1], 2) - count_number(num_list[0]-num_list[1], 2)

print(min(five_cnt, two_cnt))

