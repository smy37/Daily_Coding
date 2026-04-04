import sys 

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))


### Fisrt Approach
# answer = 0
# for i in range(N):
#     idx = i
#     cur = 0
#     while 1:
#         cur += num_list[idx]
#         if cur == 50:
#             answer += 1
#             break
#         elif cur > 50:
#             break
#         idx += 1
#         if idx >= N:
#             idx -= N
#
# print(answer//2)


### Second Approach
# answer = 0
# num_list.sort()
# cur_val = 0
# def dfs(accum_val, cur_idx):
#     global answer
#     if accum_val == 50:
#         answer +=1
#         return
#     elif accum_val > 50:
#         return
#     else:
#         if cur_idx >= N:
#             return
#         dfs(accum_val, cur_idx +1)
#         dfs(accum_val+num_list[cur_idx], cur_idx+1)
#
# dfs(cur_val, 0)
# print(answer//2)


### Third Approach
from itertools import permutations

def check_half(n_l):
    cnt = 0
    for i in range(N):
        cur = n_l[i]
        if cur == 50:
            cnt +=1
            continue
        elif cur > 50:
            continue
        else:
            idx = i+1
            while 1:
                if idx == N:
                    idx = 0
                cur += n_l[idx]
                if cur == 50:
                    cnt += 1
                    break
                elif cur > 50:
                    break
                idx += 1
    return cnt

final_answer = 0
for iter in permutations(num_list):
    final_answer = max(final_answer, check_half(iter))


print(final_answer//2)