import sys
from itertools import combinations
import math
T = int(sys.stdin.readline())

for _ in range(T):
    dot_n = int(sys.stdin.readline())
    node_l = []
    total_x = 0
    total_y = 0
    for _ in range(dot_n):
        x, y = map(int, sys.stdin.readline().split())
        node_l.append([x,y])
        total_x += x
        total_y += y
    cri = int(dot_n/2)

    comb = combinations(range(dot_n), cri)

    result = math.inf
    for cb in comb:
        sum_x = 0
        sum_y = 0
        for idx in cb:
            sum_x += node_l[idx][0]
            sum_y += node_l[idx][1]
        temp_x = total_x-2*sum_x
        temp_y = total_y-2*sum_y

        result = min(result, (temp_x**2+temp_y**2)**0.5)
    print(result)