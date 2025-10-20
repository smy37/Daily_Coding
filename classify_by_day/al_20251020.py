import sys
from collections import deque

N, S, P = map(int, sys.stdin.readline().split())

tree = {}
for _ in range(N-1):
    s, t = map(int, sys.stdin.readline().split())

    if s not in tree:
        tree[s] = {}
    if t not in tree:
        tree[t] = {}

    tree[s][t] = True
    tree[t][s] = True


### First Approach
# dq = deque()
# dq.append([P])
# visit = {P: True}
# support = {i+1 : True for i in range(S)}
# rest_candidate = []

# while dq:
#     cur = dq.popleft()
#     cur_node = cur[-1]

#     for next_node in tree[cur_node]:
#         if next_node in support:
#             rest_candidate.append(set(cur+[next_node]))
#         else:
#             if next_node not in visit:
#                 visit[next_node] = True
#                 dq.append(cur+[next_node])

# answer = float("inf")
# for i in range(len(rest_candidate)):
#     for j in range(i+1, len(rest_candidate)):
#         answer = min(answer, len(rest_candidate[i]|rest_candidate[j]))

# print(N-answer)


### Second Approach
dq = deque()
dq.append([P, 0])
visit = {P: True}
support = {i+1 : True for i in range(S)}
candidate = []
while dq:
    cur_node, dist = dq.popleft()

    for next_node in tree[cur_node]:
        if next_node in support:
            candidate.append(dist + 1)
        else:
            if next_node not in visit:
                visit[next_node] = True
                dq.append([next_node, dist+1])
candidate.sort()
print(N-(candidate[0]+candidate[1]+1))

explain = """
처음에는 지지대로까지 가는 경로를 BFS로 찾으면서 기록해두었다가 마지막에
각 경로를 합집합해서 그 크기가 가장 적은 2개를 더함으로써 개수를 구하였다.
그러나 이는 시간초과를 발생하였고 지지대까지 가는 경로에서 서로 겹치는 얼음은
없다는 조건때문에 BFS로 각 지지대까지의 길이만 기록해두었다가 최소값 2개를 더하면
되는 식으로 해결 가능하였다.
"""