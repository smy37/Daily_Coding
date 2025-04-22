import sys

num = int(sys.stdin.readline())

num_list =[]

for i in range(num):
    num_list.append(list(map(int, sys.stdin.readline().strip().split(' '))))

num_list =sorted(num_list, key = lambda x : (x[1], x[0]))

for i in num_list:
    print(i[0], i[1])