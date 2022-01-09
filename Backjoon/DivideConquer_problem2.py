import sys

start = int(sys.stdin.readline())

num_list = []
for i in range(start):
    temp = list(map(int, sys.stdin.readline().strip()))
    num_list.append(temp)

final = ''


def dAc(s1, s2, length, final):

    for i in range(length):
        for j in range(length):
            if num_list[s1][s2] != num_list[s1+i][s2+j]:
                t_length = length//2
                t1 = dAc(s1, s2, t_length, final)
                t2 = dAc(s1, s2 + t_length, t_length, final)
                t3 = dAc(s1+t_length, s2, t_length, final)
                t4 = dAc(s1 + t_length, s2 + t_length, t_length, final)
                real_temp = t1 + t2 + t3 + t4
                return f'({real_temp})'

    if num_list[s1][s2] == 1:
        return '1'

    elif num_list[s1][s2] == 0:
        return '0'
    return final

print(dAc(0, 0, start, final))