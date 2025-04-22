import sys

N, M = map(int, sys.stdin.readline().split())

pre_reqeust = {i+1: [] for i in range(N)}

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    pre_reqeust[b].append(a)


### Method 1.
# dp = {i+1: 0 for i in range(N)}
# print(pre_reqeust)
#
# flag = True
# while 1:
#     pop_l = []
#     for k in pre_reqeust:
#         if dp[k] == 0:
#             t_max = 0
#             flag = True
#             for i in pre_reqeust[k]:
#                 if dp[i] == 0:
#                     flag = False
#                     break
#                 t_max = max(t_max, dp[i])
#             if flag:
#                 dp[k] = t_max +1
#                 pop_l.append(k)
#     for k in pop_l:
#         del pre_reqeust[k]
#     else:
#         break
#
# print(dp[1:])


### Method 2. Using DFS && DP
dp = {}

def dfs(s):
    cur = s.pop()
    if len(pre_reqeust[cur]) == 0:
        dp[cur] = 1
        return 1

    t_max = 0
    for next in pre_reqeust[cur]:
        if next not in dp:
            temp = dfs(s+[next]) + 1
            t_max = max(t_max, temp)
        else:
            t_max = max(t_max, dp[next] + 1)
    dp[cur] = t_max

    return t_max

for i in range(N):
    dfs([i+1])

print(dp)