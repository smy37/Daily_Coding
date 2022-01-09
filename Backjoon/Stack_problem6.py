import sys

iter_num = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

result = [-1]*iter_num

stack = []

stack.append(0)

cri = 1

for i in range(1,iter_num):
    for j in range(len(stack)-1, -1, -1):
        if num_list[stack[j]] < num_list[i]:
            result[stack[j]] = num_list[i]
            stack.pop()
        else:
            break
    stack.append(i)


for i in result:
    print(i, end=' ')