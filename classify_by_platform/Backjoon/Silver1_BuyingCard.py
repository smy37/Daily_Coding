import sys

N = int(sys.stdin.readline())
board = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N)]
dp[0] = board[0]

for i in range(1,N):
    t_max = 0
    if i%2 == 0:
        for j in range(i//2):
            t_max = max(t_max, dp[j]+dp[i-j-1])
    else:
        for j in range(i//2):
            t_max = max(t_max, dp[j] + dp[i-j-1])
        t_max = max(t_max, 2*dp[i//2])

    t_max = max(t_max, board[i])
    dp[i] = t_max

print(dp[-1])