import sys

N = int(sys.stdin.readline())
g = {i+1:[] for i in range(N)}
p_list = [0 for _ in range(N)]

for i in range(N-1):
    s,e = map(int, sys.stdin.readline().split())
    g[s].append(e)
    g[e].append(s)

def dfs(stk:list, visit_d: dict, graph:dict):
    while stk:
        t = stk.pop()
        for i in graph[t]:
            if i not in visit_d:    ## 경로가 유일한 트리의 특성상 이 부분만 적용되면 된다.
                visit_d[i] = 1
                p_list[i-1] = t
                stk.append(i)

s_node = 1
s = []
visited = {}
s.append(1)
visited[1] = 1

dfs(s, visited, g)

for i in range(1, len(p_list)):
    print(p_list[i])