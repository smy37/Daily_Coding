import sys

def cross(v1, v2):
    return v1[0]*v2[1]-v1[1]*v2[0]

def subtract(v1, v2):
    return [v1[0]-v2[0], v1[1]-v2[1]]

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

A = [x1, y1]
a = subtract([x2,y2], A)
B = [x3, y3]
b = subtract([x4, y4], B)

aCb = cross(a, b)
AmB = subtract(A, B)
if aCb == 0:
    if cross(AmB, a) == 0:
        if max(x1, x2) >= min(x3, x4) and min(x1, x2) <= max(x3, x4) and max(y1, y2) >= min(y3, y4) and min(y1, y2) <= max(y3, y4):
            print(1)
            sys.exit()
    print(0)
    sys.exit()

t = -cross(AmB, b)/aCb
u = -cross(AmB, a)/aCb

if 0<= t <= 1 and 0<=u <=1:
    print(1)
else:
    print(0)