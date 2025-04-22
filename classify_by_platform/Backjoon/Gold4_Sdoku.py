import sys

n = 9

def return_aval_num(x, y, board):
    result = []
    sec_x = x//3
    sec_y = y//3
    temp_m = {i:0 for i in range(1, 10)}
    for i in range(3):
        cur_x = sec_x*3 + i
        for j in range(3):
            cur_y = sec_y*3 + j

            if board[cur_x][cur_y] in temp_m:
                temp_m.pop(board[cur_x][cur_y])
    for i in range(9):
        if board[x][i] in temp_m:
            temp_m.pop(board[x][i])
        if board[i][y] in temp_m:
            temp_m.pop(board[i][y])
    for i in temp_m:
        result.append(i)
    return result

def dfs(cur_idx, zero_dict_idx, board):
    if cur_idx == len(zero_dict_idx):
        for i in range(9):
            for j in board[i]:
                print(j, end= ' ')
            print()
        sys.exit()
    else:
        cur_x = zero_dict_idx[cur_idx][0]
        cur_y = zero_dict_idx[cur_idx][1]
        aval_list = return_aval_num(cur_x, cur_y, board)
        for i in aval_list:
            board[cur_x][cur_y] = i
            dfs(cur_idx+1, zero_dict_idx, board)
            board[cur_x][cur_y] = 0
        return
board = []
zero_d = {}

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if temp[j] == 0:
            zero_d[(i,j)] = 0
    board.append(temp)
zero_d_idx = list(zero_d.keys())
dfs(0, zero_d_idx, board)


### PYPI 로는 통과했지만 Python3로는 시간초과가 났음... 시간을 줄일 수 있는 방법은...?!