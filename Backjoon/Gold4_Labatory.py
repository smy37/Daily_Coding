import sys
from itertools import combinations as cmb
import copy
from collections import deque
n,m = map(int, sys.stdin.readline().strip().split(' '))

def check_v(b):
    r = 0
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] == 0:
                r +=1

    return r

board = []
blank = []
virus = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split(' ')))
    for j in range(m):
        if temp[j] == 0:
            blank.append([i,j])
        elif temp[j] == 2:
            virus.append([i,j])
    board.append(temp)
cb = list(cmb(blank, 3))

result = 0
for i in cb:
    t_r = 0
    temp_b = copy.deepcopy(board)
    for j in i:
        temp_b[j[0]][j[1]] =1
    dq = deque()
    visited = []
    for v in virus:
        dq.append(v)
        while dq:
            t = dq.popleft()
            if t not in visited:
                visited.append(t)
                for j in range(4):
                    if j == 0:  ## 상
                        if t[0]-1 >= 0 and temp_b[t[0]-1][t[1]]==0:
                            dq.append([t[0]-1, t[1]])
                            temp_b[t[0]-1][t[1]] = 2
                    elif j == 1:    ## 하
                        if t[0]+1 < n and temp_b[t[0]+1][t[1]]==0:
                            dq.append([t[0] + 1, t[1]])
                            temp_b[t[0] + 1][t[1]] = 2
                    elif j == 2:    ## 좌
                        if t[1] -1 >= 0 and temp_b[t[0]][t[1]-1]==0:
                            dq.append([t[0], t[1] - 1])
                            temp_b[t[0]][t[1]-1] = 2
                    elif j == 3:    ## 우
                        if t[1] +1 < m and temp_b[t[0]][t[1]+1]==0:
                            dq.append([t[0], t[1] + 1])
                            temp_b[t[0]][t[1] + 1] = 2

    tt = check_v(temp_b)

    if tt > result:
        result = tt

print(result)
