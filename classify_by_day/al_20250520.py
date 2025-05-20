import sys
from collections import deque
graph = {}

try:
    while True:
        line = sys.stdin.readline()
        a, b, d = map(int, line.strip().split())
        if a not in graph:
            graph[a] = {}
        if b not in graph:
            graph[b] = {}
        graph[a][b] = d
        graph[b][a] = d
except:
    pass

if not graph:
    print(0)
    sys.exit()

### Try 1. Leaf Node Strat
# start = []
# for a in graph:
#     if len(graph[a]) == 1:
#         start.append(a)
#
# answer = 0
# for s_n in start:
#     dq = deque()
#     dq.append([s_n, 0])
#     visited = {s_n:1}
#     while dq:
#         t, d = dq.popleft()
#
#         for n_n in graph[t]:
#             if n_n not in visited:
#                 n_d = graph[t][n_n] + d
#                 dq.append([n_n, n_d])
#                 visited[n_n] = 1
#                 answer = max(n_d, answer)
# print(answer)

### Try 2. Diameter of Tree
tree_node = -1
max_dist = 0

dq = deque()
visited = {}
for k in graph:
    dq.append([k, 0])
    visited[k] = True
    break
while dq:
    t, d = dq.popleft()

    for n_n in graph[t]:
        if n_n not in visited:
            next_dist = d + graph[t][n_n]
            visited[n_n] = True
            dq.append([n_n, next_dist])
            if max_dist < next_dist:
                max_dist = next_dist
                tree_node = n_n

answer = 0
dq = deque()
dq.append([tree_node, 0])
visited = {tree_node:True}


while dq:
    t, d = dq.popleft()

    for n_n in graph[t]:
        if n_n not in visited:
            next_d = d + graph[t][n_n]
            visited[n_n] = True
            dq.append([n_n, next_d])
            answer = max(answer, next_d)

print(answer)

explain = """
첫번째 시도에서는 리프 노드가 degree 1인점을 이용하여 리프노드에서 BFS를 통해 가장 멀리 떨어진 두 노드 사이의 거리를 구하였다. 
그러나 해당 그래프가 임의의 두 노드 사이의 연결 관계가 존재하고 한 노드에서 다른 노드로 갈 때, 같은 노드를 두번 방문하지 않고 가는 경로는
유일하다는 특징을 이용하면 BFS 2번으로 풀 수 있고 두번째 시도에 반영하였다. 즉 해당 문제에서 주어진 그래프는 트리이고 트리에서는 
BFS 또는 DFS 두번을 통해 트리의 지름을 구할 수 있다. 입력에 대한 조건이 많이 주어지지 않아서 입력 처리가 쉽지 않았다. 
비어있는 그래프가 주어지는 경우를 대비하기 위하여 grpah가 빈 딕셔너리일때의 대한 처리와 입력의 끝이 주어지지 않으므로 try-except 문으로 처리해야 한다. 
"""