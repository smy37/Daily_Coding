import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
ori_board = []

for _ in range(N):
    ori_board.append(list(map(int, sys.stdin.readline().split())))

after_board = []
for _ in range(N):
    after_board.append(list(map(int, sys.stdin.readline().split())))

move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

dq = deque()
visited = {}
start_idx = {}
start_num = {}
for i in range(N):
    for j in range(M):
        if (i, j) not in visited:
            visited[(i, j)] = 1
            dq.append([i, j, ori_board[i][j]])
            start_idx[(i, j)] = [(i, j)]
            start_num[(i, j)] = ori_board[i][j]
            while dq:
                x, y, num = dq.popleft()

                for k in range(4):
                    n_x, n_y = x+move_x[k], y+move_y[k]
                    if 0<=n_x<N and 0<=n_y<M and (n_x, n_y) not in visited and ori_board[n_x][n_y] == num:
                        visited[(n_x, n_y)] = 1
                        dq.append([n_x, n_y, num])
                        start_idx[(i,j)].append((n_x, n_y))

dq = deque()
visited = {}
after_idx = {}
after_num = {}
flag = True
cnt = 0
for i, j in start_idx:
    if (i, j) not in visited:
        visited[(i, j)] = 1
        dq.append([i, j, after_board[i][j]])
        after_idx[(i, j)] = [(i, j)]
        after_num[(i, j)] = after_board[i][j]
        while dq:
            x, y, num = dq.popleft()

            for k in range(4):
                n_x, n_y = x+move_x[k], y+move_y[k]
                if 0<=n_x<N and 0<=n_y<M and (n_x, n_y) not in visited and after_board[n_x][n_y] == num:
                    visited[(n_x, n_y)] = 1
                    dq.append([n_x, n_y, num])
                    after_idx[(i,j)].append((n_x, n_y))
        if start_idx[(i, j)] != after_idx[(i,j)]:
            flag = False
            break
        else:
            if start_num[(i, j)] != after_num[(i, j)]:
                cnt +=1
if flag and cnt <=1:
    print("YES")
else:
    print("NO")