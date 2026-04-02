import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
S = int(sys.stdin.readline())

## 1. First Approach
# cnt = 0
# while cnt < S:
#     flag = True
#     for i in range(N):
#         for j in range(N-i-1):
#             if num_list[j] < num_list[j+1]:
#                 cnt += 1
#                 memory = num_list[j+1]
#                 num_list[j+1] = num_list[j]
#                 num_list[j] = memory
#                 flag = False
#                 break
#         if not flag:
#             break
#     if flag:
#         cnt += 1


## 2. Second Approach
cnt = 0
start = 0
while cnt < S and start < N:

    max_value = max(num_list[start:start+(S-cnt)+1])
    max_index = num_list.index(max_value)

    if max_index == start:
        start += 1
        continue
    for i in range(max_index, start, -1):
        memory = num_list[i]
        num_list[i] = num_list[i-1]
        num_list[i-1] = memory
    cnt += (max_index-start)
    start += 1

for n in num_list:
    print(n, end = " ")

