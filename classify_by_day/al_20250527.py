import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

dp = [[0,0] for _ in range(N+1)]
for _ in range(M):
    V = int(sys.stdin.readline())
    dp[V][1] = -1
dp[0][1] = 1

for i in range(1, N+1):
    if dp[i-1][1] == -1:
        dp[i][0] = dp[i-1][0]
    else:
        if dp[i][1] == -1:
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
        else:
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0]

answer = sum(dp[-1]) if dp[-1][1] !=-1 else dp[-1][0]
print(answer)

explain ="""
전형적인 dp 문제로 bottom-up 형식으로 배열을 갱신해 나가면 되는 문제이다. 
현재 조회하는 좌석을 갱신해 줄 때, 이전 좌석에서 좌석을 그대로 앉은 경우와 교환해서 앉은 경우일때, 다르게 갱신해주면 된다.
"""