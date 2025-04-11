import sys

def subtract(n1, n2):
    return [n1[0]-n2[0], n1[1]-n2[1]]

def cross(v1, v2):
    return v1[0]*v2[1]-v1[1]*v2[0]

x_a, y_a = map(int, sys.stdin.readline().split())
x_b, y_b = map(int, sys.stdin.readline().split())
x_c, y_c = map(int, sys.stdin.readline().split())

AB = subtract([x_b, y_b], [x_a, y_a])
BC = subtract([x_c, y_c], [x_b, y_b])

denom = cross(AB, BC)

if denom > 0:
    print(1)
elif denom <0:
    print(-1)
else:
    print(0)