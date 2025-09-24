import sys

for _ in range(4):
    temp_line = list(map(int, sys.stdin.readline().split()))
    x1,y1,p1,q1 = temp_line[:4]
    x2,y2,p2,q2 = temp_line[4:]

    if (p1<x2 or p2 < x1) and (q1<y2 or q2 < y1):
        print("d")