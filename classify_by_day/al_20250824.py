import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
ori_board = []

for _ in range(N):
    ori_board.append(list(map(int, sys.stdin.readline().split())))

after_board = []
for _ in range(N):
    after_board.append(list(map(int, sys.stdin.readline().split())))

move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

dq = deque()
visited = {}
start_idx = {}
start_num = {}
for i in range(N):
    for j in range(M):
        if (i, j) not in visited:
            visited[(i, j)] = 1
            dq.append([i, j, ori_board[i][j]])
            start_idx[(i, j)] = [(i, j)]
            start_num[(i, j)] = ori_board[i][j]
            while dq:
                x, y, num = dq.popleft()

                for k in range(4):
                    n_x, n_y = x+move_x[k], y+move_y[k]
                    if 0<=n_x<N and 0<=n_y<M and (n_x, n_y) not in visited and ori_board[n_x][n_y] == num:
                        visited[(n_x, n_y)] = 1
                        dq.append([n_x, n_y, num])
                        start_idx[(i,j)].append((n_x, n_y))

### 1. First Approach

# dq = deque()
# visited = {}
# after_idx = {}
# after_num = {}
# flag = True
# cnt = 0
# for i, j in start_idx:
#     if (i, j) not in visited:
#         visited[(i, j)] = 1
#         dq.append([i, j, after_board[i][j]])
#         after_idx[(i, j)] = [(i, j)]
#         after_num[(i, j)] = after_board[i][j]
#         while dq:
#             x, y, num = dq.popleft()

#             for k in range(4):
#                 n_x, n_y = x+move_x[k], y+move_y[k]
#                 if 0<=n_x<N and 0<=n_y<M and (n_x, n_y) not in visited and after_board[n_x][n_y] == num:
#                     visited[(n_x, n_y)] = 1
#                     dq.append([n_x, n_y, num])
#                     after_idx[(i,j)].append((n_x, n_y))
#         if start_idx[(i, j)] != after_idx[(i,j)]:
#             flag = False
#             break
#         else:
#             if start_num[(i, j)] != after_num[(i, j)]:
#                 cnt +=1
# if flag and cnt <=1:
#     print("YES")
# else:
#     print("NO")


### 2. Second Approach
dq = deque()
visited = {}
after_idx = {}
after_num = {}
flag = True
cnt = 0
for k, v in start_idx.items():
    cri = after_board[k[0]][k[1]]
    if cri != ori_board[k[0]][k[1]]:
        cnt += 1
    for i, j in v:
        if after_board[i][j] != cri:
            flag = False
            break
    if not flag:
        break

if not flag:
    print("NO")
else:
    if cnt <= 1:
        print("YES")
    else:
        print("NO")

explain = """
처음 시도에서는 bfs 두번을 통해서 찾을려고 했지만 숫자가 업데이트 되면서 연결되는 모양이 바뀌는 경우를 커버하지 못했다.
따라서 처음 bfs에서 연결되는 그룹을 기록해두고 업데이트 된 보드에서 해당 그룹에 속하는 원소들이 같은 숫자를 가지고 있는지 판단하였다.
또한 그룹마다 숫자가 있고 이 숫자가 업데이트 후에 바뀌는는 횟수가 최대 1회가 되어야만 "YES"를 출력하도록 하였다.
"""