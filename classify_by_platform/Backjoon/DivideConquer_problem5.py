import sys

num_list = list(map(int, sys.stdin.readline().rstrip().split()))

cri = min(num_list[0]-num_list[1], num_list[1])

temp = 1
for i in range(cri):
    temp = (temp*(num_list[0]-i)/(num_list[1]-i))%1000000007

print(round(temp))