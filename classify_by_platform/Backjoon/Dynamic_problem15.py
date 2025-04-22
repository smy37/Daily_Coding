import sys

num_length = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().strip().split()))


temp = 0
max_n = -30000

if num_length == 1:
    print(num_list[0])
    sys.exit()


for i in num_list:
    temp += i
    if temp >= max_n:
        max_n = temp
        if temp < 0 :
            temp = 0
    elif temp < max_n and temp <=0:
        temp = 0

print(max_n)