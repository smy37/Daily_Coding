import sys
import math
N, T = map(int, sys.stdin.readline().split())

special = {}
ordinary = {}
cord_l = []
for i in range(N):
    s, x, y = map(int, sys.stdin.readline().split())
    if s == 1:
        special[i] = T
    else:
        ordinary[i] = 0
    cord_l.append([x, y])

for k in ordinary:
    ordinary_d = math.inf
    x1, y1 = cord_l[k]
    for s_k in special:
        x2, y2 = cord_l[s_k]
        ordinary_d = min(ordinary_d, abs(x1-x2)+abs(y1-y2))
    ordinary[k] = ordinary_d

min_d = [[math.inf for _ in range(N)] for _ in range(N)]

for i in range(N):
    x1, y1 = cord_l[i]
    for j in range(i+1, N):
        x2, y2 = cord_l[j]
        if i in special and j in special:
            min_d[i][j] = min(T, abs(x1-x2)+abs(y1-y2))
            min_d[j][i] = min(T, abs(x1-x2)+abs(y1-y2))
        elif i in special:
            min_d[i][j] = min(T+ordinary[j], abs(x1-x2)+abs(y1-y2))
            min_d[j][i] = min(T+ordinary[j], abs(x1-x2)+abs(y1-y2))
        elif j in special:
            min_d[i][j] = min(ordinary[i]+T, abs(x1-x2)+abs(y1-y2))
            min_d[j][i] = min(ordinary[i]+T, abs(x1-x2)+abs(y1-y2))
        else:
            min_d[i][j] = min(ordinary[i]+ordinary[j]+T, abs(x1-x2)+abs(y1-y2))
            min_d[j][i] = min(ordinary[i]+ordinary[j]+T, abs(x1-x2)+abs(y1-y2))

M = int(sys.stdin.readline())

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    print(min_d[a-1][b-1])