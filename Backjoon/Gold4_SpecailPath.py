import sys

V, E = map(int, sys.stdin.readline().split())

g = {i+1 : {} for i in range(V)}
for i in range(E):
    s, e, w = map(int, sys.stdin.readline().split())

    if e not in g[s]:
        g[s][e] = w
    else:
        g[s][e] = min(g[s][e], w)

    if s not in g[e]:
        g[e][s] = w
    else:
        g[e][s] = min(g[e][s], w)

v1, v2 = map(int, sys.stdin.readline().split())

import heapq

def shortest_path(gr, s_node):
    dist = {i+1 : float('infinity') for i in range(V)}
    hq = []
    heapq.heappush(hq, [0, s_node])

    while hq:
        c_d, c_n = heapq.heappop(hq)
        # if c_n == e_node:
        #     return c_d
        if dist[c_n] < c_d:
            continue
        for adj, w in gr[c_n].items():
            distance = w + c_d
            if dist[adj] > distance:
                dist[adj] = distance
                heapq.heappush(hq, [distance,adj])

    return dist

t1 = shortest_path(g, 1)
t1[1] = 0
t2 = shortest_path(g, v1)
t2[1] = 0
t3 = shortest_path(g, v2)
t3[1] = 0

if v2 == V:
    l = t1[v1]+t2[v2]
else:
    l = min(t1[v1]+t2[v2]+t3[V], t1[v2]+t3[v1]+t2[V])
if l == float('infinity'):
    print(-1)
else:
    print(l)
