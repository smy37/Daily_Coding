import sys

N = int(sys.stdin.readline())

num_l = list(map(int, sys.stdin.readline().split()))
answer = 0
num_dict = {}
num_check = {}

for i in num_l:
    if i not in num_dict:
        num_dict[i] = 1
        num_check[i] = False
    else:
        num_dict[i] += 1
flag = True
for i in range(N):
    for j in range(i+1, N):
        sum_n = num_l[i] + num_l[j]
        if sum_n in num_dict and num_check[sum_n] == False:
            if num_l[i] == 0 and num_dict[sum_n] < 2:
                continue
            if num_l[j] == 0 and num_dict[sum_n] < 2:
                continue
            if sum_n == 0 and num_l[i]!=0 and num_l[j]!= 0:
                flag = False
            answer += num_dict[sum_n]
            num_check[sum_n] = True

if 0 in num_dict and num_dict[0] == 2 and flag:
    answer -=2

