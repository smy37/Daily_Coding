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
dp = [-float("inf")]*(c+1)
dp[0] = 0

for _ in range(m):
    new_dp = copy.deepcopy(dp)
    cur_m = list(map(int, sys.stdin.readline().split()))

    for i in range(c):
        for j in range(c-(i)):
            if dp[j] != -float("inf"):
                new_dp[j+i+1] = max(new_dp[j+i+1], cur_m[i]+dp[j])
    dp = new_dp

print(max(dp))

explain = """
0번째 항을 0으로 초기화 해주고 dp[j] != -float("inf") 조건으로 하는게 중요하다.
특정 상인에게서 구매를 시작하는 조건을 위해서는 dp[0] = 0가 필요하다. 또한 != -float("inf") 조건이 없으면
구매 상태가 없는데도 이어서 구매를 하게 되므로 추가해줘야 한다. 
"""