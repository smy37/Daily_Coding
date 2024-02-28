import sys

V, E = map(int, sys.stdin.readline().split())

g = {i+1 : i+1 for i in range(V)}
e_list = {}
for i in range(E):
    t = list(map(int, sys.stdin.readline().split()))
    min_v = min(t[0],t[1])
    max_v = max(t[0],t[1])
    if (min_v, max_v) not in e_list:
        e_list[(min_v, max_v)] = t[2]
    elif e_list[(min_v, max_v)] > t[2]:
        e_list[(min_v, max_v)] = t[2]

e_list = sorted(e_list.items(), key = lambda x : x[1])

sum_c = 0

visited = [0 for _ in range(V+1)]
for x in e_list:
    i = x[0]
    if g[i[0]]!=g[i[1]]:
        min_v = min(g[i[0]], g[i[1]])
        max_v = max(g[i[0]], g[i[1]])
        for k in g:
            if g[k] == max_v:
                g[k] = min_v
        sum_c += x[1]
print(sum_c)