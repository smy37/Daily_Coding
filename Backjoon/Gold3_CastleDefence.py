import sys
from itertools import permutations
from collections import  deque
import copy
N, M, D = map(int, sys.stdin.readline().split())

board = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    board.append(temp)
board = board + [[0 for _ in range(M)]]
dx = [0, -1, 0]
dy = [-1, 0, 1]
def update_board(b : list):
    return b[:len(b)-2]+[[0 for _ in range(len(b[0]))]]
def dfs(s, visited,b, cur_d, D):
    while s:
        t = s.popleft()
        if b[t[0]][t[1]] ==1 :
            b[t[0]][t[1]] = 0
            return True
        else:
            for i in range(3):
                nx = t[0] + dx[i]
                ny = t[1] + dy[i]
                if 0<=nx<len(b) and 0<=ny<len(b[0]) and (nx,ny) not in visited and cur_d+1 <= D:
                    s.append([nx,ny])
                    visited[(nx,ny)] = 1
            cur_d+=1
    return False

permute = permutations(range(M), 3)
cnt = 0
g_cnt = 0
for i in permute:
    t_board = copy.deepcopy(board)
    cnt = 0
    for j in range(N):
        for k in i:
            dq = deque()
            dq.append([len(t_board)-1,k])
            visited = {}
            visited[(len(t_board)-1, k)] = 1

            if dfs(dq, visited, t_board, 0, D):
                cnt +=1
            # print(k, cnt)
            # for x in board:
            #     print(x)
            # print()
        t_board = update_board(t_board)
    g_cnt = max(g_cnt, cnt)

print(g_cnt)