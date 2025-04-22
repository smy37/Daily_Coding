import sys

dp = [0 for _ in range(31)]
dp[0] = 1
dp[1] = 1
for i in range(2, 31):
    for j in range(i):
        dp[i] += dp[j]*dp[i-1-j]

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    print(dp[n])