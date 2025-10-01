import sys

T = int(sys.stdin.readline())
for _ in range(T):
    cord_l = []
    for _ in range(4):
        x, y = map(int, sys.stdin.readline().split())
        cord_l.append([x,y])
    d1 = (cord_l[0][0]-cord_l[1][0])**2 + (cord_l[0][1]-cord_l[1][1])**2
    d2 = (cord_l[0][0]-cord_l[2][0])**2 + (cord_l[0][1]-cord_l[2][1])**2
    d3 = (cord_l[0][0]-cord_l[3][0])**2 + (cord_l[0][1]-cord_l[3][1])**2

    dist_l = sorted([d1, d2, d3])

    if dist_l[0] == dist_l[1] and 2*dist_l[0] == dist_l[2]:
        print(1)
    else:
        print(0)