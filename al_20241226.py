import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

tree = {i+1:{} for i in range(N)}
for _ in range(N-1):
    n1, n2, w = map(int, sys.stdin.readline().split())
    tree[n1][n2] = w
    tree[n2][n1] = w

for _ in range(K):
    s_n, t_n = map(int, sys.stdin.readline().split())
    s = deque([[s_n, 0]])
    dist = 0
    while s:
        t, t_dist = s.popleft()
        if t == t_n:
            dist = t_dist
            break
        for k in tree[t]:
            s.append([k, t_dist + tree[t][k]])
    print(dist)