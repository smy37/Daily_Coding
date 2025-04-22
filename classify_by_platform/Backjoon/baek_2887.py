import sys
import heapq
import math
import copy

N = int(sys.stdin.readline())
case_x = []
case_y = []
case_z = []

for i in range(N):
    x,y,z = map(int, sys.stdin.readline().split())
    case_x.append([x, i])
    case_y.append([y, i])
    case_z.append([z, i])
    if N == 1:
        print(min(x,y,z))
        sys.exit()

case_x = sorted(case_x, key = lambda x : x[0])
case_y = sorted(case_y, key = lambda x : x[0])
case_z = sorted(case_z, key = lambda x : x[0])
test = [case_x, case_y, case_z]
edges = {i: [] for i in range(N)}
for t in test:
    for i in range(N-1):
        heapq.heappush(edges[t[i][1]], [abs(t[i][0] - t[i + 1][0]), t[i+1][1]])
        heapq.heappush(edges[t[i+1][1]], [abs(t[i][0] - t[i + 1][0]), t[i][1]])
        

answer = 0
hq = edges[0]
visited = {0:True}
heapq.heapify(hq)
while hq:
    dist, node = heapq.heappop(hq)
    if node not in visited:
        visited[node] = True
        answer += dist
        for nn in edges[node]:
            if nn[1] not in visited:
                heapq.heappush(hq, nn)

print(answer)
