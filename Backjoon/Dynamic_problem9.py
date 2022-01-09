import sys

num_length = int(sys.stdin.readline())

temp_1 = {}

for i in range(10):
    temp_1[i] = 0

for i in range(1, 10):
    temp_1[i] = 1

for i in range(num_length-1):
    real_temp = {}
    for j in range(10):
        real_temp[j] = 0
    for k,v in temp_1.items():
        if k == 0:
            real_temp[1] += v
        elif k == 9:
            real_temp[8] += v
        else:
            real_temp[k+1] += v
            real_temp[k-1] += v
    temp_1 = real_temp

print(sum(temp_1.values())%1000000000)