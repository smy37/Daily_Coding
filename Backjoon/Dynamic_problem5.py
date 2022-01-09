import sys

iter_num = int(sys.stdin.readline())

fir_temp = list(map(int, sys.stdin.readline().rstrip().split()))
temp_0 = [[fir_temp[0]], [fir_temp[1]], [fir_temp[2]]]

for k in range(iter_num-1):
    temp = [[],[],[]]
    sec_temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(3):
        for j in temp_0[i]:
            if i == 0:
                temp[1].append(j+sec_temp[1])
                temp[2].append(j+sec_temp[2])
            elif i ==1:
                temp[0].append(j+sec_temp[0])
                temp[2].append(j+sec_temp[2])
            elif i ==2:
                temp[0].append(j+sec_temp[0])
                temp[1].append(j+sec_temp[1])

        if i==0:
            temp[1] = [min(temp[1])]
            temp[2] = [min(temp[2])]
        elif i==1:
            temp[0] = [min(temp[0])]
            temp[2] = [min(temp[2])]
        elif i==2:
            temp[0] = [min(temp[0])]
            temp[1] = [min(temp[1])]

    temp_0 = temp

temp2 = []
for i in temp_0:
    temp2.append(min(i))
print(min(temp2))