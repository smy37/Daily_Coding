import sys

ali_num = int(sys.stdin.readline())

if ali_num%2 == 0:
    temp = list(sorted(map(int, sys.stdin.readline().split())))
    print(temp[0]*temp[-1])
elif ali_num%2 != 0:
    temp = list(sorted(map(int, sys.stdin.readline().split())))
    if len(temp) == 1:
        print(temp[0]**2)
    else:
        print(temp[0]*temp[-1])