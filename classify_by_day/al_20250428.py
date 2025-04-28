import sys
import math

N = int(sys.stdin.readline())

board = []

for _ in range(N):
    t = list(sys.stdin.readline().split())
    for i in range(len(t)):
        if t[i].isdigit():
            t[i] = int(t[i])
    board.append(t)

dp = []
for i in range(N):
    t = [[-math.inf, math.inf] for _ in range(N)]
    dp.append(t)

move_l = [[1, 0], [0, 1]]

s = [(0, 0)]
dp[0][0][0] = board[0][0]
dp[0][0][1] = board[0][0]

while s:
    t = s.pop()
    for i in range(2):
        nx, ny = t[0] + move_l[i][0], t[1] + move_l[i][1]
        if 0<= nx < N and 0 <= ny < N:
            if isinstance(board[nx][ny], int):
                px, py = t[2]
                value_max = eval(f"{dp[px][py][0]}{t[3]}{board[nx][ny]}")
                value_min = eval(f"{dp[px][py][1]}{t[3]}{board[nx][ny]}")

                dp[nx][ny][0] = max(dp[nx][ny][0], value_max)
                dp[nx][ny][1] = min(dp[nx][ny][1], value_min)
                s.append((nx, ny))
            else:
                s.append((nx, ny, [t[0], t[1]], board[nx][ny]))


for k in dp[-1][-1]:
    print(k, end=" ")
    

## 그래프 알고리즘과 Dynamic Programming을 조합해서 사용하는 전형적인 문제...
## 좌상단에서 우하단까지 최단거리로 이동하므로 하, 우의 이동만 고려하였고 문자열에 대해서 피연산자와 연산자를 넣고 eval() 함수로 계산된 값을 얻어
## DP에 저장하였다. DP에는 최대값과 최솟값을 저장하였고 BFS를 통해 그래프를 탐색하였으며 현재 Node가 연산자일 때와, 피연산자일 때 
## 스택에 넣는 값을 달리하였다.