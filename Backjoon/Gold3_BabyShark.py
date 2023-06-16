import sys
from collections import deque

N = int(sys.stdin.readline().strip())

m_x = [-1, 0, 0, 1]
m_y = [0, -1, 1, 0]

answer = 0
t_n = 0

fish_board = []
shark = []
cur = []
size = 2
size_up = 0
dq = deque()
visited = {}

for i in range(N):
    temp = list(map(int, sys.stdin.readline().strip().split(' ')))
    fish_board.append(temp)
    for j in range(len(temp)):
        if temp[j] == 9:
            cur = [i, j]


dq.append(cur)
visited[tuple(cur)] = 0
fish_board[cur[0]][cur[1]] = 0

while 1:

    temp = []
    while dq:
        t = dq.popleft()
        for i in range(4):
            n_x = t[0] + m_x[i]
            n_y = t[1] + m_y[i]
            if 0<= n_x < N and 0<= n_y < N:
                if (n_x, n_y) not in visited:
                    if 0 < fish_board[n_x][n_y] < size:
                        visited[(n_x, n_y)] = visited[(t[0], t[1])] + 1
                        dq.append([n_x,n_y])
                        temp.append([visited[(n_x,n_y)], n_x, n_y])
                    elif fish_board[n_x][n_y] == 0 or fish_board[n_x][n_y] == size:
                        dq.append([n_x,n_y])
                        visited[(n_x,n_y)] = visited[(t[0],t[1])] + 1

                        # print(f"Case2 : {t_n}, 현재위치: {n_x}, {n_y}")
    if len(temp) == 0:
        break
    else:
        temp = sorted(temp, key = lambda x : (x[0], x[1], x[2]))
        next = temp[0]
        answer += next[0]
        size_up += 1
        fish_board[next[1]][next[2]] = 0
        visited = {}
        visited[(next[1], next[2])] = 0
        dq = deque()
        dq.append([next[1], next[2]])

        if size_up == size:
            size += 1
            size_up = 0

print(answer)