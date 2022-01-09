import sys

length = int(sys.stdin.readline())
num_list = []

for i in range(length):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    num_list.append(temp)


def dAc(s1, s2, length):
    for i in range(length):
        for j in range(length):
            if num_list[s1][s2] != num_list[s1+i][s2+j]:
                length = length//3
                a1 = dAc(s1, s2, length)
                a2 = dAc(s1, s2+length, length)
                a3 = dAc(s1, s2+length*2, length)
                a4 = dAc(s1+length, s2, length)
                a5 = dAc(s1+length, s2+length, length)
                a6 = dAc(s1+length, s2+length*2, length)
                a7 = dAc(s1+length*2, s2, length)
                a8 = dAc(s1+length*2, s2+length, length)
                a9 = dAc(s1+length*2, s2+length*2, length)

                return [a1[0]+a2[0]+a3[0]+a4[0]+a5[0]+a6[0]+a7[0]+a8[0]+a9[0], a1[1]+a2[1]+a3[1]+a4[1]+a5[1]+a6[1]+a7[1]+a8[1]+a9[1], a1[2]+a2[2]+a3[2]+a4[2]+a5[2]+a6[2]+a7[2]+a8[2]+a9[2]]

    if num_list[s1][s2] == -1:
        return [1,0,0]

    elif num_list[s1][s2] == 0:
        return [0,1,0]

    elif num_list[s1][s2] == 1:
        return [0,0,1]

real_final = dAc(0,0, length)

for i in real_final:
    print(i)