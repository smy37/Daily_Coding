import sys
from collections import deque
K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().strip().split())
board = []
visited = [[[1 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]

for _ in range(H):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    board.append(temp)

if W== 1 and H == 1:
    print(0)
    sys.exit()

dx = [0,0,-1,1,  -1,1, -1,1, -2,-2, 2,2, ]
dy = [-1,1,0,0,  -2,-2, 2,2, -1,1, -1,1, ]
dq = deque()
dq.append([[0,0],K, 0])     ## [Cur_Position:list, Rest_HorseMoving:int, Accum_Step:int]
visited[0][0][K] = 1
answer = (W*H+1)*1000
def bfs():
    global answer
    flag = False
    while dq:
        temp = dq.popleft()
        c_x,c_y = temp[0][0], temp[0][1]
        rest_horse_move = temp[1]
        accum_step = temp[2]

        if rest_horse_move > 0: ## can move like horse
            for i in range(12):
                n_x, n_y = c_x+dx[i], c_y+dy[i]
                if 0<=n_x < W and 0<=n_y < H and board[n_y][n_x] != 1:
                    if i < 4:
                        if visited[n_y][n_x][rest_horse_move]:
                            dq.append([[n_x, n_y], rest_horse_move, accum_step + 1])
                            visited[n_y][n_x][rest_horse_move] = 0
                            if n_x == W - 1 and n_y == H - 1:
                                answer = min(answer, accum_step + 1)
                                flag = True
                    else:
                        if visited[n_y][n_x][rest_horse_move-1]:
                            dq.append([[n_x,n_y],rest_horse_move-1, accum_step+1])
                            visited[n_y][n_x][rest_horse_move-1] = 0
                            if n_x == W - 1 and n_y == H - 1:
                                answer = min(answer, accum_step + 1)
                                flag = True
        else:   ## can't move like horse
            for i in range(4):
                n_x, n_y = c_x+dx[i], c_y+dy[i]
                if 0<=n_x < W and 0<=n_y < H and board[n_y][n_x] != 1:
                    if visited[n_y][n_x][rest_horse_move]:
                        dq.append([[n_x,n_y],rest_horse_move, accum_step+1])
                        visited[n_y][n_x][rest_horse_move] = 0
                        if n_x == W-1 and n_y == H-1:
                            answer = min(answer, accum_step + 1)
                            flag = True
    if flag:
        return answer

    else:
        return -1

print(bfs())