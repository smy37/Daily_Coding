import sys
from collections import deque

N, M, T = map(int, sys.stdin.readline().split())

move_r = [1, -1, 0, 0]
move_c = [0, 0, -1, 1]


board = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)

dq = deque()
dq.append([0,0,0,0])
visit = {(0,0,0): True}

answer = float("inf")

while dq:
    x, y, b_gram, time = dq.popleft()
    if x == N - 1 and y == M - 1 and time <= T:
        answer = min(answer, time)
    for i in range(4):
        nx, ny = x + move_r[i], y + move_c[i]

        if 0 <= nx < N and 0 <= ny < M and (nx, ny, b_gram) not in visit:
            if b_gram == 0 and board[nx][ny] != 1:  ## 그램 소유 X
                if board[nx][ny] == 2:
                    visit[(nx, ny, 1)] = True
                    dq.append([nx, ny, 1, time + 1])

                else:
                    visit[(nx, ny, 0)] = True
                    dq.append([nx, ny, 0, time + 1])

            elif b_gram == 1:  ## 그램 소유
                visit[(nx, ny, 1)] = True
                dq.append([nx, ny, 1, time + 1])

if answer == float("inf"):
    print("Fail")
else:
    print(answer)

explain = """
전형적인 그래프 탐색 문제로 BFS를 사용하면 풀 수 있었다. 그람을 소유한 상태와 소유하지 않은 상태를 같은 좌표에 도달하더라도 구분해서 기록해두고
DFS는 상화좌우로 움직이는 상황에서 stack.pop()을 이용하면 각 좌표에 최단 거리로 도달 못하므로 BFS를 사용하는 쪽이 수월하다는 것도 유의해야 한다.
"""