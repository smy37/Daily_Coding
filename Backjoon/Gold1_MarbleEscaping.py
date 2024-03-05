import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

board = []

b_idx = [0,0]
r_idx = [0,0]
out_idx = [0,0]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for j in range(N):
    t = sys.stdin.readline()
    t_l = []
    cnt = 0
    for i in t:
        if i == '#':
            t_l.append(-1)
        elif i == '.':
            t_l.append(0)
        elif i == 'B':
            b_idx = [j, cnt]
            t_l.append(0)
        elif i == 'R':
            r_idx = [j, cnt]
            t_l.append(0)
        elif i== 'O':
            out_idx = [j, cnt]
            t_l.append(-2)

        cnt +=1

    board.append(t_l)

dq = deque()
dq.append([r_idx, b_idx, 0])

while dq:
    t = dq.popleft()
    r_cur = t[0]
    b_cur = t[1]
    dist = t[2]
    r_x, r_y = r_cur[0], r_cur[1]
    b_x, b_y = b_cur[0], b_cur[1]

    if dist == 10:
        continue
    for i in range(4):
        flag = False
        flag2 = False
        r_nx, r_ny = r_x, r_y
        b_nx, b_ny = b_x, b_y
        if i == 0:  ## 위로 기울이기
            for j in range(N):
                r_nx =r_nx - 1
                if board[r_nx][r_ny] == -1:
                    r_nx += 1
                    break
                elif board[r_nx][r_ny] == -2:
                    flag = True
                    break
            for j in range(N):
                b_nx =b_nx - 1
                if board[b_nx][b_ny] == -1:
                    b_nx += 1
                    break
                elif board[b_nx][b_ny] == -2:
                    flag2 = True
                    break
        elif i == 1:  ## 아래로 기울이기
            for j in range(N):
                r_nx = r_nx + 1
                if board[r_nx][r_ny] == -1:
                    r_nx -= 1
                    break
                elif board[r_nx][r_ny] == -2:
                    flag = True
                    break
            for j in range(N):
                b_nx = b_nx + 1
                if board[b_nx][b_ny] == -1:
                    b_nx -= 1
                    break
                elif board[b_nx][b_ny] == -2:
                    flag2 = True
                    break
        elif i == 2:  ## 왼쪽로 기울이기
            for j in range(M):
                r_ny  = r_ny -1
                if board[r_nx][r_ny] == -1:
                    r_ny += 1
                    break
                elif board[r_nx][r_ny] == -2:
                    flag = True
                    break
            for j in range(M):
                b_ny = b_ny - 1
                if board[b_nx][b_ny] == -1:
                    b_ny += 1
                    break
                elif board[b_nx][b_ny] == -2:
                    flag2 = True
                    break
        elif i == 3:  ## 오른쪽로 기울이기
            for j in range(M):
                r_ny = r_ny + 1
                if board[r_nx][r_ny] == -1:
                    r_ny -= 1
                    break
                elif board[r_nx][r_ny] == -2:
                    flag = True
                    break
            for j in range(M):
                b_ny = b_ny + 1
                #print(t, b_x, b_y, b_ny)
                if board[b_nx][b_ny] == -1:
                    b_ny -= 1
                    break
                elif board[b_nx][b_ny] == -2:
                    flag2 = True
                    break

        if flag and flag2:
            continue
        elif flag:
            print(dist+1)
            sys.exit()
        elif flag2:
            continue

        # r_nx = max(0, r_nx)
        # r_nx = min(N-1, r_nx)
        #
        # r_ny = max(0, r_ny)
        # r_ny = min(M-1, r_ny)
        #
        # b_nx = max(0, b_nx)
        # b_nx = min(N - 1, b_nx)
        #
        # b_ny = max(0, b_ny)
        # b_ny = min(M - 1, b_ny)

        if [r_nx, r_ny] == [b_nx, b_ny]:
            if i == 0:
                    if r_x > b_x:
                        r_nx += 1
                    else:
                        b_nx += 1
            elif i == 1:
                    if r_x > b_x:
                        b_nx -= 1
                    else:
                        r_nx -= 1
            elif i == 2:
                    if r_y > b_y:
                        r_ny += 1
                    else:
                        b_ny += 1
            elif i == 3:
                    if r_y > b_y:
                        b_ny -= 1
                    else:
                        r_ny -= 1

        dq.append([[r_nx,r_ny],[b_nx,b_ny],dist +1])

print(-1)