import sys
from functools import cmp_to_key

def ccw(x1, y1, x2, y2, x3, y3):
    v1 = [x2-x1, y2-y1]
    v2 = [x3-x1, y3-y1]
    return v1[0]*v2[1]-v1[1]*v2[0]

T = int(sys.stdin.readline())

for _ in range(T):
    cur_line = list(map(int, sys.stdin.readline().split()))
    node_num = cur_line[0]

    cord_list = []

    for i in range(node_num):
        x, y = cur_line[1+2*i:3+2*i]
        cord_list.append([x, y, i])

    cord_list.sort(key = lambda x: [x[1], x[0]])
    x_0, y_0, _ = cord_list[0]


    def compare(x1, x2):
        ccw_v = ccw(x_0, y_0, x1[0], x1[1], x2[0], x2[1])

        if ccw_v != 0:
            if ccw_v < 0:
                return 1
            else:
                return -1
        else:
            if (x_0-x1[0])**2 + (y_0-x1[1])**2 < (x_0-x2[0])**2 + (y_0-x2[1])**2:
                return -1
            else:
                return 1
        return 0
    cord_list.sort(key = cmp_to_key(compare))

    reverse_idx_list = []

    x_last, y_last, _ = cord_list[-1]
    for i in range(len(cord_list)-1, -1, -1):
        ccw_v = ccw(x_0, y_0, x_last, y_last, cord_list[i][0], cord_list[i][1])
        if ccw_v == 0:
            reverse_idx_list.append(cord_list[i][2])

        else:
            break

    for i in range(len(cord_list)-len(reverse_idx_list)):
        print(cord_list[i][2], end=" ")
    for i in range(len(reverse_idx_list)):
        print(reverse_idx_list[i], end=" ")
    print()