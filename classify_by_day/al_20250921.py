import sys

N = int(sys.stdin.readline())
stone_l = list(map(int, sys.stdin.readline().split()))


### 1. Fisrt Approach
# dp = [[0 for _ in range(N)] for _ in range(N)]

# answer = 0

# for i in range(N):
#     if stone_l[i] == 1:
#         dp[i][i] = 1
#     else:
#         dp[i][i] = -1
#     for j in range(i+1, N):
#         if stone_l[j] == 1:
#             dp[i][j] = dp[i][j-1] +1
#         else:
#             dp[i][j] = dp[i][j-1] -1
#     answer = max(answer, max(dp[i]), abs(min(dp[i])))

# print(answer)

### 2. Second Approach
left_max = 0
cur = 0
for i in range(N):
    if stone_l[i] == 1:
        cur = max(1, cur+1)
    elif stone_l[i] == 2:
        cur = max(0, cur-1)
    left_max = max(left_max, cur)


right_max = 0
cur = 0
for i in range(N):
    if stone_l[i] == 2:
        cur = max(1, cur+1)
    elif stone_l[i] == 1:
        cur = max(0, cur-1)
    left_max = max(left_max, cur)
  
print(max(left_max, right_max))

explain = """
처음 시도에서는 DP를 이용하여 구간합을 저장하였지만 메모리 초과가 발생하였다. 
두번째 시도에서는 오른쪽을 향하는 석상들을 잇는 것 한번과 왼쪽을 향하는 석상들을 잇는 것 한번
총 2번의 카운트르 통해 최대값을 구하는 방법을 사용하였다. 그리고 연속된 구간합의 최대가 한번의 순회동안에
매 순간 최대값을 체크함으로써 구해질 수 있음을 이용한다.
"""