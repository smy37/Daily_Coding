import sys
from itertools import combinations
from collections import deque
N, M = map(int, sys.stdin.readline().split())

board = []
chicken_list = []
house_list = {}
for i in range(N):
    t = list(map(int, sys.stdin.readline().split()))
    for j in range(len(t)):
        if t[j] == 2:
            chicken_list.append([i,j])
        elif t[j] == 1:
            house_list[(i,j)] = 1
    board.append(t)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = N**3
for i in combinations(chicken_list, M):

    t_board = [[N**2 for _ in range(N)] for _ in range(N)]
    dq = deque()
    for j in list(i):
        dq.append(j+[0])
        t_board[j[0]][j[1]] = 0
    while dq:
        t = dq.popleft()
        x, y, dist = t[0], t[1], t[2]
        # if (x,y) in house_list:
        #     continue
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0<= nx < N and 0<= ny < N and dist + 1 < t_board[nx][ny]:
                t_board[nx][ny] = dist + 1
                dq.append([nx, ny, dist + 1])
    t_ans = 0
    # print(house_list)
    # for j in t_board:
    #     print(j)
    # print('###################')
    for j in house_list:
        t_ans += t_board[j[0]][j[1]]
    answer = min(answer, t_ans)

print(answer)