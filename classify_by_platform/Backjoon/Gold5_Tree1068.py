import sys
from collections import deque
N = int(sys.stdin.readline())
t_l = list(map(int, sys.stdin.readline().split()))
r_node = int(sys.stdin.readline())

t_g = {i : [] for i in range(N)}

for i in range(len(t_l)):
    if t_l[i] != -1:
        t_g[t_l[i]].append(i)

remove_n = {}
dq = deque()
dq.append(r_node)
remove_n[r_node] = 1

while dq:
    t = dq.popleft()
    for n in t_g[t]:
        remove_n[n] = 1
        dq.append(n)

answer = 0
for i in t_g:
    if r_node in t_g[i]:
        t_g[i].remove(r_node)
    if len(t_g[i]) == 0 and i not in remove_n:
        answer += 1

print(answer)