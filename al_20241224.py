import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

mod = 1000000003

if int(N/2) < K:
    print(0)
    sys.exit()

answer = 0
dp = [[[0,0] for _ in range(N)] for _ in range(K+1)]

for dp_com in dp[0]:
    dp_com[0] = 1

for j in range(1, N):
    for i in range(1, K+1):
        dp[i][j][0] = (dp[i][j-1][0] + dp[i][j-1][1])%mod
        dp[i][j][1] = (dp[i-1][j-1][0])%mod

answer += sum(dp[-1][-1])

dp = [[[0,0] for _ in range(N-1)] for _ in range(K+1)]
dp[1][0][1] = 1

for j in range(1, N-1):
    for i in range(1, K+1):
        dp[i][j][0] = (dp[i][j - 1][0] + dp[i][j - 1][1])%mod
        dp[i][j][1] = (dp[i - 1][j - 1][0])%mod

answer += sum(dp[-1][-1])

print(answer%mod)
