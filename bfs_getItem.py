test = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
rec = {}


def cross_check(rec1, rec2):
    if (rec1[0]>rec2[2] or rec1[2]<rec2[0] or rec1[1] > rec2[3] or rec1[3] < rec2[1]):
        sensor = False
    else:
        sensor = True
    return sensor

def inner_check(dot, rec):
    if dot[0]>rec[0] and dot[0] <rec[2] and dot[1] <rec[3] and dot[1]>rec[1]:
        return False
    else:
        return True
total_dot = []
test = sorted(test, key = lambda x : x[0])
print(test)
for i in range(len(test)):
    for j in range(i):
        temp_b = cross_check(test[j],test[i])
        print(f'{i+1}번째 사각형과 {j+1}번째 사각형은 {temp_b}')
        if temp_b == True:
            if test[j][3] < test[i][3] and test[j][1] > test[i][1]:
                if test[j][2] > test[i][2]:
                    cross_dot1 = [test[i][0], test[j][3]]
                    cross_dot2 = [test[i][0], test[j][1]]
                    cross_dot3 = [test[i][2], test[j][3]]
                    cross_dot4 = [test[i][2], test[j][1]]
                    print(cross_dot1)
                    print(cross_dot2)
                    print(cross_dot3)
                    print(cross_dot4)
                    total_dot.append(cross_dot1)
                    total_dot.append(cross_dot2)
                    total_dot.append(cross_dot3)
                    total_dot.append(cross_dot4)
                elif test[j][2] < test[i][2]:
                    cross_dot1 = [test[i][0], test[j][3]]
                    cross_dot2 = [test[i][0], test[j][1]]
                    print(cross_dot1)
                    print(cross_dot2)
                    total_dot.append(cross_dot1)
                    total_dot.append(cross_dot2)
            else:
                if test[j][3] < test[i][3]:
                    if test[j][2] > test[i][2]:
                        cross_dot1 = [test[i][0],test[j][3]]
                        cross_dot2 = [test[i][2],test[j][3]]
                        print(cross_dot1)
                        print(cross_dot2)
                        total_dot.append(cross_dot1)
                        total_dot.append(cross_dot2)
                    elif test[j][2] < test[i][2]:
                        cross_dot1 = [test[i][0], test[j][3]]
                        cross_dot2 = [test[j][2], test[i][1]]
                        print(cross_dot1)
                        print(cross_dot2)
                        total_dot.append(cross_dot1)
                        total_dot.append(cross_dot2)
                if test[j][1] > test[i][1]:
                    if test[j][2] > test[i][2]:
                        cross_dot1 = [test[i][0], test[j][1]]
                        cross_dot2 = [test[i][2], test[j][1]]
                        print(cross_dot1)
                        print(cross_dot2)
                        total_dot.append(cross_dot1)
                        total_dot.append(cross_dot2)
                    elif test[j][2] < test[i][2]:
                        cross_dot1 = [test[i][0], test[j][1]]
                        cross_dot2 = [test[j][2], test[i][3]]
                        print(cross_dot1)
                        print(cross_dot2)
                        total_dot.append(cross_dot1)
                        total_dot.append(cross_dot2)

print()
for i in range(len(test)):
    n1, n2, n3, n4 = [test[i][0], test[i][1]], [test[i][0], test[i][3]], [test[i][2], test[i][1]], [test[i][2],test[i][3]]
    temp1 = [n1,n2,n3,n4]
    total_dot.append(n1)
    total_dot.append(n2)
    total_dot.append(n3)
    total_dot.append(n4)
    for j in range(i+1,len(test)):
        n5, n6, n7, n8 = [test[j][0], test[j][1]], [test[j][0], test[j][3]], [test[j][2], test[j][1]], [test[j][2],test[j][3]]
        temp2 = [n5,n6,n7,n8]

        for k in range(4):
            if inner_check(temp1[k],test[j]) == False:
                print(temp1[k])
            if inner_check(temp2[k], test[i]) == False:
                print(temp2[k])

print(total_dot)
print(len(total_dot))

true_dot = []
for dot in total_dot:
    sensor = True
    if dot not in true_dot:
        for rec in test:
            if inner_check(dot,rec) == False:
                sensor = False
                break
    if sensor:
        true_dot.append(dot)
print(true_dot)
print(len(true_dot))

c_x = 1
c_y = 3
i_x = 7
i_y = 8
# def checker(point, rec):
#     if point[0] > rec[0] and point[0] < rec[2] and point[1] >rec[1] and point[1] <rec[3]:
#         return True
#     else:
#         return False
#
# def checker2(rec1, rec2):
#     h_l = rec1[0]
#     h_r = rec1[2]
#     v_b = rec1[1]
#     v_t = rec1[3]
#
# for i in range(len(test)):
#     rec[i+1] = []
# cnt = 1
# for i in test:
#     print(i[0],i[1])
#     print(i[0],i[3])
#     print(i[2],i[3])
#     print(i[2],i[1])
#     print()
#     rec[cnt].append([i[0],i[1]])
#     rec[cnt].append([i[0],i[3]])
#     rec[cnt].append([i[2],i[3]])
#     rec[cnt].append([i[2],i[1]])
#     cnt +=1
#
# for i in rec.keys():
#     for j in rec[i]:
#         sensor = True
#         for k in test:
#             if checker(j, k):
#                 sensor = False
#                 break
#         if sensor == False:
#             print(j, k)
#             print(j)
#             print()