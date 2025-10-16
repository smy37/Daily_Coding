import sys 

N = int(sys.stdin.readline())
x_dist, y_dist = map(int, sys.stdin.readline())
cord_l = {}

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x not in cord_l:
        cord_l[x] = {}
    cord_l[x][y] = 1

x_list = list(cord_l.keys())


