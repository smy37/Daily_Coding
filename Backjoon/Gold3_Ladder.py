import sys
from itertools import permutations
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

add_l = []

for i in range(H):
    for j in range(N-1):
        if ladder[i][j] == 0 and ladder[i][j+1] == 0:
            add_l.append([i,j])

for i in range(3):
    p_l = permutations(add_l, i+1)
    t_ladder = copy.deepcopy(ladder)
    for k in p_l:
        for j in k:
            t_ladder[j[0]][j[1]] = 1
            t_ladder[j[0]][j[1]+1] = 2

        if simulation(t_ladder):
            print(i+1)
            sys.exit()
print(-1)


test = [[1,2,0,1,2], [0,0,1,2,0], [1,2,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]