import sys
from collections import deque
import copy

N = int(sys.stdin.readline())

board = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    board.append(temp)


s_x = [-1, 1, 0, 0]
s_y = [0, 0, -1, 1]

cur_n = 2
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            stack = deque()
            stack.append([i,j])
            board[i][j] = cur_n
            while stack:
                temp = stack.popleft()
                for k in range(4):
                    n_x = temp[0]+s_x[k]
                    n_y = temp[1]+s_y[k]
                    if 0<=n_x < N and 0<= n_y < N and board[n_x][n_y] ==1:
                        board[n_x][n_y] = cur_n
                        stack.append([n_x,n_y])
            cur_n+=1
# for i in range(N):
#     print(board[i])
# print()

##### !!!!! 아랫 부분에 대한 구현을 설마 NxN 위 격자들에서 BFS를 전부 돌려도 구해 질 수 있다는 것에 대한 시간적 감각이 없었다..... !!!!! #####
##### 일단은 가장 무식한 방법이더라도 시간만 충분하다면 풀 수 있는 해를 생각해보자....

result = 1000000
temp_n = 1
for i in range(N):
    for j in range(N):
        if 2<=board[i][j] <cur_n:
            stack = deque()
            temp_n = board[i][j]
            new_board = copy.deepcopy(board)
            stack.append([i,j,0])
            flag = True
            while stack:
                temp = stack.popleft()
                for k in range(4):
                    n_x = temp[0] + s_x[k]
                    n_y = temp[1] + s_y[k]
                    if 0<= n_x < N and 0<= n_y < N and new_board[n_x][n_y] != temp_n:
                        if new_board[n_x][n_y] == 0:
                            stack.append([n_x,n_y, temp[2]+1])
                            new_board[n_x][n_y] = temp_n
                            # for i in range(N):
                            #     print(new_board[i])
                            # print(temp[2])
                            # print()
                        else:
                            result = min(result, temp[2])

                            flag = False
                            break

print(result)
