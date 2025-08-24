import sys
from collections import deque

T = int(sys.stdin.readline())
move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]

for _ in range(T):
    dq = deque()
    w, h = map(int, sys.stdin.readline().split())
    board = []
    fire = {}
    cur_x, cur_y = -1, -1
    for i in range(h):
        temp = sys.stdin.readline().strip()
        for j in range(len(temp)):
            if temp[j] == "@":
                cur_x, cur_y = i, j 
            elif temp[j] == "*":
                fire[(i, j)] = 1
        
        board.append([x for x in temp])
    visited = {(cur_x, cur_y): 1}
    dq.append([cur_x, cur_y])
    flag = True
    time = 1
    
    while flag:
        new_fire = {}
        for f_x, f_y in fire:
            for i in range(4):
                n_f_x, n_f_y = f_x + move_x[i], f_y+ move_y[i]
                if 0<=n_f_x < h and 0<=n_f_y < w and (n_f_x, n_f_y) not in fire and board[n_f_x][n_f_y] != "#":
                    new_fire[(n_f_x, n_f_y)] = 1
                    board[n_f_x][n_f_y] = "*"
        
        for nf in new_fire:
            fire[nf] = 1
                    
        next_dq = deque()
        while dq:
            c_x, c_y = dq.popleft()

            for i in range(4):
                n_x, n_y = c_x + move_x[i], c_y + move_y[i]
                if 0<=n_x < h and 0<=n_y < w and (n_x, n_y) not in visited and board[n_x][n_y] == ".":
                    next_dq.append([n_x, n_y])
                    visited[(n_x, n_y)] = 1

                elif 0 > n_x or n_x >= h or 0 > n_y or n_y >= w:
                    print(time)
                    flag = False
                    dq = None
                    break
        if len(next_dq) == 0 and flag:
            print("IMPOSSIBLE")
            break
        dq = next_dq
        time += 1
