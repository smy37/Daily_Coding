import sys
from functools import cmp_to_key

N = int(sys.stdin.readline())
cord_list = []
for _ in range(N):
    x, y, b_convex = sys.stdin.readline().split()
    if b_convex == "N":
        continue
    x, y = int(x), int(y)

    cord_list.append([x, y])

cord_list.sort(key = lambda x : [x[0], x[1]])
print(len(cord_list))
x_0, y_0 = cord_list[0]

def ccw(x1, y1, x2, y2, x3, y3):
    v1 = [x2-x1, y2-y1]
    v2 = [x3-x1, y3-y1]

    ccw_v = v1[0]*v2[1]-v1[1]*v2[0]

    return ccw_v

def compare(a, b):
    x1, y1 = a
    x2, y2 = b

    ccw_v = ccw(x_0, y_0, x1, y1, x2, y2)

    if ccw_v > 0:
        return -1
    elif ccw_v < 0:
        return 1
    else:
        dist1 = (x_0-x1)**2 + (y_0-y1)**2
        dist2 = (x_0-x2)**2 + (y_0-y2)**2

        if dist1 < dist2:
            return -1
        else:
            return 1

cord_list.sort(key = cmp_to_key(compare))
x_last, y_last = cord_list[-1]
reverse_list = []
for i in range(len(cord_list)-1, -1, -1):
    t_x, t_y = cord_list[i]
    if ccw(x_0, y_0, x_last, y_last, t_x, t_y) == 0:
        reverse_list.append(cord_list[i])
    else:
        break

for i in range(len(cord_list)-len(reverse_list)):
    x, y = cord_list[i]
    print(x,y)
for x, y in reverse_list:
    print(x, y)

explain ="""Angle sorting with CCW(Counter Clock Wise) Algorithm.
"""