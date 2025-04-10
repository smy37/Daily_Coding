import sys
from itertools import permutations
import math

def cal(a, l_a, r_a):
    x_a, x_y = 0, a
    x_la, y_la = -l_a/math.sqrt(2), l_a/math.sqrt(2)
    x_ra, y_ra = r_a/math.sqrt(2), r_a/math.sqrt(2)

    if (y_la-x_y)/(x_la-x_a) < (y_ra-x_y)/(x_ra-x_a):
        return False
    else:
        return True

num_l = list(map(int, sys.stdin.readline().split()))

cnt = 0
for p in permutations(num_l, 8):
    flag = True
    for i in range(len(p)):
        if i == len(p)-1:
            if not cal(p[i], p[i-1], p[0]):
                flag = False
                break
        else:
            if not cal(p[i], p[i - 1], p[i + 1]):
                flag = False
                break
    if flag:
        cnt +=1

print(cnt)