import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

g = {}
board = []
p = [i for i in range(N+1)]

for i in range(M):
    t = list(map(int, sys.stdin.readline().split()))
    tt = (min(t[0],t[1]),max(t[0],t[1]))

    if tt not in g:
        g[tt] = t[2]
        board.append(t)
    else:
        if t[2] < g[tt]:
            g[tt] = t[2]
            board.append(t)

board = sorted(board, key = lambda x : x[2])

sum_c = 0
for i in board:
    if p[i[0]] != p[i[1]]:
        cri = p[i[1]]
        for j in range(N+1):
            if p[j] == cri:
                p[j] = p[i[0]]
        sum_c += i[2]

print(sum_c)