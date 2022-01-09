import sys

dynamic_list = {}

dynamic_list[(1,1,1)] = 2

for i in range(1,21):
    for j in range(1,21):
        for k in range(1,21):
            dynamic_list[(i,j,k)] = 0


for i,a in dynamic_list.items():
    if i[0]<i[1] and i[1]<i[2]:
        temp1 = (i[0], i[1], i[2]-1)
        temp2 = (i[0], i[1]-1, i[2]-1)
        temp3 = (i[0], i[1]-1, i[2])
        if temp1[2]<=0:
            temp1 = 1
        elif dynamic_list[temp1] != 0:
            temp1 = dynamic_list[temp1]

        if temp2[1]<=0 or temp2[2]<=0:
            temp2 = 1
        elif dynamic_list[temp2] != 0:
            temp2 = dynamic_list[temp2]

        if temp3[1]<=0:
            temp3 = 1
        elif dynamic_list[temp3] != 0:
            temp3 = dynamic_list[temp3]

        dynamic_list[i] = temp1+temp2-temp3

    else:
        temp1 = (i[0]-1, i[1], i[2])
        temp2 = (i[0]-1, i[1] - 1, i[2])
        temp3 = (i[0]-1, i[1], i[2]-1)
        temp4 = (i[0]-1, i[1]-1, i[2]-1)

        if temp1[0]<=0:
            temp1 = 1
        elif dynamic_list[temp1] != 0:
            temp1 = dynamic_list[temp1]

        if temp2[0]<=0 or temp2[1]<=0:
            temp2 = 1
        elif dynamic_list[temp2] != 0:
            temp2 = dynamic_list[temp2]

        if temp3[0]<=0 or temp3[2]<=0:
            temp3 = 1
        elif dynamic_list[temp3] != 0:
            temp3 = dynamic_list[temp3]

        if temp4[0] <=0 or temp4[1] <= 0 or temp4[2] <=0:
            temp4 = 1
        elif dynamic_list[temp4] != 0:
            temp4 = dynamic_list[temp4]

        dynamic_list[i] = temp1 + temp2 + temp3 -temp4


while True:
    num = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    if num == [-1,-1,-1]:
        break
    if num[0]<1 or num[1]<1 or num[2]<1:
        print(f'w({num[0]}, {num[1]}, {num[2]}) = 1')
    elif num[0]>20 or num[1]>20 or num[2]>20:
        print(f'w({num[0]}, {num[1]}, {num[2]}) = {dynamic_list[(20, 20, 20)]}')
    else:
        print(f'w({num[0]}, {num[1]}, {num[2]}) = {dynamic_list[(num[0], num[1], num[2])]}')