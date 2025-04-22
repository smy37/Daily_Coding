import sys

iter = int(sys.stdin.readline())

man_list = []

for i in range(iter):
    man_list.append(list(map(int, sys.stdin.readline().split(' '))))


for i in range(len(man_list)):
    temp = 0
    for j in range(len(man_list)):
        if man_list[i][0] < man_list[j][0] and man_list[i][1] < man_list[j][1]:
            temp +=1
    print(temp+1, end = ' ')