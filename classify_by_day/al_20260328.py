import sys

N = int(sys.stdin.readline())

def get_cord(edge_type, dist):
    if edge_type == 1:
        return [dist, 50]
    elif edge_type == 2:
        return [dist, 0]
    elif edge_type == 3:
        return [0, 50-dist]
    elif edge_type == 4:
        return [50, 50-dist]


node_list = []
for _ in range(N//2):
    p1_edge, p1_dist, p2_edge, p2_dist = map(int, sys.stdin.readline().split())

    node1 = get_cord(p1_edge, p1_dist)
    node2 = get_cord(p2_edge, p2_dist)


    node_list.append(sorted([node1, node2], key = lambda x : [x[0], x[1]]))

global_cross = 0
max_checker = {i : 0 for i in range(N)}
for i in range(len(node_list)):
    temp_cross = 0
    n1 = node_list[i]

    [x1, y1], [x2, y2] = n1[0], n1[1]
    ab = (x1-x2, y1-y2)
    for j in range(i+1, len(node_list)):
        n2 = node_list[j]
        [x3, y3], [x4, y4] = n2[0], n2[1]
        ac = (x1-x3, y1-y3)
        ad = (x1-x4, y1-y4)

        ccw1 = ab[0]*ac[1]-ab[1]*ac[0]
        ccw2 = ab[0]*ad[1]-ab[1]*ad[0]

        if ccw1 *ccw2 < 0:
            temp_cross +=1
            max_checker[i] +=1
            max_checker[j] += 1
        elif ccw1*ccw2 == 0:

            if ccw1 == 0 and ccw2 == 0:
                if x1 == x3:
                    if min(y1, y2) <= min(y3, y4):
                        if min(y3, y4) < max(y1, y2) and max(y3, y4) > max(y1, y2):
                            temp_cross += 1
                            max_checker[i] += 1
                            max_checker[j] += 1
                    else:
                        if max(y3, y4) > min(y1, y2) and max(y3, y4) < max(y1, y2):
                            temp_cross += 1
                            max_checker[i] += 1
                            max_checker[j] += 1
                else:
                    if min(x1, x2) <= min(x3, x4):
                        if min(x3, x4) < max(x1, x2) and max(x1, x2) < max(x3, x4):
                            temp_cross += 1
                            max_checker[i] += 1
                            max_checker[j] += 1
                    else:
                        if min(x1, x2) < max(x3, x4) and max(x1, x2) > max(x3, x4):
                            temp_cross += 1
                            max_checker[i] += 1
                            max_checker[j] += 1
            else:
                if ccw1 == 0:
                    cri_x, cri_y = x3, y3
                elif ccw2 == 0:
                    cri_x, cri_y = x4, y4
                if min(x1, x2) <= cri_x and cri_x<= max(x1, x2) and min(y1, y2) <= cri_y and cri_y <= max(y1, y2):
                    temp_cross += 1
                    max_checker[i] += 1
                    max_checker[j] += 1

    global_cross += temp_cross


print(global_cross)
print(max(max_checker.values()))