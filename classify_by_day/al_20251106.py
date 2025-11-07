import sys
import copy

N = int(sys.stdin.readline())

### 1. First Approach
# egg_l = []
# visited = {i: 0 for i in range(N)}

# for _ in range(N):
#     dura, weight = map(int, sys.stdin.readline().split())
#     egg_l.append([dura, weight])

# answer = 0

# def dfs(cur_idx, e_l, visit):
#     global answer
    
#     for i in visit:
#         if visit[i] == 0 and i != cur_idx:
#             n_d = e_l[cur_idx][0]-e_l[i][1]
#             n_e_l = copy.deepcopy(e_l)
#             n_e_l[i][0] -= e_l[cur_idx][1]

#             if n_e_l[i][0] <= 0:
#                 visit[i] = 1

#             if n_d >0:
#                 dfs(cur_idx, n_e_l, visit)
#             else:
#                 visit[cur_idx] = 1
#                 for j in visit:
#                     if visit[j] == 0:
#                         dfs(j, n_e_l, visit)
#                         break
#             answer= max(answer, sum(visit.values()))

#             visit[i] = 0
#             visit[cur_idx] = 0
#     else:
#         answer= max(answer, sum(visit.values()))

# dfs(0, egg_l, visited)
# print(answer)



### 2. Second Approach
weight_l = {}
dura_l = []
visit = {i: 0 for i in range(N)}
for i in range(N):
    dura, weight = map(int, sys.stdin.readline().split())
    weight_l[i] = weight
    dura_l.append(dura)

answer = 0
def dfs(e_l, v):
    global answer
    for i in range(N):
        
        if e_l[i] > 0 and v[i] == 0:
            v[i] = 1
            for j in range(i+1, N):
                if e_l[j] > 0:
                    t_e_l = copy.deepcopy(e_l)
                    t_e_l[i] -= weight_l[j]
                    t_e_l[j] -= weight_l[i]
                    dfs(t_e_l, v)
    cnt = 0
    
    for d in e_l:
        if d <= 0:
            cnt +=1
    answer = max(answer, cnt)
dfs(dura_l, visit)
print(answer)
