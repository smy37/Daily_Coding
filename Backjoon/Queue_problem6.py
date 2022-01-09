import sys

temp = list(map(int, sys.stdin.readline().strip().split()))

num_list = [i+1 for i in range(temp[0])]

ans_list = list(map(int, sys.stdin.readline().strip().split()))

total = 0


for i in ans_list:
    temp_idx = num_list.index(i)
    if temp_idx > len(num_list)-temp_idx:
        total += len(num_list)-temp_idx
        num_list = list(reversed(num_list[-1:temp_idx:-1])) + num_list[:temp_idx]

    elif temp_idx <= len(num_list)-temp_idx:
        total += temp_idx
        num_list = num_list[temp_idx+1:] + num_list[:temp_idx]

print(total)

