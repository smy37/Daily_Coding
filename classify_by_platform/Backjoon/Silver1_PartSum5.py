import sys
N, M = map(int, sys.stdin.readline().split())

board = []
for i in range(N):
    t = list(map(int, sys.stdin.readline().split()))
    board.append(t)

dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    dp[i][0] = board[i][0]

for i in range(N):
    if i != 0:
        for j in range(1, N):
            dp[i][j] = dp[i][j-1] + board[i][j]
        for j in range(0, N):
            dp[i][j] += dp[i-1][j]
    else:
        for j in range(1, N):
            dp[i][j] = dp[i][j-1] + board[i][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1> 1:
        result = dp[x2-1][y2-1] - dp[x1-1-1][y2-1]
    else:
        result = dp[x2-1][y2-1]
    if y1 > 1:
        if x1 > 1:
            result -= (dp[x2-1][y1-1-1]-dp[x1-1-1][y1-1-1])
        else:
            result -= dp[x2-1][y1-1-1]
    print(result)