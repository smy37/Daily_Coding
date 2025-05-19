import sys
import math

M, N = map(int, sys.stdin.readline().split())

mv = [[-1, 0], [1, 0], [0, -1], [0, 1]]

board = []
for _ in range(N):
    temp = sys.stdin.readline().strip()
    board.append([int(i) for i in temp] )

if N==1 and M == 1 and board[0][0] == 1:
    print(1)
    sys.exit()

# ## Try 1. DFS 가지치기 사용.
# sys.setrecursionlimit(10**6)
# answer = math.inf
# 
# def dfs(s, visited, cur_cnt):
#     global N, M, answer
# 
#     if len(s) == 0:
#         return
#     x, y = s.pop()
# 
#     if x == N-1 and y == M-1:
#         answer = min(answer, cur_cnt)
# 
#     for i in range(len(mv)):
#         n_x, n_y = x+mv[i][0], y+mv[i][1]
# 
#         if 0<=n_x<N and 0<=n_y<M :
#             if board[n_x][n_y] == 1 and cur_cnt +1 < answer and cur_cnt + 1 < visited[(n_x,n_y)]:
#                 visited[(n_x, n_y)] = cur_cnt + 1
#                 dfs(s+[[n_x, n_y]], visited, cur_cnt+1)
# 
# 
#             elif board[n_x][n_y] == 0 and cur_cnt < answer and cur_cnt< visited[(n_x,n_y)]:
#                 visited[(n_x, n_y)] = cur_cnt
#                 dfs(s + [[n_x, n_y]], visited, cur_cnt)
# 
# s = [[0,0]]
# visited = {(i, j): math.inf for i in range(N) for j in range(M)}
# visited[(0,0)] = 0
# dfs(s, visited, 0)
# 
# print(answer)

## Try 2. 0-1 BFS
from collections import deque
dq = deque()

dq.append([0,0])
visited = {(i, j):math.inf for i in range(N) for j in range(M)}
visited[(0,0)] = 0

while dq:
    x, y = dq.popleft()

    for i in range(len(mv)):
        n_x, n_y = x+mv[i][0], y+mv[i][1]
        if 0<=n_x<N and 0<=n_y<M:
            cost = board[n_x][n_y] + visited[(x,y)]

            if cost < visited[(n_x,n_y)]:
                visited[(n_x, n_y)] = cost

                if board[n_x][n_y] == 1:
                    dq.append([n_x, n_y])
                else:
                    dq.appendleft([n_x, n_y])

print(visited[(N-1,M-1)])

explain= """
첫번째 시도는 전역 변수인 answer와 visited에 벽을 부순 횟수를 기록해 두어 가지치기를 수행해서 답을 구할려고 하였으나 시간초과가 발생하였다.
벽을 부수지 않고 이동이 가능할때는 스택의 왼쪽에 넣어주고 벽을 부숴야 이동이 가능할때는 스택의 오른쪽에 넣어주어 BFS를 수행하여 답을 구하였음.
지금까지 어떤 경로로 왔던간에 현재 노드에서 모든 경우의 수로 이동을 하므로 < visited[(n_x, n_y)] 일때만 dq에 추가해 주는 것이 핵심이었다.
현재까지 이동해온 경로가 중요한 경우와 경로에서 상관없이 이전에서 누적해온 값만 사용하면 되는 경우가 있는데 이번 경웨는 후자이다.
"""
