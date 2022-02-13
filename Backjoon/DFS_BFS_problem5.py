import sys
import collections
n,m = map(int, sys.stdin.readline().strip().split(' '))


graph = []

for i in range(n):
    graph = [sys.stdin.readline().strip()[-1::-1]]+graph


visited = []
for i in range(n):
    visited.append([0]*m)

stack = collections.deque()
stack.append([0,0])
visited[0][0] = 1
def bfs(stack):

    while stack:
        v = stack.popleft()
        if v == [n,m]:
            break
        if v[0]+1 < n and graph[v[0]+1][v[1]] == '1' and visited[v[0]+1][v[1]] == 0:
            stack.append([v[0]+1, v[1]])
            visited[v[0]+1][v[1]] = visited[v[0]][v[1]]+1
        if v[1]+1 <m and graph[v[0]][v[1]+1] == '1' and visited[v[0]][v[1]+1] == 0:
            stack.append([v[0], v[1]+1])
            visited[v[0]][v[1]+1] = visited[v[0]][v[1]] + 1
        if v[0] > 0 and graph[v[0]-1][v[1]] == '1' and visited[v[0]-1][v[1]] ==0:
            stack.append([v[0]-1, v[1]])
            visited[v[0]-1][v[1]] = visited[v[0]][v[1]] + 1
        if v[1] > 0 and graph[v[0]][v[1]-1] == '1' and visited[v[0]][v[1]-1] == 0:
            stack.append([v[0], v[1]-1])
            visited[v[0]][v[1]-1] = visited[v[0]][v[1]] + 1
    return
bfs(stack)

print(visited[n-1][m-1])