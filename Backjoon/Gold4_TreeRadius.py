import sys
from collections import deque

N = int(sys.stdin.readline())
if N == 1:
    print(0)
    sys.exit()
leaf_node = {1 : 1}
g = {i+1 : {} for i in range(N)}

for i in range(N-1):
    t = list(map(int, sys.stdin.readline().split()))
    g[t[1]][t[0]] = t[2]
    g[t[0]][t[1]] = t[2]
    leaf_node[t[1]] = 1

answer = 0
cnt = 0
one_p = 0
second_p = 0
dq = deque()
dq.append([1,0])
visited = {}
visited[1] = 1
while dq:
    cur_n, dist = dq.pop()
    for next_n in g[cur_n]:
        if next_n not in visited:
            dq.append([next_n, dist + g[cur_n][next_n]])
            visited[next_n] = 1
            if answer < dist + g[cur_n][next_n]:
                answer = dist + g[cur_n][next_n]
                one_p = next_n

dq = deque()
dq.append([one_p,0])

visited = {}
visited[one_p] = 1
while dq:
    cur_n, dist = dq.pop()
    for next_n in g[cur_n]:
        if next_n not in visited:
            dq.append([next_n, dist + g[cur_n][next_n]])
            visited[next_n] = 1
            if answer < dist + g[cur_n][next_n]:
                answer = dist + g[cur_n][next_n]
                second_p = next_n

print(answer)