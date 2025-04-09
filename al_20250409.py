import sys
import math
def cal_dist(n1, n2):
    return (n1[0]-n2[0])**2+(n1[1]-n2[1])**2+(n1[2]-n2[2])**2

def in_product(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]+v1[2]*v2[2]


def cal_dot_line(n2l, v1):
    up = (n2l[0]*v1[1]-n2l[1]*v1[0])**2 + (n2l[0]*v1[2]-n2l[2]*v1[0])**2 + (n2l[1]*v1[2]-n2l[2]*v1[1])**2
    down = v1[0]**2 + v1[1]**2 + v1[2]**2

    return math.sqrt(up)/math.sqrt(down)

l_x1, l_y1, l_z1, l_x2, l_y2, l_z2, n_x, n_y, n_z = map(int, sys.stdin.readline().split())

d1 = cal_dist([l_x1, l_y1, l_z1], [n_x, n_y, n_z])
d2 = cal_dist([l_x2, l_y2, l_z2], [n_x, n_y, n_z])

if d1 < d2:
    v1 = [l_x2-l_x1, l_y2-l_y1, l_z2-l_z1]
    v2 = [n_x-l_x1, n_y-l_y1, n_z-l_z1]

else:
    v1 = [l_x1 - l_x2, l_y1 - l_y2, l_z1 - l_z2]
    v2 = [n_x - l_x2, n_y - l_y2, n_z - l_z2]

ip = in_product(v1, v2)

if ip >= 0 :
    dist = cal_dot_line(v2, v1)
    print(dist)
else:
    print(math.sqrt(min(d1, d2)))