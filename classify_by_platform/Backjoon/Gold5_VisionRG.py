import sys
from collections import deque


N = int(sys.stdin.readline())

board = []
board2 = []
for i in range(N):
    temp = sys.stdin.readline().split()
    board+= temp
    board2.append(temp[0].replace('G', 'R'))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def findArea(N, col_cnt, board):
    visited = {}
    for i in range(N):
        for j in range(N):
            if (i,j) not in visited:
                dq = deque()
                dq.append([i,j])
                visited[(i,j)] = 1
                color = board[i][j]

                col_cnt[color] += 1
                while dq:
                    cur_x, cur_y = dq.popleft()
                    for k in range(4):
                        n_x = cur_x + dx[k]
                        n_y = cur_y + dy[k]
                        if 0<=n_x<N and 0<=n_y<N and (n_x,n_y) not in visited and board[n_x][n_y] == color:
                            visited[(n_x,n_y)] = 1
                            dq.append([n_x,n_y])
    return col_cnt

normal_col_cnt = {'R':0, 'G':0, 'B':0}
print(sum(findArea(N, normal_col_cnt, board).values()), end=' ')

unnormal_col_cnt = {'R':0, 'B':0}
print(sum(findArea(N, unnormal_col_cnt, board2).values()))
