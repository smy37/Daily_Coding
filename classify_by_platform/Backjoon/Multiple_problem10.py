import sys
from itertools import combinations


total_num = int(sys.stdin.readline())

def recursion(num_list, genome):
    if len(genome) == len(num_list):
        temp = 1
        for k,v in enumerate(genome):
            if v == '0':
                temp *= 1
            else:
                temp *= num_list[k]
        return temp
    else:
        return recursion(num_list, genome+'0') + recursion(num_list, genome+'1')


for i in range(total_num):
    cloth_list = {}
    cloth_num = int(sys.stdin.readline())
    for j in range(cloth_num):
        temp_cloth = list(sys.stdin.readline().rstrip().split())
        if temp_cloth[1] not in cloth_list:
            cloth_list[temp_cloth[1]] = 1
        else:
            cloth_list[temp_cloth[1]] += 1

    temp = list(cloth_list.values())
    final = 1

    for k in temp:
        final*=(k+1)
    print(final-1)





    #
    # del cloth_list
    #
    # binary_list = []
    # for a in range(1, 2**len(temp)):
    #     binary_list.append(bin(a)[2:])
    #
    #
    # final = 0
    # for a in binary_list:
    #     real_temp = 1
    #     for k,v in enumerate(a):
    #         if v == '0':
    #             real_temp*= 1
    #         else:
    #             real_temp*= temp[k]
    #     final+= real_temp
    #
    # print(final)