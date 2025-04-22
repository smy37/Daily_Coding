import sys

N = int(sys.stdin.readline())

if N == 1:
    print(1)
elif N == 2:
    print(1)
else:
    dp = [1, 0]
    for i in range(N - 2):
        new_dp = [dp[0] + dp[1], dp[0]]
        dp = new_dp

    print(sum(dp))