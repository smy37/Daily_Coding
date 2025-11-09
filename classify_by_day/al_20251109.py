import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
virus = []
board = []

move_x = [1, -1, 0, 0]
move_y = [0, 0, -1, 1]

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)

    for j in range(N):
        if row[j] != 0:
            virus.append([i, j, row[j], 0])

S, X, Y = map(int, sys.stdin.readline().split())

virus = sorted(virus, key=lambda x : x[2])
dq = deque(virus)

while dq:
    x, y, v_n, s = dq.popleft()

    if s < S:
        for i in range(4):
            n_x, n_y = x+move_x[i], y+move_y[i]
            if 0<=n_x<N and 0<=n_y<N and board[n_x][n_y] == 0:
                board[n_x][n_y] = v_n
                dq.append([n_x, n_y, v_n, s+1])

print(board[X-1][Y-1])

explain = """
queue에 바이러스의 좌표와 바이러스 번호, 그리고 시각을 넣어주 준 후 S초 까지 BFS를 진행해서 board를 업데이트 해준다.
업데이트가 끝난 후, X,Y의 값을 조회한다.
"""