import sys
from itertools import combinations
import copy

N, M, H = map(int, sys.stdin.readline().split())

ladder = [[0 for _ in range(N)] for _ in range(H)]

def simulation(l):
    for s in range(len(l[0])):
        cur_x = 0
        cur_y = s
        while cur_x < len(l):
            if l[cur_x][cur_y] == 1:
                cur_y += 1
                cur_x += 1
            elif l[cur_x][cur_y] == 2:
                cur_y -= 1
                cur_x += 1
            else:
                cur_x += 1
        if cur_y != s:
            return False
    return True

for i in range(M):
    a, b= map(int, sys.stdin.readline().split())
    ladder[a-1][b-1] = 1
    ladder[a-1][b] = 2

if simulation(ladder):
    print(0)
    sys.exit()


def dfs(cnt, idx):
    global min_cnt
    if simulation(ladder):
        min_cnt = min(min_cnt, cnt)
    elif cnt == 3 or min_cnt <= cnt:
        return
    for i in range(idx, limit):
        if ladder[add_l[i][0]][add_l[i][1]] == 0 and ladder[add_l[i][0]][add_l[i][1]+1] == 0:
            ladder[add_l[i][0]][add_l[i][1]] = 1
            ladder[add_l[i][0]][add_l[i][1]+1] = 2
            dfs(cnt+1, i+1)
            ladder[add_l[i][0]][add_l[i][1]] = 0
            ladder[add_l[i][0]][add_l[i][1] + 1] = 0
add_l = []

for i in range(H):
    for j in range(N-1):
        if ladder[i][j] == 0 and ladder[i][j+1] == 0:
            add_l.append([i,j])

limit = len(add_l)
min_cnt = 10


dfs(0,0)
if min_cnt <=3:
    print(min_cnt)
else:
    print(-1)
