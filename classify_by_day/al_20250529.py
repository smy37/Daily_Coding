import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

### 1. First Approach
# def bfs(s_num, graph):
#     sum_n = 0
#     dq = deque()
#     dq.append(s_num)
#     visited = {s_num:1}
#
#     while dq:
#         t = dq.popleft()
#         if t in graph:
#             for n in graph[t]:
#                 if n not in visited:
#                     sum_n += 1
#                     dq.append(n)
#                     visited[n] = 1
#     return sum_n
#
# in_graph = {}
# out_graph = {}
# for _ in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     if a not in out_graph:
#         out_graph[a] = {}
#     out_graph[a][b] = 1
#     if b not in in_graph:
#         in_graph[b] = {}
#     in_graph[b][a] = 1
#
#
# for i in range(1, N+1):
#     left = bfs(i, in_graph)
#     right = bfs(i, out_graph)
#     print(N- (left+right)-1)



### 2. Second Approach
graph = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] =1

for i in range(N):
    connect = 0
    for j in range(N):
        if graph[i][j] == 1 or graph[j][i] == 1:
            connect += 1

    print(N-connect-1)


explain= """
얼핏 생각하면 엣지의 방향성이 중요하지 않다고 생각해서 BFS나 DFS를 통해서 찾으면 될거라고 생각하지만 실제로는 방향성을 생각해서
나가는 방향으로 BFS 한번, 들어오는 방향으로 BFS 한번을 통해서 답을 구할 수 있다. 즉, 무게를 안다는 것은 방향성을 가지고 그래프를 탐색했을때, 
도달할 수 있어야 된다는 것과 같다.
그러나 Node의 개수가 500개 이하이기 때문에 플로이드-워셜 알고리즘을 응용한다면 더 빠르게 답을 구할 수 있다.
모든 정점간의 최단 거리를 구하는 알고리즘인데 특정 노드에서 특정 노드를 갈 때, 중간에 다른 노드를 끼고 가는 모든 경우의 수를 고려하는 방법이다.
방향성을 가져야 하기 때문에 첫번째, M개의 a,b를 받았을때, 한쪽 방향으로만 엣지를 연결해주었고 i가 j보다 가벼운지 무거운지를 알아야 하므로
graph[i][j] ==1 or graph[j][i] ==1 을 하였다.
"""