import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().strip().split())
board = [[5 for _ in range(N)] for _ in range(N)]


plus_food = []
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    plus_food.append(temp)

trees = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, old = map(int, sys.stdin.readline().strip().split())
    trees[x-1][y-1].append(old)

dy = [-1, 0, 1, -1, 1, -1, 0, 1]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
def spring_summer():
    for i in range(N):
        for j in range(N):
            new_tree = deque()
            dead = 0
            for old in trees[i][j]:
                if board[i][j] >= old:
                    board[i][j] -= old
                    new_tree.append(old+1)
                else:
                    dead += (old//2)
            trees[i][j] = new_tree
            board[i][j] += dead
def autumn_winther():
    new_tree2 = []
    for i in range(N):
        for j in range(N):
            for old in trees[i][j]:
                if old % 5 == 0:
                    for k in range(8):
                        nx, ny = i + dx[k], j + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            new_tree2.append([nx, ny])
    for i in new_tree2:
        x, y = i[0], i[1]
        trees[x][y].appendleft(1)

    for i in range(N):
        for j in range(N):
            board[i][j] += plus_food[i][j]
for year in range(K):
    spring_summer()
    autumn_winther()

cnt = 0
for i in range(N):
    for j in range(N):
        cnt += len(trees[i][j])
print(cnt)