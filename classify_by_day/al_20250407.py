import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    c_list = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())

    dp = [0]*(target+1)
    dp[0] = 1

    for c in c_list:
        for i in range(target-c+1):
            dp[i+c] += dp[i]

    print(dp[-1])
