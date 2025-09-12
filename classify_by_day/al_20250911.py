import sys
import copy

c, m = map(int, sys.stdin.readline().split())

### 1. First Approach
# dp = list(map(int, sys.stdin.readline().split()))
# for _ in range(m-1):
#     cur_m = list(map(int, sys.stdin.readline().split()))
#     for i in range(c):
#         for j in range(c-i-1):
#             dp[i+j+1] = max(dp[i+j+1], dp[j]+cur_m[i])
#
# print(max(dp))

### 2. Second Approach
dp = [0]*(c+1)
cur_m = list(map(int, sys.stdin.readline().split()))
for i in range(c):
    dp[i + 1] = max(dp[i + 1], cur_m[i])
for _ in range(m-1):
    cur_m = list(map(int, sys.stdin.readline().split()))
    new_dp = copy.deepcopy(dp)
    for i in range(c):
        dp[i+1] = max(dp[i+1], cur_m[i])
    for i in range(c):
        for j in range(c-(i)):
            if dp[j] > 0:
                dp[j+i+1] = max(dp[j+i+1], cur_m[i]+dp[j])
    print(dp)
print(dp)