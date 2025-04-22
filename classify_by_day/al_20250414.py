import sys
str_1 = sys.stdin.readline().strip()
str_2 = sys.stdin.readline().strip()


### 1. 첫번째 시도
# if len(str_1) <= len(str_2):
#     min_s = str_1
#     max_s = str_2
# else:
#     min_s = str_2
#     max_s = str_1
#
# answer = 0
# for i in range(len(min_s)):
#     flag = False
#     for j in range(len(max_s)):
#         if min_s[i] == max_s[j]:
#             cur= 1
#             while 1:
#                 if i+cur >= len(min_s) or j+cur >= len(max_s) or min_s[i+cur] != max_s[j+cur]:
#                     answer = max(answer, cur)
#                     break
#                 cur += 1
# print(answer)

### 2. 두번쨰 시도
n, m = len(str_1), len(str_2)
str_1 = "."+str_1
str_2 = "."+str_2

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if str_1[i] == str_2[j]:
            dp[i][j] = dp[i-1][j-1]+1

answer = 0
for i in dp:
    answer = max(answer, max(i))
print(answer)