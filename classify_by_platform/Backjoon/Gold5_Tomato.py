import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
start = []
board = []
s_board = [[n*m+1 for _ in range(m)] for _ in range(n)]
for i in range(n):
    t = list(map(int, sys.stdin.readline().split()))
    board.append(t)
    for j in range(m):
        if t[j] == 1:
            start.append([i,j])
        elif t[j] == -1:
            s_board[i][j] = 0
dx = [1,-1,0,0]
dy = [0,0,-1,1]
dq = deque()
visited = {}
cur = 0
for s in start:
    dq.append([s[0], s[1], cur])
    visited[tuple(s)] = 1
    s_board[s[0]][s[1]] = 0
while dq:
    t = dq.popleft()
    cX, cY, tt = t[0], t[1], t[2]
    for i in range(4):
        nX, nY = cX+dx[i], cY+dy[i]
        if 0<= nX < n and 0<= nY < m and (nX,nY) not in visited and board[nX][nY]==0 and s_board[nX][nY]>tt+1:
            s_board[nX][nY] = min(s_board[nX][nY], tt+1)
            visited[(nX,nY)] = 1
            dq.append([nX,nY,tt+1])

answer = 0
for i in s_board:
    for j in i:
        if j == n*m+1:
            print(-1)
            sys.exit()
        answer = max(answer, j)

print(answer)
