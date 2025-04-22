import sys


def cross_check(rec1 : list, rec2 : list) -> bool:          ## 사각형이 겹치는지 판단
    if (rec1[0]>rec2[2] or rec1[2]<rec2[0] or rec1[1] > rec2[3] or rec1[3] < rec2[1]):
        sensor = False
    else:
        sensor = True
    return sensor

def inner_check(dot, rec):      ## 한점이 사각형 내부에 존재하는지 판단
    if dot[0]>rec[0] and dot[0] <rec[2] and dot[1] <rec[3] and dot[1]>rec[1]:
        return False
    else:
        return True

def insert_start(temp_true_dot, characterX, characterY):
    c_vertical_list1 = []
    c_vertical_list2 = []
    c_horizontal_list1 = []
    c_horizontal_list2 = []
    for i in range(len(temp_true_dot)):
        if temp_true_dot[i][0] == characterX:
            if temp_true_dot[i][1] > characterY:
                c_vertical_list1.append(temp_true_dot[i])
            elif temp_true_dot[i][1] < characterY:
                c_vertical_list2.append(temp_true_dot[i])
        if temp_true_dot[i][1] == characterY:
            if temp_true_dot[i][0] > characterX:
                c_horizontal_list1.append(temp_true_dot[i])
            elif temp_true_dot[i][0] < characterX:
                c_horizontal_list2.append(temp_true_dot[i])
    c_vertical_list1 = sorted(c_vertical_list1, key=lambda x: x[1])
    c_vertical_list2 = sorted(c_vertical_list2, key=lambda x: x[1], reverse=True)
    c_horizontal_list1 = sorted(c_horizontal_list1, key=lambda x: x[0])
    c_horizontal_list2 = sorted(c_horizontal_list2, key=lambda x: x[0], reverse=True)

    cri1, cri2 = -1, -1
    if len(c_vertical_list1) >= 1 and len(c_vertical_list2) >= 1:
        cri1 = temp_true_dot.index(c_vertical_list1[0])
        cri2 = temp_true_dot.index(c_vertical_list2[0])

    elif len(c_horizontal_list1) >= 1 and len(c_horizontal_list2) >= 1:
        cri1 = temp_true_dot.index(c_horizontal_list1[0])
        cri2 = temp_true_dot.index(c_horizontal_list2[0])

    real_cri = min(cri1, cri2)
    real_cri2 = max(cri1, cri2)
    if real_cri == 0 and real_cri2 == len(temp_true_dot)-1:
        temp_true_dot = [[characterX, characterY]] + temp_true_dot
    else:
        temp_true_dot = temp_true_dot[:real_cri + 1] + [[characterX, characterY]] + temp_true_dot[real_cri + 1:]

    return temp_true_dot
