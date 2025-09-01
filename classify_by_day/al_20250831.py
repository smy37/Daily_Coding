import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())


stop_dict = {}
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    stop_dict[(x, y)] = 1

visited = {(0, 0): 1}
dq = deque()
dq.append([0, 0])
move_x = [1, 1]
move_y = [1, -1]

while dq:
    x, y = dq.popleft()
    for i in range(2):
        nx, ny = x+move_x[i], y+move_y[i]

        if (nx, ny) not in stop_dict and (nx, ny) not in visited:
            if nx <= N:
                if 0<= ny <= nx:
                    dq.append([nx, ny])
                    visited[(nx, ny)] = 1
            else:
                if 0<= ny <= (2*N-nx):
                    dq.append([nx, ny])
                    visited[(nx, ny)] = 1


visited_r = {(2*N, 0): 1}
dq = deque()
dq.append([2*N, 0])
move_x = [-1, -1]
move_y = [1, -1]
answer = 0

while dq:
    x, y = dq.popleft()
    for i in range(2):
        nx, ny = x+move_x[i], y+move_y[i]

        if (nx, ny) not in stop_dict and (nx, ny) not in visited_r:
            if nx <= N:
                if 0<= ny <= nx:
                    dq.append([nx, ny])
                    visited_r[(nx, ny)] = 1
            else:
                if 0<= ny <= (2*N-nx):
                    dq.append([nx, ny])
                    visited_r[(nx, ny)] = 1

max_y = sorted(visited.keys(), key=lambda x: x[1], reverse=True)
for t in max_y:
    if t in visited_r:
        print(t[1])
        break
else:
    print(-1)

explain = """
처음 시도에서는 BFS를 한번 했지만 특정 노드에서 경로중에 더이상 진행이 불가하여
폐기되는 노드에 대한 처리가 불가하였음. 역방향으로 BFS를 한번 더 사용하여 (0,0)에서
방문할 수 있는 노드와 (2*N, 0)에서 방문할 수 있는 노드의 교집합을 통해 방문 가능한
노드를 특정하였음.
"""