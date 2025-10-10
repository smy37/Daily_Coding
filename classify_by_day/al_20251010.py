import sys

N = int(sys.stdin.readline())

graph = {}

for i in range(N):
    graph[i+1] = int(sys.stdin.readline())

### Method 1. 표에서 위의 값들을 담는 딕셔너리 한개와 아래 값들을 담는 스택 한개 사용 (정답 코드임)
# answer = {}
#
# for i in range(N):
#     if i + 1 not in answer:
#         temp = {i+1 : False}
#         s = [graph[i+1]]
#
#         while s:
#             t = s.pop()
#             temp[t] = True
#             if t not in temp:
#                 s.append(graph[t])
#         for t in temp:
#             if temp[t] == False:
#                 break
#         else:
#             for t in temp:
#                 answer[t] = True
#
# print(len(answer))
# answer_l = sorted(answer.keys())
# for i in answer_l:
#     print(i)
