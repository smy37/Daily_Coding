import sys

N, M = map(int, sys.stdin.readline().split())

memory = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
cri = sum(cost)

answer = cri
dp = [[0 for _ in range(cri+1)] for _ in range(N+1)]
for i in range(N):
    m = memory[i]
    c = cost[i]
    for j in range(c):
        dp[i+1][j] = dp[i][j]
    for j in range(c, cri+1):
        dp[i+1][j] = max(dp[i][j], dp[i][j-c]+m)
    for j in range(cri+1):
        if dp[i+1][j] >= M:
            answer = min(answer, j)

print(answer)