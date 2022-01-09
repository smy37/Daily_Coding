import sys


iter_num = int(sys.stdin.readline())


for i in range(iter_num):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))

    result = 1
    for j in range(temp[0]):
        result = result*(temp[1]-j)/(temp[0]-j)

    print(round(result))