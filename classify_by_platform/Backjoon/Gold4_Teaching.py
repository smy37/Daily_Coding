import sys
import re
from itertools import combinations

N, K = map(int, sys.stdin.readline().split())

if K < 5:
    print(0)
    sys.exit()
part_set = []
total_set = set()
answer = 0

for i in range(N):
    t = sys.stdin.readline()
    tt = set(re.sub("[tanic]", "", t).strip())
    if len(tt) == 0:
        answer += 1
    else:
        total_set = total_set.union(tt)
        ttt = {}
        for j in tt:
            ttt[ord(j)] = 1
        part_set.append(ttt)

if K-5 >= len(total_set):
    print(N)
    sys.exit()

temp_ans = 0
for i in combinations(total_set, K-5):
    t_ord = {}
    temp = 0
    for j in i:
        t_ord[ord(j)] =1
    for j in part_set:
        for k in j:
            if k not in t_ord:
                break
        else:
            temp +=1
    temp_ans = max(temp_ans, temp)

answer += temp_ans
print(answer)


# Mehtod 2. Using 비트연산...
# import sys
# import re
# from itertools import combinations
#
# N, K = map(int, sys.stdin.readline().split())
#
# ord_set = []
# if K < 5:
#     print(0)
# else:
#     word_masks = []
#     for _ in range(N):
#         word = sys.stdin.readline().strip()
#         mask = 0
#         for char in set(word) - {'a', 'n', 't', 'i', 'c'}:
#             mask |= (1 << (ord(char) - ord('a')))
#             ord_set.append(ord(char) - ord('a'))
#         word_masks.append(mask)
#
#     answer = 0
#     ord_set = set(ord_set)
#     if K-5 >= len(ord_set):
#         answer = N
#     else:
#         for comb in combinations(ord_set, K-5):
#             comb_mask = 0
#             for i in comb:
#                 comb_mask |= (1 << i)
#             temp_ans = sum(1 for word_mask in word_masks if word_mask & comb_mask == word_mask)
#             answer = max(answer, temp_ans)
#
#     print(answer)