# import sys
#
# M = int(sys.stdin.readline())
#
# start_word = {}
# end_word = {}
# word_list = []
#
# for _ in range(M):
#     word = sys.stdin.readline().strip()
#     word_list.append(word)
#
#     if word[0] not in start_word:
#         start_word[word[0]] = []
#     start_word[word[0]].append(word)
#
#     if word[-1] not in end_word:
#         end_word[word[-1]] = []
#     end_word[word[-1]].append(word)
#
#
#
# ## First Approach
# # final_word = {}
# # for e in end_word:
# #     if e not in start_word:
# #         for word in end_word[e]:
# #             final_word[word[0]] = word
# # answer_list = []
# # answer = {}
# # def dfs(cur_word, cur_idx, visit):
# #     if cur_word in answer:
# #         if cur_idx%2 == 0:
# #             return 0
# #         else:
# #             return 1
# #     if cur_word[-1] not in start_word:
# #         if cur_idx%2 == 0:
# #             return 0
# #         else:
# #             return 1
# #     for next_word in start_word[cur_word[-1]]:
# #         if next_word[0] in final_word:
# #             if (cur_idx+1)%2 == 0:
# #                 return 0
# #             else:
# #                 return 1
# #     record = {}
# #     for next_word in start_word[cur_word[-1]]:
# #         if next_word[0] == next_word[-1]:
# #             record[2] = True
# #             continue
# #         if next_word not in visit:
# #             visit[next_word] = True
# #             r = dfs(next_word, cur_idx+1, visit)
# #             record[r] = True
# #     print(cur_word, record)
# #     if cur_idx % 2 == 0:
# #         if 0 in record and 1 in record:
# #             return 2
# #         elif 0 in record:
# #             return 0
# #         elif 2 in record:
# #             return 2
# #         else:
# #             return 1
# #     else:
# #         if 0 in record and 1 in record:
# #             return 2
# #         elif 1 in record:
# #             return 1
# #         elif 2 in record:
# #             return 2
# #         else:
# #             return 0
# #
# #
# #
# # for word in word_list:
# #     if word[0] == word[-1]:
# #         continue
# #     visit = {}
# #     flag = dfs(word, 0, visit)
# #     if flag == 0:
# #         answer[word] = 1
# #
# # print(len(answer))
# # for k in answer:
# #     print(k)
#
#
# ## Second Approach
# answer = {}
# memory = {}
#
# final_word = {}
# for e in end_word:
#     if e not in start_word:
#         for word in end_word[e]:
#             final_word[word] = True
#
# def dfs(cur_word, cur_idx, visit):
#     if cur_word in final_word:
#         if cur_idx %2 == 0:
#             return 0
#         else:
#             return 1
#
#     record = {}
#     for next_word in start_word[cur_word[-1]]:
#         if next_word in visit:
#             record[2] = True
#             continue
#         elif next_word not in visit:
#             visit[next_word] = True
#             r = dfs(next_word, cur_idx +1, visit)
#             del visit[next_word]
#             record[r] = True
#
#     if not record:
#         return 2
#     if cur_idx%2 == 0:
#         if 1 in record:
#             return 1
#         elif 2 in record:
#             return 2
#         elif 0 in record:
#             return 0
#     else:
#         if 0 in record:
#             return 0
#         elif 2 in record:
#             return 2
#         elif 1 in record:
#             return 1
#
# for word in word_list:
#     r = dfs(word, 0, {word: True})
#     if r == 0:
#         answer[word] = True
#
# print(len(answer))
# for k in answer:
#     print(k)


## Third Approach
# import sys
#
# M = int(sys.stdin.readline())
#
# ori_word_list = []
# state = {}
# start_word_l = {}
# end_word_l = {}
# for _ in range(M):
#     cur_str = sys.stdin.readline().strip()
#     s, e = cur_str[0], cur_str[-1]
#
#     if s not in start_word_l:
#         start_word_l[s] = []
#     start_word_l[s].append(e)
#
#     if e not in end_word_l:
#         end_word_l[e] = []
#     end_word_l[e].append(s)
#     state[s+e] = -1
#     ori_word_list.append(cur_str)
#
# fin_word = {}
# for e in end_word_l:
#     if e not in start_word_l:
#         for s in end_word_l[e]:
#             fin_word[s+e] = True
#
#
# def dfs(cur_str, visit):
#     if cur_str in fin_word:
#         return 1
#
#     # if state[cur_str] != -1:
#     #     return state[cur_str]
#
#     s, e = cur_str[0], cur_str[-1]
#
#     record = {}
#     for next_e in start_word_l[e]:
#         temp_str = e+next_e
#         if temp_str not in visit:
#             visit[temp_str] = True
#             r = dfs(temp_str, visit)
#             del visit[temp_str]
#             record[r] = True
#         else:
#             record[2] = True
#     if not record:
#         record[2] = True
#
#     if 1 in record:
#         state[cur_str] = 0
#         return 0
#     elif 2 in record:
#         state[cur_str] = 2
#         return 2
#     else:
#         state[cur_str] = 1
#         return 1
#
#
# for se in state:
#     r = dfs(se, {})
#     state[se] = r
#
# answer_l = []
# for word in ori_word_list:
#     s, e = word[0], word[-1]
#     if state[s+e] == 1:
#         answer_l.append(word)
# print(len(answer_l))
# for k in answer_l:
#     print(k)


## Final Approach
import sys
from collections import deque

input = sys.stdin.readline

M = int(input().strip())
graph = [[] for _ in range(26)]
rev = [[] for _ in range(26)]
outdeg = [0] * 26

words = []

for _ in range(M):
    w = input().strip()
    s = ord(w[0]) - ord('a')
    e = ord(w[-1]) - ord('a')
    words.append((w, s, e))

    graph[s].append(e)
    rev[e].append(s)
    outdeg[s] += 1
state = [-1] * 26

lose_count = [0] * 26

q = deque()

for i in range(26):
    if outdeg[i] == 0:
        state[i] = 0
        q.append(i)
while q:
    cur = q.popleft()

    for prev in rev[cur]:
        if state[prev] != -1:
            continue

        if state[cur] == 0:
            state[prev] = 1
            q.append(prev)
        elif state[cur] == 1:
            lose_count[prev] += 1
            if lose_count[prev] == outdeg[prev]:
                state[prev] = 0
                q.append(prev)

answer = []
for w, s, e in words:
    if state[e] == 0:
        answer.append(w)

print(len(answer))
for w in answer:
    print(w)