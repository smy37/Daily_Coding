import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = {}
weight_l = []
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    if A not in graph:
        graph[A] = {}
    if B not in graph:
        graph[B] = {}
    if B not in graph[A]:
        graph[A][B] = 0
    if A not in graph[B]:
        graph[B][A] = 0

    graph[A][B] = max(graph[A][B], C)
    graph[B][A] = max(graph[B][A], C)
    weight_l.append(C)
s, t = map(int, sys.stdin.readline().split())

### 1. First Approach -> DFS + Backtracking
# stack = [s]
# answer = 0
# visited = {s: True}
# def dfs(cur_s, cur_cri, visited, target):
#     global answer
#     n = cur_s.pop()
#     if n == target:
#         answer = max(answer, cur_cri)
#
#     for next_n in graph[n]:
#         if next_n not in visited:
#             visited[next_n] = True
#             dfs(cur_s+[next_n], min(cur_cri, graph[n][next_n]), visited, target)
#             del visited[next_n]
#
# dfs(stack, float("inf"), visited, t)
# print(answer)

### 2. Second Approach -> Binary Search + BFS
def check(cri):
    dq = deque()
    dq.append(s)
    visited = {s:1}
    flag = False
    while dq:
        cur_t = dq.popleft()
        if cur_t == t:
            flag = True
            break
        for next_n in graph[cur_t]:
            if next_n not in visited and graph[cur_t][next_n] >=cri:
                visited[next_n] = 1
                dq.append(next_n)
    return flag

weight_l.sort()
start, end = 0, len(weight_l)-1
answer = 0
while start <= end:
    mid = (start+end)//2

    b_possible = check(weight_l[mid])

    if b_possible:
        start = mid+1
        answer = max(answer, weight_l[mid])
    else:
        end = mid-1

print(answer)
explain = """
첫번째 시도에서는 백트래킹 + DFS를 이용하여 갈 수 있는 모든 경로에 대해서 허용 하중이 최대인 값을 찾았다. 
그러나 시간초과가 발생하여, 교각의 허용 하중을 배열에 담고 해당 배열에 이분 탐색을 진행하며 해당 허용 하중에서
출발지부터 목적지까지 이동 가능한지 BFS를 통해 검증하였다.
"""
