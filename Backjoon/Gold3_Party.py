import sys

N, M, X = map(int, sys.stdin.readline().strip().split(' '))
inf = 100001
graph = {}
graph2 = {}

visited = {}
record = {}

visited2 = {}
record2 = {}

for i in range(N):
    graph[i+1] = {}
    graph2[i+1] = {}
    record[i+1] = inf
    record2[i+1] = inf
for i in range(M):
    s, e, t = map(int, sys.stdin.readline().strip().split(' '))
    graph[s][e] = t
    graph2[e][s] = t

visited[X] = 0
record[X] = 0

visited2[X] = 0
record2[X] = 0

for i in graph[X]:
    record[i] = graph[X][i]
for i in graph2[X]:
    record2[i] = graph2[X][i]

def find_minIdx(rc, vis):
    min_val = inf
    result = -1
    for idx, val in rc.items():
        if idx not in vis and val < min_val:
            result = idx
            min_val = val
    return result

while len(visited) != N:
    temp = find_minIdx(record, visited)
    visited[temp] = 0
    for i in graph[temp]:
        record[i] = min(record[i], record[temp]+ graph[temp][i])

while len(visited2) != N:
    temp = find_minIdx(record2, visited2)
    visited2[temp] = 0
    for i in graph2[temp]:
        record2[i] = min(record2[i], record2[temp] + graph2[temp][i])

fin = 0

for i in range(N):
    if record[i+1] + record2[i+1] > fin:
        fin = record[i+1] + record2[i+1]
print(fin)