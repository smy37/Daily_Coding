import sys
from collections import deque



N = int(sys.stdin.readline().strip())
board = [[0 for _ in range(N)] for _ in range(N)]
apple_num = int(sys.stdin.readline().strip())
for i in range(apple_num):
    r, c = map(int, sys.stdin.readline().strip().split())
    board[r-1][c-1] = 2
event_num = int(sys.stdin.readline())
event = {}
for i in range(event_num):
    t = sys.stdin.readline().strip().split()
    event[int(t[0])] = t[1]

cur_t = 0

cur_x = 0
cur_y = 0

dx = 0
dy = 1
s_body = deque()
s_body.append([0,0])
while 1:
    n_x = cur_x + dx
    n_y = cur_y + dy
    cur_t += 1
    if 0<= n_x < N and 0<= n_y < N:
        if board[n_x][n_y] == 1: ## contact snake body
            # print(board, n_x, n_y)
            # print(cur_t, "case1")
            print(cur_t)
            sys.exit()
        elif board[n_x][n_y] == 2: ## contact apple
            board[n_x][n_y] = 1
            s_body.append([n_x,n_y])
        elif board[n_x][n_y] == 0: ## contact void space
            board[n_x][n_y] = 1
            s_body.append([n_x, n_y])
            tail = s_body.popleft()
            board[tail[0]][tail[1]] = 0
        cur_x = n_x
        cur_y = n_y
        if cur_t in event:
            if event[cur_t] == "D":
                t_dy = int(dy)
                dy = -1*dx
                dx = t_dy
            elif event[cur_t] == "L":
                t_dy = int(dy)
                dy = dx
                dx = -1*t_dy
    else:
        # print(board, n_x, n_y)
        # print(cur_t, "case2")
        print(cur_t)
        sys.exit()