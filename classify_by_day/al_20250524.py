import sys
import math

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = {}
for _ in range(M):
    s, t, w = map(int, sys.stdin.readline().split())
    if s not in graph:
        graph[s] = {}
    if t not in graph[s]:
        graph[s][t] = w
    else:
        graph[s][t] = min(graph[s][t], w)

s, f_t= map(int, sys.stdin.readline().split())

visited = [0  for _ in range(N+1)]
dist = [math.inf  for _ in range(N+1)]

dist[s] = 0
visited[s] = 1
for t in graph[s]:
    dist[t] = graph[s][t]

for _ in range(N-1):
    temp_min = math.inf
    temp_idx = -1
    for i in range(1, N+1):
        if visited[i] == 0 and temp_min > dist[i]:
            temp_min = dist[i]
            temp_idx = i

    visited[temp_idx] = 1
    if temp_idx in graph:
        for t in graph[temp_idx]:
            dist[t] = min(dist[t], dist[temp_idx]+graph[temp_idx][t])
print(dist[f_t])


explain = """
전형적으로 데이크스트라 알고리즘을 이용해서 그래프의 특점 지점으로부터 다른지점까지의 최단 거리를 구하는 문제이다.
Greedy하게 현재 방문하지 않은 노드중에서 최단 거리인 지점을 찾아서 해당 지점으로 이동후 해당 지점에서 다시 방문하지 않은 노드들의 
거리를 갱신하는 방법이다. 
구현시 주의해야할점은 처음 간선의 정보가 주어질때, 특정 노드 s부터 특정 노드 t까지 가는 간선이 여러개 주어질 수 있어서 이중에서 거리가 
최소가 되는 경로만 저장해야하고 특정 노드 s에서 출발하는 간선이 주어지지 않아서 해당 노드 s로 출발하는 간선이 있는지 체크하는 파트가 들어가야한다.
"""