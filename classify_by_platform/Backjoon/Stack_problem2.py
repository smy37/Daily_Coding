import sys

iter_num = int(sys.stdin.readline())


temp_l = []
for i in range(iter_num):
    temp = int(sys.stdin.readline())

    if temp == 0:
        temp_l.pop()
    else:
        temp_l.append(temp)

print(sum(temp_l))