import sys

N, K = map(int, sys.stdin.readline().split())

code_l = []
for _ in range(N):
    code = sys.stdin.readline().strip()
    code_l.append(code)

graph = {i+1: [] for i in range(N)}

for i in range(N):
    code_1 = code_l[i]
    for j in range(i+1, N):
        code_2 = code_l[j]
        cnt = 0
        for k in range(K):
            if code_1[k] != code_2[k]:
                cnt +=1
            if cnt >=2 :
                break
        if cnt == 1:
            graph[i+1].append(j+1)
            graph[j+1].append(i+1)

source, target = map(int, sys.stdin.readline().split())
s = [source]
visited = {source: True}

def dfs(s, visited):
    global target
    t = s.pop()
    if t == target:
        for k in visited:
            print(k, end=" ")
        sys.exit()
    for n_n in graph[t]:
        if n_n not in visited:
            visited[n_n] = True
            dfs(s+[n_n], visited)
            del visited[n_n]

dfs(s, visited)
print(-1)


## 일단 주어진 이진수들 간의 비교를 통해서 해밍 거리를 찾고 해밍 거리가 1인 노드 들끼리 이어 그래프를 구성해야 한다.
## 이때, 그래프 구성에는 O(n^3)의 시간 복잡도가 소요되고 그래프 구성 이후에는 시작지점과 타겟 지점을 DFS를 통해 찾아준다.
## BFS 대신에 DFS 사용한 이유는 백트래킹을 이용해 Path를 찾아주기 위함이다. Path를 찾을 때는 백트래킹을 이용하지 않으면
## 실제 경로와 상관없는 Node이 포함되기 때문에 백트래킹을 사용해야 한다.