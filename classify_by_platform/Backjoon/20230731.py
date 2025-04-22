import sys
from collections import deque

r, c = map(int, sys.stdin.readline().strip().split())

board = []
for i in range(r):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    board.append(temp)

m_x = [0, 0, 1]
m_y = [1, -1, 0]

m_x2 = [[0,-1,0],[-1,0,1],[0,1,0],[1,0,-1]]
m_y2 = [[-1,0,1],[0,1,0],[1,0,-1],[0,-1,0]]

answer = 0
dq = deque()

for i in range(r):
    for j in range(c):
        for x in range(4):
            tt = board[i][j]
            for y in range(3):
                n_x2 = i + m_x2[x][y]
                n_y2 = j + m_y2[x][y]
                if 0<= n_x2 < r and 0<= n_y2 <c:
                    tt += board[n_x2][n_y2]
                else:
                    tt = 0
                    break
            answer = max(answer, tt)
        s = board[i][j]
        dq = deque()
        dq.append([s, 1, [[i,j]]])

        while dq:
            t = dq.popleft()
            if t[1] == 4:
                answer = max(answer, t[0])
                continue
            else:
                for k in range(3):
                    n_x = t[2][-1][0] + m_x[k]
                    n_y = t[2][-1][1] + m_y[k]

                    if 0<= n_x < r and 0<=n_y<c and [n_x, n_y] not in t[2]:
                        dq.append([t[0]+board[n_x][n_y], t[1]+1, t[2]+[[n_x,n_y]]])
print(answer)




