import sys
from collections import deque

answer = 0

N = int(sys.stdin.readline())
length = 3*N
drug_status = sys.stdin.readline().strip()

### First Approach
# def bfs(cur):
#     global answer
#     dq = deque()
#     dq.append(["B", cur])
#
#     while dq:
#         t, cur = dq.popleft()
#         answer = max(answer, length - len(cur))
#         if len(cur) == 0:
#             break
#         if t == "B":
#             if cur[0] == "L":
#                 dq.append(["L", cur[1:]])
#             if cur[-1] == "L":
#                 dq.append(["L", cur[:-1]])
#         elif t == "L":
#             if cur[0] == "D":
#                 dq.append(["D", cur[1:]])
#             if cur[-1] == "D":
#                 dq.append(["D", cur[:-1]])
#         elif t == "D":
#             if cur[0] == "B":
#                 dq.append(["B", cur[1:]])
#             if cur[-1] == "B":
#                 dq.append(["B", cur[:-1]])
#
# if drug_status[0] == "B":
#     cur = drug_status[1:]
#     bfs(cur)
#
# if drug_status[-1] == "B" and answer < length:
#     cur = drug_status[:-1]
#     bfs(cur)
#
# print(answer)


### Second Approach
order = "BLD"
def bfs():
    global answer
    dq = deque()
    visit = {}
    if drug_status[0] == "B":
        dq.append([1, length-1])
        answer = 1
        visit[(1, length-1)] = 1
    if drug_status[-1] == "B":
        dq.append([0, length-2])
        answer = 1
        visit[(0, length - 2)] = 1
    while dq:
        s, e = dq.popleft()
        if s > e:
            break
        order_idx = (length-(e-s+1))%3

        if drug_status[s] == order[order_idx]:
            dq.append([s+1, e])
            answer = max(answer, length-(e-s))
            visit[(s+1, e)] = 1
        if drug_status[e] == order[order_idx]:
            dq.append([s, e-1])
            answer = max(answer, length - (e - s))
            visit[(s, e-1)] = 1
bfs()
print(answer)

explain = """
첫번째 시도에서 남은 문자열을 queue에 넘겨 해당 부분부터 앞 또는 뒤라는 갈래로 그래프(여기서는 트리)를 전개하였다.
그러나 시간초과가 발생하여 앞-뒤 인덱스를 넘기는 방법으로 바꾸고 앞-뒤 인덱스를 키로 하는 딕셔너리를 만들어서 
이전에 계산한 적이 있다면 queue에 추가하지 않도록 하였다.
그리고 하나 주의해야 할점은, 처음 queue에 앞-뒤 인덱스를 넣어줄 때, answer 값을 갱신해야 한다.
"""