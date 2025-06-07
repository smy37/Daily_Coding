import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N+1)]
dp[0] = 1

for i in range(N):
    for j in range(1, 7):
        if i+j <= N:
            dp[i+j] += dp[i]*(1/6)
        else:
            dp[N] += dp[i]*(1/6)

print(sum(dp[1:]))

explain = """
dp 배열을 통해서 사탕의 개수가 i개가 될 때의 확률을 dp[i]로 누적해서 구했다. 이때, sum(dp[1:])을 하는 것이 
사탕 개수가 적어도 N개가 되기 위해 던져야 하는 횟수의 기대값이 된다는 것을 귀납적으로 발견해서 적용하였다. 
그러나 이론적으로 왜 되는 지에 대해서는 정확히 이해가 안되서 더욱 고민해봐야 될 것 같다. 
"""