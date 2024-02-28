import sys


V = int(sys.stdin.readline())
s_idx = []
g = {i+1:{} for i in range(V)}
for i in range(V):
    t = list(map(int, sys.stdin.readline().split()))
    if len(t) == 4:
        s_idx.append(t[0])
    cri = (len(t)-2)//2
    for j in range(cri):
        g[t[0]][t[1+2*j]] =t[1+2*j+1]
answer = 0
one_p = 0
second_p = 0

from collections import deque

dq = deque()
dq.append([s_idx[0],0])

visited = {}
visited[s_idx[0]] = 1

while dq:
    cur_n, dist = dq.pop()
    for next_n in g[cur_n]:
        if next_n not in visited:
            dq.append([next_n, dist + g[cur_n][next_n]])
            visited[next_n] = 1
            if answer < dist + g[cur_n][next_n] :
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
            if answer < dist + g[cur_n][next_n] :
                answer = dist + g[cur_n][next_n]
                second_p = next_n

print(answer)