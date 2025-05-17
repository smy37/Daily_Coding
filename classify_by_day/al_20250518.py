import sys
from collections import deque

N, M, total_money = map(int, sys.stdin.readline().split())
cost = list(map(int, sys.stdin.readline().split()))


graph = {i+1:{} for i in range(N)}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = {}
dq = deque()

answer = 0
for k in graph:
    if k in visited:
        continue
    visited[k] = 1
    dq.append(k)
    temp_min = cost[k-1]
    while dq:
        t = dq.popleft()

        for n in graph[t]:
            if n not in visited:
                dq.append(n)
                visited[n] = 1
                temp_min = min(temp_min, cost[n-1])
    answer += temp_min

if answer > total_money:
    print("Oh no")
else:
    print(answer)


explain = """
문제 자체는 그래프 탐색의 전형적인 문제와 핵심 아이디어가 같다. 노드별로 그래프 탐색(일반적으로 더 빠르다는 BFS 사용)을 수행하여
서로 연결되어있는 그래프 집합들을 찾고 집합내 노드중 비용이 가장 적은 노드들 끼리 합쳐서 총 비용을 산출하면 되는 문제이다. 
하지만 주어지는 연결관계로 그래프를 생성하였는데 이때, 연결관계가 없는 노드들은 그래프에 생성되지 않고 비용 산정에도 포함되지 않아 
오답이 발생한다. 즉, 연결관계가 없는 노드들이 등장하는 케이스에 대한 고려가 필요하고 이에 대한 처리를 위해, 모든 노드가 포함된(연결관계가 없어도)
그래프를 생성후에 연결관계를 추가해준다.
"""
