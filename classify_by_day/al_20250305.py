import sys
import heapq
N = int(sys.stdin.readline())

node_l = []

for _ in range(N):
    x, y = map(float, sys.stdin.readline().split())
    node_l.append([x,y])

edge_l = {i : [] for i in range(N)}

for i in range(N):
    x1, y1 = node_l[i]
    for j in range(N):
        if j == i:
            continue
        x2, y2 = node_l[j]
        dist = (x1-x2)**2 + (y1-y2)**2
        edge_l[i].append([dist, j])
        edge_l[j].append([dist, i])
hq = edge_l[0]
heapq.heapify(hq)
visited = {0:True}
answer = 0

while len(visited) < N:
    dist, cur = heapq.heappop(hq)
    if cur not in visited:
        visited[cur] = True
        answer += dist**(1/2)
        for edge in edge_l[cur]:
            heapq.heappush(hq, edge)
print(answer)




