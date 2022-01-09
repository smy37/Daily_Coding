##### 시간 초과.... 실행 시간 줄이는 법은?



import sys
from collections import OrderedDict
length = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().rstrip().split()))
temp = sorted(list(OrderedDict.fromkeys(num_list)))
answer = {}
for k,v in enumerate(temp):
    answer[v] = k
for v in num_list:
    print(answer[v], end=' ')


# fin_sort = [0]*length
# left_list = []
# left_list.append(num_list[0])
#
# for i in range(1, len(num_list)):
#     temp = num_list[i]
#     cnt = 0
#     temp2 = []
#     for j in range(len(left_list)):
#         if left_list[j] > temp and temp not in left_list:
#             fin_sort[j]+=1
#         elif left_list[j] < temp and left_list[j] not in temp2:
#             cnt+=1
#             temp2.append(left_list[j])
#     left_list.append(temp)
#     fin_sort[i] = cnt
#
# for i in fin_sort:
#     print(i, end = ' ')



