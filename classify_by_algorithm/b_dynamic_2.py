import sys
import collections
dd = collections.defaultdict(int)


def function(num_list,diction):

    if tuple(num_list) in diction:
        return dd[tuple(num_list)]
    if num_list[0] <= 0 or num_list[1] <= 0 or num_list[2] <=0:
        diction[tuple(num_list)] = 1
        return 1
    if num_list[0] > 20 or num_list[1] > 20 or num_list[2] > 20:
        return function([20,20,20], diction)
    if num_list[0] <num_list[1] and num_list[1]<num_list[2]:
        temp = function([num_list[0], num_list[1], num_list[2]-1], diction) + function([num_list[0], num_list[1]-1, num_list[2]-1], diction) - function([num_list[0], num_list[1]-1, num_list[2]], diction)
        diction[tuple(num_list)] = temp
        return temp
    else:
        temp = function([num_list[0]-1, num_list[1], num_list[2]], diction) + function([num_list[0]-1, num_list[1]-1, num_list[2]], diction) + function([num_list[0]-1, num_list[1], num_list[2]-1], diction)-function([num_list[0]-1, num_list[1]-1, num_list[2]-1],diction)
        diction[tuple(num_list)] = temp
        return temp

while True:

    temp = list(map(int, sys.stdin.readline().split(' ')))
    source = f'w({temp[0]}, {temp[1]}, {temp[2]})'
    if temp[0] == -1 and temp[1] == -1 and temp[2] == -1:
        break

    tt = function(temp, dd)
    print(source + f' = {tt}')

