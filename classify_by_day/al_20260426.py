import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))


### First Approach
# zero_idx = []
# for i in range(N):
#     if num_list[i] == 0:
#         zero_idx.append(i)
#
#
# cur = 0
# answer = 0
# for zero_idx in zero_idx:
#     if zero_idx-cur == 1:
#         answer += 3*num_list[cur]
#         num_list[cur]  = 0
#         cur = zero_idx+1
#         continue
#     elif zero_idx-cur == 2:
#         min_cri = min(num_list[cur], num_list[cur+1])
#         answer += 5*min_cri
#         num_list[cur] -= min_cri
#         num_list[cur+1] -= min_cri
#         answer += 3*max(num_list[cur], num_list[cur+1])
#         num_list[cur] = 0
#         num_list[cur+1] = 0
#         cur = zero_idx+1
#         continue
#     elif zero_idx-cur == 0:
#         cur = zero_idx+1
#         continue
#
#     for i in range(cur, zero_idx-3+1):
#         min_cri = min(num_list[i], num_list[i+1], num_list[i+2])
#         num_list[i] = num_list[i] - min_cri
#         num_list[i+1] = num_list[i+1] - min_cri
#         num_list[i+2] = num_list[i+2] - min_cri
#         answer += 7*min_cri
#         min_cri = min(num_list[i], num_list[i+1])
#         num_list[i] = num_list[i] - min_cri
#         num_list[i+1] = num_list[i+1] - min_cri
#         answer += 5*min_cri
#         answer += num_list[i]*3
#         num_list[i] = 0
#         cur = zero_idx+1
# min_cri = min(num_list[-2], num_list[-1])
# answer += 5*min_cri
# num_list[-2] -= min_cri
# num_list[-1] -= min_cri
# answer += 3*max(num_list[-2], num_list[-1])
# print(answer)

answer = 0
for i in range(N):
    if i+2 < N:
        if num_list[i+1] > num_list[i+2]:
            min_cri = min(num_list[i], num_list[i+1]-num_list[i+2])
            answer += 5*min_cri
            num_list[i] -= min_cri
            num_list[i+1] -= min_cri

        min_cri = min(num_list[i], num_list[i+1], num_list[i+2])
        answer += 7 * min_cri
        num_list[i] -= min_cri
        num_list[i + 1] -= min_cri
        num_list[i + 2] -= min_cri


    if i+1 < N:
        min_cri = min(num_list[i], num_list[i + 1])
        answer += 5 * min_cri
        num_list[i] -= min_cri
        num_list[i + 1] -= min_cri

    answer += 3*num_list[i]
    num_list[i] = 0

print(answer)


