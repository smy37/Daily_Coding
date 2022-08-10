import sys
import math
import copy

N, K = map(int, sys.stdin.readline().split(' '))
num_iter = list(map(int, sys.stdin.readline().split(' ')))
final_cnt = 0
sensor = False
while 1:
    for i in range(N-1):
        if max(num_iter)-min(num_iter) <= K:
            print(final_cnt)
            sensor = True
            break
    if sensor:
        break
    ### Step1. Add
    cri_min = min(num_iter)
    for i in range(len(num_iter)):
        if num_iter[i] == cri_min:
            num_iter[i] +=1
    pan = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(0)
        pan.append(temp)


    for i in range(N):
        pan[N-1][i] = num_iter[i]




    ### Step2. Rotation
    s_n = 0
    rest = 1
    width = 1
    height = 1
    while height <= N-rest:
        for i in range(height):
            for j in range(width):

                pan[N-1-(j+1)][rest+i] = pan[N-1-i][rest-j-1]
                pan[N-1-i][rest - j - 1] = 0



        width = int(math.ceil(s_n/2)) + 1
        height = (s_n//2) + 2
        rest += width
        s_n += 1


    new_pan = copy.deepcopy(pan)

    for i in range(N-1, N-height-1, -1):

        for j in range(rest-width, N):

            if pan[i][j] == 0:
                continue

            if i+1 < N and pan[i+1][j]!=0:
                if abs(pan[i][j] - pan[i+1][j])//5 >=1:
                    if pan[i][j] > pan[i+1][j]:
                        new_pan[i][j] -= abs(pan[i][j] - pan[i+1][j])//5
                        new_pan[i+1][j] += abs(pan[i][j] - pan[i+1][j])//5
                    elif pan[i][j] < pan[i+1][j]:
                        new_pan[i][j] += abs(pan[i][j] - pan[i+ 1][j]) // 5
                        new_pan[i + 1][j] -= abs(pan[i][j] - pan[i + 1][j]) // 5

            if j+1 < N and pan[i][j+1] !=0:
                if abs(pan[i][j] - pan[i][j+1]) // 5 >= 1:
                    if pan[i][j] > pan[i][j+1]:
                        new_pan[i][j] -= abs(pan[i][j] - pan[i][j+1]) // 5
                        new_pan[i][j+1] += abs(pan[i][j] - pan[i][j+1]) // 5
                    elif pan[i][j] < pan[i][j+1]:
                        new_pan[i][j] += abs(pan[i][j] - pan[i][j + 1]) // 5
                        new_pan[i][j + 1] -= abs(pan[i][j] - pan[i][j + 1]) // 5



    new_array = []
    for i in range(N):
        new_array.append(0)
    cnt = 0
    for i in range(rest-width, N):
        for j in range(N-1, N-height-1, -1):
            if new_pan[j][i] == 0:
                continue

            new_array[cnt] = new_pan[j][i]
            cnt +=1


    cri  = N//2 -1
    temp1 = []
    temp2 = []
    for i in range(2):
        temp = []
        for j in range(N//2):
            temp.append(0)
        temp1.append(temp)

    for i in range(4):
        temp = []
        for j in range(((N//2)//2)):
            temp.append(0)
        temp2.append(temp)

    for i in range(N//2):
        temp1[0][cri-i] = new_array[i]
        temp1[1][cri-i] = new_array[N-1-i]


    for j in range((N//2)//2):
        temp2[0][(N//2)//2-1-j] = temp1[1][j]
        temp2[1][(N//2)//2-1-j] = temp1[0][j]
        temp2[2][(N//2)//2-1-j] = temp1[0][cri-j]
        temp2[3][(N//2)//2-1-j] = temp1[1][cri-j]

    n_c = (N//2)//2
    final = copy.deepcopy(temp2)
    for i in range(4):
        for j in range(n_c):
            if j+1 < n_c:
                t_c = abs(temp2[i][j]- temp2[i][j+1])//5
                if t_c >=1:
                    if temp2[i][j] > temp2[i][j+1]:
                        final[i][j+1] += t_c
                        final[i][j] -= t_c
                    elif temp2[i][j] < temp2[i][j+1]:
                        final[i][j+1] -= t_c
                        final[i][j] += t_c
            if i+1 <4:
                t_c = abs(temp2[i][j]- temp2[i+1][j])//5
                if t_c >=1:
                    if temp2[i][j] > temp2[i+1][j]:
                        final[i][j] -= t_c
                        final[i+1][j] += t_c
                    elif temp2[i][j] < temp2[i+1][j]:
                        final[i][j] += t_c
                        final[i+1][j] -= t_c


    answer = []
    for i in range(n_c):
        for j in range(4):
            answer.append(final[3-j][i])
    final_cnt +=1
    num_iter = answer
