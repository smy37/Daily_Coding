import sys

num_length = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().rstrip().split()))

if len(num_list) == 1:
    print(1)
    sys.exit()



result_list = {}
for i in range(num_length):
    result_list[i+1] = []


result_list[1].append(num_list[0])

cur = 1
for i in range(1,num_length-1):
    if num_list[i] > result_list[cur][0]:
        result_list[cur+1].append(num_list[i])
        cur+=1
    for j in range(cur):
        if j!= 0:
            if num_list[i] < result_list[j+1][0] and num_list[i] > result_list[j][0]:
                result_list[j+1][0] = num_list[i]
        elif j == 0:
            if num_list[i] < result_list[1][0]:
                result_list[1][0] = num_list[i]


if result_list[cur][0] < num_list[-1]:
    cur+=1

print(cur)
