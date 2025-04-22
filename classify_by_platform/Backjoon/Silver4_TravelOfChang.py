import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    g = {}
    for i in range(M):
        t = list(map(int, sys.stdin.readline().split()))
        if t[0] not in g:
            g[t[0]] = []
        g[t[0]].append(t[1])
        if t[1] not in g:
            g[t[1]] = []
        g[t[1]].append(t[0])

    print(N-1)