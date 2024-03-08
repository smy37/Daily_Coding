import sys

n, k = map(int, sys.stdin.readline().split())

c_list = []

for i in range(n):
    c_list.append(int(sys.stdin.readline()))

c_list = sorted(c_list, reverse=True)

dp = [0 for _ in range(k+1)]
dp[0] = 1

for c in c_list:
    for j in range(k-c+1):
        dp[j+c] += dp[j]

print(dp[-1])