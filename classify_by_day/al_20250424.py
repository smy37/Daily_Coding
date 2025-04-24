import sys

def dfs(s, visited, depth):
    if depth == 5:
        print(1)
        sys.exit()
    global graph
    t = s.pop()

    for n_n in graph[t]:
        if n_n not in visited:
            visited[n_n] = True
            dfs(s + [n_n], visited, depth+1)
            del visited[n_n]

N, M = map(int, sys.stdin.readline().split())

graph = {i : [] for i in range(N)}
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for n in graph:
    visited = {n: True}
    s = [n]
    dfs(s, visited, 1)

print(0)

## 백트래킹을 이용하는 것이 중요했던 문제, 그래프에서 경로와 상관없이 Node의 모든 방문이 문제라면 그냥 DFS나 BFS를 사용해도 되지만
## 특정 조건을 만족하는 경로를 구해야할 때는 백트래킹 기법이 들어가야 된다. 경로에 따라서 조건이 달라지는 경우라면 즉, A->B->C를 방문하는 것과
## A->C->B를 방문하는 것이 조건이 달리될 때 백트래킹이라는 기법을 사용하면 된다. 또한 여담으로 BFS를 구현시에 while 문과 재귀를 사용할 수 있고
## DFS 구현시에도 whild 문과 재귀를 사용할 수 있지만 DFS를 wihle로 재귀를 사용하지 않고 구현하는 것이 이 넷중에서 가장 까다롭다.