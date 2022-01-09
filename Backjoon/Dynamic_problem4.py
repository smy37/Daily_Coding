import sys

def pivoN(n):
    if n <=5 :
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n == 3:
            return 1
        elif n == 4:
            return 2
        elif n == 5:
            return 2
    else:
        start = [1,1,1,2,2]
        for i in range(5,n):
            start.append(start[i-1]+start[i-5])
        return start[-1]

iter_num = int(sys.stdin.readline())

for i in range(iter_num):
    num = int(sys.stdin.readline())
    print(pivoN(num))