import sys

iter_num = int(sys.stdin.readline())

for i in range(iter_num):
    temp = list(map(int, sys.stdin.readline().split()))
    max_num, min_num = max(temp), min(temp)
    while True:
        if max_num % min_num ==0 :
            print(int(temp[0]*temp[1]/min_num))
            break
        else:
            temp_2 = int(max_num)
            max_num = min_num
            min_num = temp_2 % min_num