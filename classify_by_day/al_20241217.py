import sys

T, N = map(int, sys.stdin.readline().split())
dp = [0 for _ in range(T+1)]

for _ in range(N):
    w, t = map(int, sys.stdin.readline().split())

    for i in range(T-t, -1, -1):
        dp[i+t] = max(dp[i+t], dp[i]+w)

print(max(dp))