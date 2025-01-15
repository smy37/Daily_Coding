import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coin_l = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())

    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    for i in range(N):
        coin = coin_l[i]
        for j in range(target-coin+1):
            dp[j+coin] += dp[j]

    print(dp[-1])