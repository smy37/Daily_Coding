import sys
import math
N = int(sys.stdin.readline())
node_l = []

for _ in range(N):
    node_l.append(list(map(int, sys.stdin.readline().split())))

global_idx = -1
global_max = math.inf
for i in range(N):
    t_max = 0
    for j in range(N):
        if i != j:
            n1, n2 = node_l[i], node_l[j]
            d = (n1[0]-n2[0])**2 + (n1[1]-n2[1])**2
            if d > t_max:
                t_max = d
    if t_max < global_max:
        global_idx = i
        global_max = t_max

print(node_l[global_idx][0], node_l[global_idx][1])