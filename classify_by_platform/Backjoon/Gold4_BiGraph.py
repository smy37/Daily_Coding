import sys
from collections import deque
t = int(sys.stdin.readline())

for _ in range(t):
    flag = True
    V, E = map(int, sys.stdin.readline().split())
    g = {i+1:[] for i in range(V)}
    for _ in range(E):
        i = list(map(int,sys.stdin.readline().split()))
        g[i[0]].append(i[1])
        g[i[1]].append(i[0])

    g_idx = {i+1:0 for i in range(V)}
    visited = {}

    for x in range(V):
        if x+1 not in visited:
            dq = deque()
            dq.append(x+1)
            g_idx[x+1] = 1
            visited[x+1] = 0
            while dq:
                cur = dq.popleft()
                for i in g[cur]:
                    if g_idx[i] == g_idx[cur]:
                        flag = False
                        break
                    else:
                        if i not in visited:
                            g_idx[i] = g_idx[cur]*-1
                            dq.append(i)
                for i in g[cur]:
                    visited[i] = 0
                if flag == False:
                    break
            if flag == False:
                break
    if flag == False:
        print("NO")
    else:
        print("YES")
