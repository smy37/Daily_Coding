import sys 
from collections import deque


### 1. First Try
# coord = [[0,0]]
# n, T = map(int, sys.stdin.readline().split())
# for _ in range(n):
#     coord.append(list(map(int, sys.stdin.readline().split())))



# graph = {}
# for i in range(n+1):
#     for j in range(i+1, n+1):
#         x1, y1 = coord[i]
#         x2, y2 = coord[j]
#         if (x1, y1) not in graph:
#             graph[(x1,y1)] = {}
#         if (x2, y2) not in graph:
#             graph[(x2,y2)] = {}
#         if abs(x2-x1)<=2 and abs(y2-y1) <=2:
#             graph[(x1, y1)][(x2, y2)] = 1
#             graph[(x2, y2)][(x1, y1)] = 1

# dq = deque()
# dq.append([0,0,0])
# visited = {(0,0): 1}

# while dq:
#     x, y, cnt = dq.popleft()
#     if y == T:
#         print(cnt)
#         sys.exit()
#     for t in graph[(x, y)]:
#         if (t[0], t[1]) not in visited:
#             dq.append([t[0], t[1], cnt+1])
#             visited[(t[0], t[1])] = 1

# print(-1)


### 2. Second Try
n, T = map(int, sys.stdin.readline().split())

coord = {(0,0):1}

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    coord[(x,y)] = 1


dq = deque()
dq.append([0,0,0])
visited = {(0,0): 1}

while dq:
    x, y, cnt = dq.popleft()
    if y == T:
        print(cnt)
        sys.exit()

    for dx in [-2, -1, 0, 1, 2]:        ## 핵심 부분!
        for dy in [-2, -1, 0, 1, 2]:
            n_x, n_y = x+dx, y+dy
            if (n_x, n_y) in coord and (n_x, n_y) not in visited:
                visited[(n_x, n_y)] = 1
                dq.append([n_x, n_y, cnt+1])

print(-1)

explain = """
처음 방법에는 O(n^2)의 시간복잡도로 한 노드에서 이동 가능한 노드를 간선으로 이어두었다. 그러나 시간 초과가 발생하였고
노드의 좌표가 정수이고 노드 간의 x좌표가 2 이하, y 좌표가 2 이하 임을 이용해서 O(25) 만큼의 비교를 통해서 이동 가능한 node를 
stack에 추가하여 BFS를 수행하였다.
"""