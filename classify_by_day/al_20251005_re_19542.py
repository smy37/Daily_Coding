import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, S, D = map(int, sys.stdin.readline().split())

tree = {}
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    if a not in tree:
        tree[a] = {}
    if b not in tree:
        tree[b] = {}
    tree[a][b] = True
    tree[b][a] = True


### 1. First Approach
# answer = 0
# stack = [[S, D]]
# visited = {S: True}
# def dfs(s):
#     global answer
#     cur_n, r_d = s.pop()

#     if cur_n in tree:
#         for next_n in tree[cur_n]:
#             if next_n not in visited:
#                 visited[next_n] = True
#                 if r_d == 0:
#                     answer += 2
#                     dfs(s+[[next_n, D]])
#                 else:
#                     dfs(s+[[next_n, r_d-1]])

# dfs(stack)
# print(answer)

### 2. Second Approach
# check_point = {}
# visited = {S: True}
# stack = [S]
# def dfs(s):
#     cur_n = s.pop()
    
#     flag = False
#     temp_d = 0
#     for next_n in tree[cur_n]:
#         if next_n not in visited:
#             visited[next_n] = True
#             cul_d = dfs(s+[next_n])
#             temp_d = max(temp_d, cul_d)
#             if D == cul_d:
#                 check_point[cur_n] = True
#                 flag = True
#     if flag:
#         return 0
#     else:
#         return temp_d+1

# dfs(stack)
# if len(check_point) == 0 and D == 0:
#     check_point = {i+1: True for i in range(N) if i+1 != S}


# answer = 0
# dq = deque()
# dq.append([S, 0])
# visited = {S: True}
# dist_check_point = {}
# while dq:
#     cur_n, cur_dist = dq.popleft()
#     for next_n in tree[cur_n]:
#         if next_n not in visited:
#             visited[next_n] = True
#             if next_n in check_point:
#                 dist_check_point[next_n] = True
                
#                 answer += 2*(cur_dist+1)
#                 if len(dist_check_point) == len(check_point):
#                     print(answer)
#                     sys.exit()
#                 dq.append([next_n, 0])
#                 cur_dist = 0
#             else:
#                 dq.append([next_n, cur_dist+1])

# print(answer)

### 3. Third Approach
answer = 0
visited = {S: True}
depth = {i+1:0 for i in range(N)}
stack = [S]
def dfs(s):
    global answer

    cur_n = s.pop()
    for next_n in tree[cur_n]:
        if next_n not in visited:
            visited[next_n] = True
            temp_depth = dfs(s+[next_n])
            depth[cur_n] = max(depth[cur_n], temp_depth+1)
    if depth[cur_n] >= D and cur_n != S:
        answer += 1
    return depth[cur_n]

dfs(stack)
print(answer*2)

explain = """
발상의 전환이 필요했는데 계속 유사한 생각으로 시간도 오래걸리고 트라이를 여러번 하였다.
루트에서 이동거리를 누적하면서 D 이상인 노드를 찾는다는 생각 대신에 리프 노드를 기준으로
가장 말단에 속하는 노드를 구해서 해당 노드를 가기 위해 걸리는 거리의 2배를 해주는 식으로 
구해줘야 했다. 이때, 한 노드에서 가지가 쳐지는 것들의 max 값으로 처리해 주는 것도 중요하였다.
"""
