import sys
import copy
N, M = map(int, sys.stdin.readline().split())
board = []
camera = []
for i in range(N):
    t = list(map(int, sys.stdin.readline().split()))
    board.append(t)
    for j in range(len(t)):
        if 1<= t[j] <=5:
            camera.append([i,j])
def count_board(b):
    cnt = 0
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                cnt +=1
    return cnt

answer = N*M
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]



def check_camera(p_board, camera_l):
    global answer
    if len(camera_l) == 0:
        answer = min(answer, count_board(p_board))
        return
    t_c = camera_l[-1]
    t_camera_l = camera_l[:-1]

    t_x, t_y = t_c[0], t_c[1]
    cri = board[t_x][t_y]

    if cri == 1:
        for i in range(4):
            t_board = copy.deepcopy(p_board)
            t_board[t_x][t_y] = '#'
            n_x = t_x + dx[i]
            n_y = t_y + dy[i]
            while (0<=n_x<N and 0<=n_y<M and board[n_x][n_y] != 6):
                t_board[n_x][n_y] = '#'
                n_x += dx[i]
                n_y += dy[i]
            check_camera(t_board, t_camera_l)

    elif cri == 2:
        for i in range(2):
            t_board = copy.deepcopy(p_board)
            t_board[t_x][t_y] = '#'
            if i == 0:
                n_x = t_x + dx[0]
                n_y = t_y + dy[0]
                while (0 <= n_x < N and 0 <= n_y < M and board[n_x][n_y] != 6):
                    t_board[n_x][n_y] = '#'
                    n_x += dx[0]
                    n_y += dy[0]
                n_x = t_x + dx[1]
                n_y = t_y + dy[1]
                while (0 <= n_x < N and 0 <= n_y < M and board[n_x][n_y] != 6):
                    t_board[n_x][n_y] = '#'
                    n_x += dx[1]
                    n_y += dy[1]
            elif i == 1:
                n_x = t_x + dx[2]
                n_y = t_y + dy[2]
                while (0 <= n_x < N and 0 <= n_y < M and board[n_x][n_y] != 6):
                    t_board[n_x][n_y] = '#'
                    n_x += dx[2]
                    n_y += dy[2]

                n_x = t_x + dx[3]
                n_y = t_y + dy[3]
                while (0 <= n_x < N and 0 <= n_y < M and board[n_x][n_y] != 6):
                    t_board[n_x][n_y] = '#'
                    n_x += dx[3]
                    n_y += dy[3]
            check_camera(t_board, t_camera_l)
    elif cri == 3:
        for i in [[0,3],[0,2], [1,2],[1,3]]:
            t_board = copy.deepcopy(p_board)
            t_board[t_x][t_y] = '#'
            for j in i:
                n_x = t_x + dx[j]
                n_y = t_y + dy[j]
                while (0 <= n_x < N and 0 <= n_y < M and board[n_x][n_y] != 6):
                    t_board[n_x][n_y] = '#'
                    n_x += dx[j]
                    n_y += dy[j]
            check_camera(t_board, t_camera_l)
    elif cri == 4:
        for i in [[0,2,3],[0,1, 2], [1,2, 3],[0, 1,3]]:
            t_board = copy.deepcopy(p_board)
            t_board[t_x][t_y] = '#'
            for j in i:
                n_x = t_x + dx[j]
                n_y = t_y + dy[j]
                while (0 <= n_x < N and 0 <= n_y < M and board[n_x][n_y] != 6):
                    t_board[n_x][n_y] = '#'
                    n_x += dx[j]
                    n_y += dy[j]
            check_camera(t_board, t_camera_l)
    elif cri == 5:
        t_board = copy.deepcopy(p_board)
        t_board[t_x][t_y] = '#'
        for j in range(4):
            n_x = t_x + dx[j]
            n_y = t_y + dy[j]
            while (0 <= n_x < N and 0 <= n_y < M and board[n_x][n_y] != 6):
                t_board[n_x][n_y] = '#'
                n_x += dx[j]
                n_y += dy[j]
        check_camera(t_board, t_camera_l)

check_camera(board, camera)
print(answer)