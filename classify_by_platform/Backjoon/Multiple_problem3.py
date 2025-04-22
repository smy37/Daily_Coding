import sys

temp = list(map(int, sys.stdin.readline().split()))
min_num = min(temp)
max_num = max(temp)

if max_num % min_num == 0:
    print(min_num)
    print(max_num)
else:
    for i in range(min_num-1, 0, -1):
        if max_num % i ==0 and min_num % i ==0:
            print(i)
            break
    cnt = 2
    while True:
        real = max_num* cnt
        if real % min_num == 0:
            print(real)
            break
        cnt+=1