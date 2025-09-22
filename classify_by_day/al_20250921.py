import sys

N = int(sys.stdin.readline())
stone_l = list(map(int, sys.stdin.readline().split()))

dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    if stone_l[i] == 1:
        dp[i][0] = 1
    else:
        dp[i][0] = -1
    for j in range(1, N):
        if dp[i][j] == 1:
            dp[i][j] = dp[i][j-1] +1
        else:
            dp[i][j] = dp[i][j-1] -1

print(dp)