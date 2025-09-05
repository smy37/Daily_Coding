import sys 
from collections import deque

N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    row = sys.stdin.readline()
    board.append(row)

score = [[0 for _ in range(M)] for _ in range(N)]

mv_x = [-1, 1, 0, 0]
mv_y = [0, 0, -1, 1]



answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == "L":
            dq = deque()
            visited = {}
            temp_answer = 0
            dq.append((i, j, 0))
            visited[(i, j)] = 1

            while dq:
                x, y, w = dq.popleft()
                temp_answer = max(temp_answer, w)
                for k in range(4):
                    nx, ny = x+mv_x[k], y + mv_y[k]
                    if 0<=nx<N and 0<=ny<M and (nx, ny) not in visited and board[nx][ny] == "L":
                        visited[(nx, ny)] = 1
                        dq.append((nx, ny, w+1))
            answer = max(answer, temp_answer)

print(answer)

explain = """"
모든 노드에 대하여 BFS를 실행하여 해당 노드에서 가장 멀리 있는 노드까지의 거리를 갱신하면 된다.
"""