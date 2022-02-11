import sys

node_n, edge_n, start = map(int, sys.stdin.readline().strip().split(' '))
edge_list = []
for i in range(edge_n):
    edge_list.append(sys.stdin.readline())

graph = {}
for i in range(node_n):
    graph[i + 1] = []

for i in range(edge_n):
    temp = edge_list[i].split(' ')
    graph[int(temp[0])].append(int(temp[1]))
    graph[int(temp[1])].append(int(temp[0]))
for i in graph:
    graph[i] = sorted(graph[i])
visited = []
stack = [start]

def dfs(start_node):
    while stack:
        v = stack.pop(0)
        if v not in visited:
            visited.append(v)
            for i in graph[v]:
                if i not in visited:
                    stack.append(i)
                    dfs(v)
    return visited

for i in dfs(1):
    print(i, end = ' ')


visited = []
stack = [start]

def bfs(start_node):
    while stack:
        v = stack.pop(0)
        if v not in visited:
            visited.append(v)
            for i in graph[v]:
                if i not in visited:
                    stack.append(i)
    return visited
print()
for i in bfs(1):
    print(i, end= ' ')