import sys
import math
from collections import deque

N, R, D, X, Y = map(int, sys.stdin.readline().split())

graph = {}
visited = {}
answer = 0

tower = []
dq = deque()
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    dist = math.sqrt((X-x)**2 + (Y-y)**2)

    if dist <= R:
        dq.append([x, y, 0])
        visited[(x, y)] = 1
        answer += D
    tower.append([x,y])


for i in range(len(tower)):
    for j in range(i+1, len(tower)):
        x1, y1 = tower[i]
        x2, y2 = tower[j]
        dist = math.sqrt((x1-x2)**2+(y1-y2)**2)
        if dist <= R:
            if (x1, y1) not in graph:
                graph[(x1,y1)] = {}
            if (x2, y2) not in graph:
                graph[(x2, y2)] = {}
            graph[(x1,y1)][(x2, y2)] = 1
            graph[(x2,y2)][(x1, y1)] = 1

if len(graph) == 0:
    print(answer)
else:
    while dq:
        x, y, d = dq.popleft()

        if (x,y) in graph:
            for n_x, n_y in graph[(x,y)]:
                if (n_x, n_y) not in visited:
                    answer += (D/(2**(d+1)))
                    visited[(n_x, n_y)] = 1
                    dq.append([n_x, n_y, d+1])
    print(answer)


explain = """
타겟의 사정거리 안에 있는 타워에서는 에너지 총량만큼 데미지를 줄 수 있고 타겟의 사정거리 밖에 있는 타워들에 대해서는
타워들을 각각 사정거리 안에 있는 타워 끼리는 간선으로 연결하여 그래프를 구성하였을 때, BFS를 통해 타겟의 사정거리 안에 있는
타워에서부터 사정거리 밖에 있는 타워들 까지 도달하는 거리를 측정하여 해당 거리를 기반으로 전체 타겟에 도달하는 거리를 구할 수 있다.
단 주의해야 할 것은 graph에 간선을 추가할 때, 조건에 의해 추가하기 때문에 BFS 도중 도출되는 node가 graph에 존재 안할 수도 있다는 것을 
유의해야 한다. 
"""