import sys


test = int(sys.stdin.readline())
cnt = 0

def dfs(stack):
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)

            if v[0]+1<n and graph[v[0]+1][v[1]] == 1 and [v[0]+1,v[1]] not in visited:
                stack.append([v[0]+1,v[1]])

            if v[0] >0 and graph[v[0]-1][v[1]] == 1 and [v[0]-1,v[1]] not in visited:
                stack.append([v[0]-1,v[1]])

            if v[1]>0 and graph[v[0]][v[1]-1] ==1 and [v[0],v[1]-1] not in visited:
                stack.append([v[0],v[1]-1])

            if v[1]+1<m and graph[v[0]][v[1]+1] == 1 and [v[0],v[1]+1] not in visited:
                stack.append([v[0],v[1]+1])

    return

for _ in range(test):
    m, n, k = map(int, sys.stdin.readline().strip().split(' '))
    graph = []
    for a in range(n):
        graph.append([0]*m)
    for i in range(k):
        temp = list(map(int, sys.stdin.readline().strip().split(' ')))
        graph[temp[1]][temp[0]] = 1
    cnt = 0

    visited = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and [i,j] not in visited:
                stack = [[i,j]]
                dfs(stack)
                cnt+=1
    print(cnt)

