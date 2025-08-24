import sys
from collections import deque

T = int(sys.stdin.readline())
move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]


### 1. First Approach
# for _ in range(T):
#     dq = deque()
#     w, h = map(int, sys.stdin.readline().split())
#     board = []
#     fire = {}
#     cur_x, cur_y = -1, -1
#     for i in range(h):
#         temp = sys.stdin.readline().strip()
#         for j in range(len(temp)):
#             if temp[j] == "@":
#                 cur_x, cur_y = i, j 
#             elif temp[j] == "*":
#                 fire[(i, j)] = 1
        
#         board.append([x for x in temp])
#     visited = {(cur_x, cur_y): 1}
#     dq.append([cur_x, cur_y])
#     flag = True
#     time = 1
    
#     while flag:
#         new_fire = {}
#         for f_x, f_y in fire:
#             for i in range(4):
#                 n_f_x, n_f_y = f_x + move_x[i], f_y+ move_y[i]
#                 if 0<=n_f_x < h and 0<=n_f_y < w and (n_f_x, n_f_y) not in fire and board[n_f_x][n_f_y] != "#":
#                     new_fire[(n_f_x, n_f_y)] = 1
#                     board[n_f_x][n_f_y] = "*"
        
#         for nf in new_fire:
#             fire[nf] = 1
                    
#         next_dq = deque()
#         while dq:
#             c_x, c_y = dq.popleft()

#             for i in range(4):
#                 n_x, n_y = c_x + move_x[i], c_y + move_y[i]
#                 if 0<=n_x < h and 0<=n_y < w and (n_x, n_y) not in visited and board[n_x][n_y] == ".":
#                     next_dq.append([n_x, n_y])
#                     visited[(n_x, n_y)] = 1

#                 elif 0 > n_x or n_x >= h or 0 > n_y or n_y >= w:
#                     print(time)
#                     flag = False
#                     dq = None
#                     break
#         if len(next_dq) == 0 and flag:
#             print("IMPOSSIBLE")
#             break
#         dq = next_dq
#         time += 1

### 2. Second Approach
for _ in range(T):
    w, h = map(int, sys.stdin.readline().split())
    man_x, man_y = -1, -1
    fire = deque()
    visited = {}
    board = []
    for i in range(h):
        row = sys.stdin.readline().strip()

        for j in range(len(row)):
            if row[j] == "@":
                man_x, man_y = i, j
            elif row[j] == "*":
                fire.append([i, j, 0])
                visited[(i, j)] = 1

        board.append([t for t in row])

    while fire:
        cur_fire = fire.popleft()
        for i in range(4):
            next_fire_x, next_fire_y = cur_fire[0] + move_x[i], cur_fire[1] + move_y[i]
            if 0<= next_fire_x < h and 0<= next_fire_y < w and board[next_fire_x][next_fire_y] != "#"and (next_fire_x, next_fire_y) not in visited:
                visited[(next_fire_x, next_fire_y)] = 1
                fire.append([next_fire_x, next_fire_y, cur_fire[2]+1])
                board[next_fire_x][next_fire_y] = cur_fire[2] + 1
    
    dq = deque()
    dq.append([man_x, man_y, 0])
    visited = {(man_x, man_y): 1}

    flag = False
    while dq:
        cur_x, cur_y, cur_time = dq.popleft()

        for i in range(4):
            next_x, next_y = cur_x + move_x[i], cur_y + move_y[i]
            if 0<= next_x < h and 0<= next_y < w and (next_x, next_y) not in visited and board[next_x][next_y] not in ["#", "*"] and \
            (board[next_x][next_y] == "." or board[next_x][next_y] > cur_time + 1):
                dq.append([next_x, next_y, cur_time + 1])
                visited[(next_x, next_y)] = 1
            elif 0 > next_x or next_x >= h or 0 > next_y or next_y >= w:
                flag = True
                print(cur_time+1)
                break
        if flag:
            break
    if not flag:
        print("IMPOSSIBLE")


explain = """
처음에는 시뮬레이션 방법으로 매 시간마다 불이 확장되는 것과 사람이 이동하는 것을 구현하여 최단 탈출 시간을 구하려고 하였다.
그러나 시간초과가 발생하였고 불이 번지는 시간을 BFS로 먼저 보드에 기록해두고 그 후에 BFS를 한번더 해서 사람이 불이 번지는 
시간보다 이전 시간이라면 이동 가능하다고 하여 탈출 가능한지 판단하였다.
"""