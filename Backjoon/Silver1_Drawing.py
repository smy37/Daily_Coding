import sys
from collections import deque
r, col = map(int, sys.stdin.readline().split())
board = []

for i in range(r):
    temp = list(map(int, sys.stdin.readline().split()))
    board.append(temp)

visited = {}
dq = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
max_c = 0
c = 0

for i in range(r):
    for j in range(col):
        if (i,j) not in visited and board[i][j] == 1:

            dq.append([i,j])
            visited[(i,j)] = 1
            t_cnt = 1
            while dq:
                c_x, c_y = dq.popleft()

                for k in range(4):
                    n_x = c_x + dx[k]
                    n_y = c_y + dy[k]
                    if 0<= n_x < r and 0<= n_y < col and (n_x,n_y) not in visited and board[n_x][n_y] == 1:
                        dq.append([n_x, n_y])
                        visited[(n_x,n_y)] = 1
                        t_cnt += 1
            c+=1
            max_c = max(max_c, t_cnt)

print(c)
print(max_c)
