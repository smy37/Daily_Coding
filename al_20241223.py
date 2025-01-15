import sys
import math
obj, N = map(int, sys.stdin.readline().split())

city_l = {}

for _ in range(N):
    cost, people = map(int, sys.stdin.readline().split())

    if people not in city_l:
        city_l[people] = cost
    else:
        city_l[people] = max(city_l[people], cost)

dp = [math.inf for _ in range(obj+1)]
dp[0] = 0
for k in city_l:
    for i in range(obj):
        idx = min(obj, i+k)

        dp[idx] = min(dp[idx],dp[i]+city_l[k])

print(dp)