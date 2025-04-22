import sys
import math

iter_num = int(sys.stdin.readline())

def cal_distance(A,B):
    return (A[0]-B[0])**2+(A[1]-B[1])**2


def closest_pair(cordlist):
    if len(cordlist) == 2:
        return cal_distance(cordlist[0], cordlist[1])
    elif len(cordlist) == 1:
        return math.inf

    else:
        t_cri = len(cordlist)//2
        temp1 = cordlist[:t_cri]
        temp2 = cordlist[t_cri:]

        min_d1 = closest_pair(temp1)
        min_d2 = closest_pair(temp2)
        min_d1 = min(min_d1, min_d2)


        temp3 = []
        for i in range(len(temp1)):
            if abs(temp1[i][0]-temp2[0][0])**2 < min_d1:
                temp3.append(temp1[i])
        for i in range(len(temp2)):
            if abs(temp2[i][0]-temp2[0][0])**2 < min_d1:
                temp3.append(temp2[i])

        temp3 = sorted(temp3, key = lambda x: x[1])

        for i in range(len(temp3)):
            for j in range(i+1, len(temp3)):
                if abs(temp3[i][1]-temp3[j][1])**2 < min_d1:
                    temp_d = cal_distance(temp3[i], temp3[j])
                    min_d1 = min(min_d1, temp_d)
                else:
                    break

        return min_d1


if __name__ == '__main__':
    cord_list = []
    for i in range(iter_num):
        n, m = list(map(int, sys.stdin.readline().split(' ')))
        cord_list.append([n,m])
    print(closest_pair(sorted(cord_list)))
