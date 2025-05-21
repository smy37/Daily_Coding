import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
mv = [[-1, 0], [1, 0], [0, -1], [0, 1]]


board = []
for _ in range(N):
    temp = sys.stdin.readline().strip()
    board.append(temp)

visited = {}
for i in range(N):
    for j in range(M):
        if (i, j) not in visited:
            cur_str = board[i][j]
            visited[(i, j)] = 1
            dq = deque()
            dq.append([i,j])
            end_i, end_j = i, j
            temp_cnt = 1

            while dq:
                x, y = dq.pop()
                for k in range(len(mv)):
                    nx, ny = x+mv[k][0], y+mv[k][1]
                    if 0<=nx <N and 0<=ny < M and board[nx][ny] == cur_str and (nx, ny) not in visited:
                        dq.append([nx,ny])
                        visited[(nx, ny)] = 1
                        end_i = max(end_i, nx)
                        end_j = max(end_j, ny)
                        temp_cnt +=1

            if temp_cnt != (end_i-i+1)*(end_j-j+1):
                print("BaboBabo")
                sys.exit()
print("dd")

explain = """
BFS 또는 DFS로 같은 알파벳을 가지는 부분 그래프를 찾는 것이 시작이다. 그리고 찾아진 부분 그래프가 직사각형의 형태를 가지는지 알기 위해서 
사용한 방법은 직사각형 형태의 그래프라면 x_min, y_min 값과 x_max, y_max 값을 각각 뺀 것을 곱한 개수가 실제 부분 집합을 이루는 노드의 개수와 같은지 체크하는 것이다.
즉 (x_max-x_min+1)*(y_max-y_min+1)이 부분집합의 노드의 개수와 같다는 것을 이용하하는 것이다.
"""