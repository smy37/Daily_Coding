from collections import deque

g_map = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
for i in g_map:
    print(i)
final = []
def dfs(start, visited, n, m, graph):
    global final
    visited  = visited + [start]
    if len(final) >=1 and len(visited) >= final[0]:
        return
    elif start == n*m:
        final = [len(visited)]

    for node in graph[start]:
        if node not in visited:
            dfs(node, visited, n, m, graph)


def solution(maps):
    answer = -1
    n,m = len(maps), len(maps[0])
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    visited = []
    dq = []
    start = (0,0)
    dq.append(start)
    dq = deque(dq)

    while dq:

        x, y = dq.popleft()
        for i in range(4):
            t_x = x+dx[i]
            t_y = y+dy[i]
            if t_x <0 or t_x >= m or t_y <0 or t_y>=n:
                continue
            if maps[t_y][t_x] ==0:
                continue
            if maps[t_y][t_x] == 1:
                maps[t_y][t_x] = maps[y][x] +1
                dq.append((t_x,t_y))
    print(maps[n-1][m-1])
    return maps[n-1][m-1]

solution(g_map)