def insert_end(temp_true_dot, itemX, itemY):
    i_vertical_list1 = []
    i_vertical_list2 = []
    i_horizontal_list1 = []
    i_horizontal_list2 = []
    for i in range(len(temp_true_dot)):
        if temp_true_dot[i][0] == itemX:
            if temp_true_dot[i][1] > itemY:
                i_vertical_list1.append(temp_true_dot[i])
            elif temp_true_dot[i][1] < itemY:
                i_vertical_list2.append(temp_true_dot[i])
        if temp_true_dot[i][1] == itemY:
            if temp_true_dot[i][0] > itemX:
                i_horizontal_list1.append(temp_true_dot[i])
            elif temp_true_dot[i][0] < itemX:
                i_horizontal_list2.append(temp_true_dot[i])
    i_vertical_list1 = sorted(i_vertical_list1, key=lambda x: x[1])
    i_vertical_list2 = sorted(i_vertical_list2, key=lambda x: x[1], reverse=True)
    i_horizontal_list1 = sorted(i_horizontal_list1, key=lambda x: x[0])
    i_horizontal_list2 = sorted(i_horizontal_list2, key=lambda x: x[0], reverse=True)

    cri1, cri2 = -1, -1
    if len(i_vertical_list1) >= 1 and len(i_vertical_list2) >= 1:
        cri1 = temp_true_dot.index(i_vertical_list1[0])
        cri2 = temp_true_dot.index(i_vertical_list2[0])

    elif len(i_horizontal_list1) >= 1 and len(i_horizontal_list2) >= 1:
        cri1 = temp_true_dot.index(i_horizontal_list1[0])
        cri2 = temp_true_dot.index(i_horizontal_list2[0])

    real_cri = min(cri1, cri2)
    real_cri2 = max(cri1, cri2)
    if real_cri == 0 and real_cri2 == len(temp_true_dot) - 1:
        temp_true_dot = [[itemX, itemY]] + temp_true_dot[real_cri + 1:]
    else:
        temp_true_dot = temp_true_dot[:real_cri + 1] + [[itemX, itemY]] + temp_true_dot[real_cri + 1:]
    return temp_true_dot
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    test = rectangle
    total_dot = []
    test = sorted(test, key=lambda x: x[0])


    ## 1. 두개의 사각형에 대하여 겹치는 사각형인지 판단 후 겹친다면 겹치는 상황별로 교점을 구해줌.
    for i in range(len(test)):
        for j in range(i):
            temp_b = cross_check(test[j], test[i])
            print(f'{i + 1}번째 사각형과 {j + 1}번째 사각형은 {temp_b}')
            if temp_b == True:
                if test[j][3] < test[i][3]:         ## Right Rectangle High
                    if test[j][1] < test[i][1]:
                        if test[i][0] > test[j][0] and test[i][2] < test[j][2]:
                            cross_dot1 = [test[i][0],test[j][3]]
                            cross_dot2 = [test[i][2],test[j][3]]
                            total_dot.append(cross_dot1)
                            total_dot.append(cross_dot2)
                        elif test[i][0] > test[j][0]:
                            cross_dot1 = [test[i][0], test[j][3]]
                            cross_dot2 = [test[j][2], test[i][1]]
                            total_dot.append(cross_dot1)
                            total_dot.append(cross_dot2)
                    elif test[j][1] > test[i][1]:
                        if test[i][2] > test[j][2]:
                            cross_dot1 = [test[i][0], test[j][3]]
                            cross_dot2 = [test[i][0], test[j][1]]
                            total_dot.append(cross_dot1)
                            total_dot.append(cross_dot2)
                        else:
                            cross_dot1 = [test[i][0], test[j][3]]
                            cross_dot2 = [test[i][2], test[j][3]]
                            cross_dot3 = [test[i][0], test[j][1]]
                            cross_dot4 = [test[i][2], test[j][1]]
                            total_dot.append(cross_dot1)
                            total_dot.append(cross_dot2)
                            total_dot.append(cross_dot3)
                            total_dot.append(cross_dot4)

                elif test[j][3] > test[i][3]:       ## Right Rectangle Low
                    if test[i][1] > test[j][1]:
                        cross_dot1 = [test[j][2], test[i][3]]
                        cross_dot2 = [test[j][2], test[i][1]]
                        total_dot.append(cross_dot1)
                        total_dot.append(cross_dot2)
                    elif test[i][1] < test[j][1]:
                        if test[i][2] > test[j][2]:
                            cross_dot1 = [test[j][2], test[i][3]]
                            cross_dot2 = [test[i][0], test[j][1]]
                            total_dot.append(cross_dot1)
                            total_dot.append(cross_dot2)
                        else:
                            cross_dot1 = [test[i][2], test[j][1]]
                            cross_dot2 = [test[i][0], test[j][1]]
                            total_dot.append(cross_dot1)
                            total_dot.append(cross_dot2)


    print()
    ## 2. Place the four vertices above rectangle in the list with the intersections obtained in process 1
    for i in range(len(test)):
        n1, n2, n3, n4 = [test[i][0], test[i][1]], [test[i][0], test[i][3]], [test[i][2], test[i][1]], [test[i][2],
                                                                                                        test[i][3]]
        temp1 = [n1, n2, n3, n4]
        total_dot.append(n1)
        total_dot.append(n2)
        total_dot.append(n3)
        total_dot.append(n4)
        for j in range(i + 1, len(test)):
            n5, n6, n7, n8 = [test[j][0], test[j][1]], [test[j][0], test[j][3]], [test[j][2], test[j][1]], [test[j][2],
                                                                                                            test[j][3]]
            temp2 = [n5, n6, n7, n8]

    print(total_dot)
    print(len(total_dot))


    ## 3. Remove the dot inside squares from True-Dot list
    true_dot = []
    for dot in total_dot:
        sensor = True
        if dot not in true_dot:
            for rec in test:
                if inner_check(dot, rec) == False:
                    sensor = False
                    break
        if sensor:
            true_dot.append(dot)
    true_dot = sorted(true_dot, key=lambda x: [x[1], x[0]])
    temp_true_dot = []


    ## 4. Find Outline by tracking node step by step.
    temp1 = []
    temp2 = []
    for i in range(1,len(true_dot)):
        if true_dot[i][1] == true_dot[0][1]:
            temp1.append(true_dot[i])
        if true_dot[i][0] == true_dot[0][0]:
            temp2.append(true_dot[i])
    temp1 = sorted(temp1, key = lambda x : x[0])
    temp2 = sorted(temp2, key = lambda x : x[1])
    dir = -1
    if len(temp1) > 0:
        temp_true_dot.append(temp1[0])
        dir = 3
    elif len(temp2)> 0:
        temp_true_dot.append(temp2[0])
        dir = 0
    while (len(true_dot) >2 and true_dot[0] == temp_true_dot[-1]) == False:
        tem1 = []
        tem2 = []
        tem3 = []
        if dir == 0:
            for i in range(len(true_dot)):
                if true_dot[i] not in temp_true_dot:
                    if temp_true_dot[-1][1] == true_dot[i][1] and temp_true_dot[-1][0]  < true_dot[i][0]:
                        tem1.append(true_dot[i])
                    elif temp_true_dot[-1][0] == true_dot[i][0] and temp_true_dot[-1][1] < true_dot[i][1]:
                        tem2.append(true_dot[i])
                    elif temp_true_dot[-1][1] == true_dot[i][1] and temp_true_dot[-1][0]  > true_dot[i][0]:
                        tem3.append(true_dot[i])
            tem1 = sorted(tem1, key = lambda x : x[0])
            tem2 = sorted(tem2, key = lambda x : x[1])
            tem3 = sorted(tem3, key = lambda x : -x[0])
            if len(tem1)>0:
                temp_true_dot.append(tem1[0])
                dir = 3
            elif len(tem2)>0:
                temp_true_dot.append(tem2[0])
                dir = 0
            elif len(tem3)>0:
                temp_true_dot.append(tem3[0])
                dir = 2

        elif dir == 1:
            for i in range(len(true_dot)):
                if true_dot[i] not in temp_true_dot:
                    if temp_true_dot[-1][1] == true_dot[i][1] and temp_true_dot[-1][0] > true_dot[i][0]:
                        tem1.append(true_dot[i])
                    elif temp_true_dot[-1][0] == true_dot[i][0] and temp_true_dot[-1][1] > true_dot[i][1]:
                        tem2.append(true_dot[i])
                    elif temp_true_dot[-1][1] == true_dot[i][1] and temp_true_dot[-1][0] < true_dot[i][0]:
                        tem3.append(true_dot[i])
            tem1 = sorted(tem1, key=lambda x: -x[0])
            tem2 = sorted(tem2, key=lambda x: -x[1])
            tem3 = sorted(tem3, key=lambda x: x[0])
            if len(tem1)>0:
                temp_true_dot.append(tem1[0])
                dir = 2
            elif len(tem2)>0:
                temp_true_dot.append(tem2[0])
                dir = 1
            elif len(tem3)>0:
                temp_true_dot.append(tem3[0])
                dir = 3
        elif dir == 2:
            for i in range(len(true_dot)):
                if true_dot[i] not in temp_true_dot:
                    if temp_true_dot[-1][0] == true_dot[i][0] and temp_true_dot[-1][1] < true_dot[i][1]:
                        tem1.append(true_dot[i])
                    elif temp_true_dot[-1][1] == true_dot[i][1] and temp_true_dot[-1][0] > true_dot[i][0]:
                        tem2.append(true_dot[i])
                    elif temp_true_dot[-1][0] == true_dot[i][0] and temp_true_dot[-1][1] > true_dot[i][1]:
                        tem3.append(true_dot[i])
            tem1 = sorted(tem1, key=lambda x: x[1])
            tem2 = sorted(tem2, key=lambda x: -x[0])
            tem3 = sorted(tem3, key=lambda x: -x[1])
            if len(tem1)>0:
                temp_true_dot.append(tem1[0])
                dir = 0
            elif len(tem2)>0:
                temp_true_dot.append(tem2[0])
                dir = 2
            elif len(tem3)>0:
                temp_true_dot.append(tem3[0])
                dir = 1
        elif dir == 3:
            for i in range(len(true_dot)):
                if true_dot[i] not in temp_true_dot:
                    if temp_true_dot[-1][0] == true_dot[i][0] and temp_true_dot[-1][1] > true_dot[i][1]:
                        tem1.append(true_dot[i])
                    elif temp_true_dot[-1][1] == true_dot[i][1] and temp_true_dot[-1][0] < true_dot[i][0]:
                        tem2.append(true_dot[i])
                    elif temp_true_dot[-1][0] == true_dot[i][0] and temp_true_dot[-1][1] < true_dot[i][1]:
                        tem3.append(true_dot[i])
            tem1 = sorted(tem1, key=lambda x: -x[1])
            tem2 = sorted(tem2, key=lambda x: x[0])
            tem3 = sorted(tem3, key=lambda x: x[1])
            if len(tem1)>0:
                temp_true_dot.append(tem1[0])
                dir = 1
            elif len(tem2)>0:
                temp_true_dot.append(tem2[0])
                dir = 3
            elif len(tem3)>0:
                temp_true_dot.append(tem3[0])
                dir = 0
    print(temp_true_dot)

    ## 5. Insert start node and end node in graph
    if [characterX, characterY] in temp_true_dot and [itemX, itemY] in temp_true_dot:
        start = temp_true_dot.index([characterX, characterY])
        end = temp_true_dot.index([itemX, itemY])
    elif [characterX, characterY] in temp_true_dot:
        temp_true_dot = insert_end(temp_true_dot, itemX, itemY)
        start = temp_true_dot.index([characterX, characterY])
        end = temp_true_dot.index([itemX, itemY])
    elif [itemX, itemY] in temp_true_dot:
        temp_true_dot = insert_start(temp_true_dot, characterX, characterY)
        start = temp_true_dot.index([characterX, characterY])
        end = temp_true_dot.index([itemX, itemY])
    else:
        temp_true_dot = insert_start(temp_true_dot, characterX, characterY)
        temp_true_dot = insert_end(temp_true_dot, itemX, itemY)
        start = temp_true_dot.index([characterX, characterY])
        end = temp_true_dot.index([itemX, itemY])
    print(temp_true_dot)

    ## 6. Calculate route length of two paths.
    start2 = int(start)
    answer1 = 0
    while start != end:
        start += 1
        if start == len(temp_true_dot):
            answer1 += abs(temp_true_dot[start-1][0] - temp_true_dot[0][0]) + abs(temp_true_dot[start-1][1] - temp_true_dot[0][1])
            start = 0
        else:
            answer1 += abs(temp_true_dot[start][0] - temp_true_dot[start-1][0]) + abs(temp_true_dot[start][1] - temp_true_dot[start-1][1])
    answer2 = 0
    while start2 != end:
        start2 -= 1
        if start2 == -1:
            answer2 += abs(temp_true_dot[0][0]-temp_true_dot[-1][0]) + abs(temp_true_dot[0][1] - temp_true_dot[-1][1])
            start2 = len(temp_true_dot)-1
        else:
            answer2 += abs(temp_true_dot[start2][0] - temp_true_dot[start2+1][0]) + abs(temp_true_dot[start2][1] - temp_true_dot[start2+1][1])
    answer = min(answer1, answer2)

    return answer



if __name__ == '__main__':              ## Test Stage!!
    test = 	[[2,1,7,5],[6,4,10,10]]
    rec = {}
    characterX = 3
    characterY = 1
    itemX = 7
    itemY = 10
    print(solution(test, characterX, characterY, itemX, itemY))