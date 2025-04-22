import sys

n = int(sys.stdin.readline())
w_l = sorted(list(map(int, sys.stdin.readline().split())))


### 1. 첫번째 접근 방법
# upper_limit = sum(w_l)
#
# dp = [0 for _ in range(upper_limit+1)]
# report = [0 for _ in range(upper_limit+1)]
# for i in range(n):
#     dp[0] = 1
#
#
# for w in w_l:
#     for j in range(upper_limit, w-1, -1):
#         dp[j] += dp[j-w]
#
# for i in range(upper_limit+1):
#     if dp[i] == 0:
#         print(i)
#         break



### 2. 풀이를 참고한 접근 방법
num_sum = 0

for w in w_l:
    if num_sum + 1 < w:
        print(num_sum +1)
        break
    num_sum += w
else:
    print(num_sum + 1)