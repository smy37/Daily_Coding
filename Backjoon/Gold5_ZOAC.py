import sys
from collections import deque

input_str = sys.stdin.readline().strip()
num_l = {}
for i in range(len(input_str)):
    if input_str[i] not in num_l:
        num_l[input_str[i]] = []
    num_l[input_str[i]].append(i)

answer = ""

cur_idx = [-1]
temp = []

while num_l:
    for k in sorted(num_l.keys()):
        for j in range(len(num_l[k])):
            if num_l[k][j] > cur_idx[-1]:
                cur_idx.append(num_l[k][j])
                answer += k
                temp.append([k, num_l[k][j]])
                temp = sorted(temp, key=lambda x: x[1])
                print("".join([t[0] for t in temp]))
                del num_l[k][j]
                if len(num_l[k]) == 0:
                    del num_l[k]
                break
        else:
            continue
        break
    else:
        cur_idx.pop()
#
# while num_l:
#     for k in sorted(num_l.keys()):
#         for idx in num_l[k]:
#             if idx > cur_idx[-1]:
#                 cur_idx.append(idx)
#                 answer += k
#                 temp.append([k, idx])
#                 temp = sorted(temp, key=lambda x: x[1])
#                 print("".join([t[0] for t in temp]))
#                 num_l[k].remove(idx)  # 안전하게 remove
#                 if len(num_l[k]) == 0:
#                     del num_l[k]
#                 break
#         else:
#             continue
#         break
#     else:
#         cur_idx.pop()
