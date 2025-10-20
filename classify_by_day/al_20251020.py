import sys
from collections import deque

N, S, P = map(int, sys.stdin.readline().split())

tree = {}
for _ in range(N-1):
    s, t = map(int, sys.stdin.readline().split())

    if s not in tree:
        tree[s] = {}
    if t not in tree:
        tree[t] = {}

    tree[s][t] = True
    tree[t][s] = True

dq = deque()
dq.append([P])
visit = {P: True}
support = {i+1 : True for i in range(S)}
rest_candidate = []

while dq:
    cur = dq.popleft()
    cur_node = cur[-1]

    for next_node in tree[cur_node]:
        if next_node in support:
            rest_candidate.append(set(cur+[next_node]))
        else:
            if next_node not in visit:
                visit[next_node] = True
                dq.append(cur+[next_node])

answer = float("inf")
for i in range(len(rest_candidate)):
    for j in range(i+1, len(rest_candidate)):
        answer = min(answer, len(rest_candidate[i]|rest_candidate[j]))

print(N-answer)