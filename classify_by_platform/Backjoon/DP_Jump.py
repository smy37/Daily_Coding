import sys
from collections import deque


N = int(sys.stdin.readline())
board = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    board.append(temp)

score = [[0 for _ in range(N)] for _ in range(N)]

dq = deque()
dq.append((0,0))
score[0][0] = 1

while dq:

    t = dq.popleft()

    cx, cy = t[0], t[1]
    nx = cx + board[cx][cy]
    ny = cy + board[cx][cy]
    if cx == N-1 and cy == N-1:
        break
    s = score[cx][cy]
    if nx < N:
        if score[nx][cy] == 0:
            dq.append((nx,cy))
        score[nx][cy] += s
    if ny < N:
        if score[cx][ny] == 0:
            dq.append((cx,ny))
        score[cx][ny] += s
    # dq = deque(sorted(dq, key = lambda x : [x[0], x[1]]))

print(score[N-1][N-1])

