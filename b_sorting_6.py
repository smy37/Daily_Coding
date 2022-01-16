import sys

iter = int(sys.stdin.readline())

num_list = []
for i in range(iter):

    num_list.append(list(map(int, sys.stdin.readline().strip().split(' '))))

temp = sorted(num_list, key = lambda x: (x[0], x[1]))

for i in temp:
    print(i[0], i[1])