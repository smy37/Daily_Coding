import sys
import math
start = int(sys.stdin.readline())

def find_convex(node_list):
    conv_list = []
    conv_node = []
    node_list = sorted(node_list)
    for i in range(len(node_list)):
        x1, y1 = node_list[i][0], node_list[i][1]
        for j in range(i+1, len(node_list)):
            sensor1, sensor2 = False, False
            sensor3 = True
            x2, y2 = node_list[j][0], node_list[j][1]
            a = y1-y2
            b = -x1 + x2
            c = x1*y2-x2*y1
            for k in range(len(node_list)):
                if node_list[i] != node_list[k] and node_list[j] != node_list[k]:
                    value = a*node_list[k][0] + b*node_list[k][1] + c
                    if value > 0:
                        sensor1 = True
                    elif value < 0:
                        sensor2 = True

                    else:
                        if node_list[k] < node_list[i] or node_list[k] > node_list[j]:
                            sensor3 = False
                            break
                if sensor1 and sensor2:
                    sensor3 = False
                    break
            if sensor3:
                conv_list.append([node_list[i], node_list[j]])
                if node_list[i] not in conv_node:
                    conv_node.append(node_list[i])
                if node_list[j] not in conv_node:
                    conv_node.append(node_list[j])


    return conv_list, conv_node

cnt = 1
while start != 0:
    final = []
    node_list = []
    for i in range(start):
        node_list.append(list(map(int, sys.stdin.readline().strip().split(' '))))
    convex, conv_node = find_convex(node_list)
    for line in convex:
        temp_max = []
        x1, y1, x2, y2 = line[0][0], line[0][1], line[1][0], line[1][1]
        a = y1-y2
        b = -x1 +x2
        c = x1*y2 - x2*y1
        for node in conv_node:
            x3, y3 = node[0], node[1]
            temp_max.append(abs(a*x3+b*y3+c)/math.sqrt(a**2+b**2))
        final.append(max(temp_max))
    answer = min(final)*100

    print(f'Case {cnt}: {math.ceil(answer)/100:.2f}')
    start = int(sys.stdin.readline())
    cnt+=1