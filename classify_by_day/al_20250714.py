import sys
import heapq

N = int(sys.stdin.readline())

conf_list = []
for _ in range(N):
    s, t = map(int, sys.stdin.readline().split())
    conf_list.append([s, t])

conf_list.sort(key = lambda x : [x[0], x[1]])
answer = 0

### First Approach - Using Stack
# stack = []
# for i in range(len(conf_list)):
#     s, t = conf_list[i]
#
#     if len(stack) == 0:
#         stack.append(t)
#     else:
#         while stack and stack[-1] <= s:
#             stack.pop()
#         stack.append(t)
#
#     answer = max(answer, len(stack))
#
# print(answer)

### Second Approach - Using Heap
hq = []
heapq.heapify(hq)
for i in range(len(conf_list)):
    s, t = conf_list[i]

    while hq and hq[0] <= s:
        heapq.heappop(hq)
    heapq.heappush(hq, t)
    answer = max(answer, len(hq))

print(answer)

explain = """
얼마전에 비슷한 문제를 풀었었는데 예전에 풀었던 스택을 이용하는 문제와, 
혼동하여 처음에 stack을 이용하는 방법으로 접근하였다. stack인 경우에는
중간에 현재 쌓여있는 것보다 빨리 끝나는 작업에 대한 처리가 불가하다.
따라서 최소힙을 이용하였고 현재 시간보다 작거나 같은 원소들을 제거해주는 로직으로 작성하였다
"""