import sys
from collections import deque

P = int(sys.stdin.readline())
answer = 0

for i in range(P):
    num, pq = sys.stdin.readline().split()
    p, q = map(int, pq.split("/"))
    if q == 1:
        next_q = int(p)+1
        print(i+1, f"1/{next_q}")
    else:
        if int(p) > int(q):
            moc = p//q
            root_p = p-moc*q
            root_root_q = q-root_p
            ans_q = root_root_q + moc*q
            print(i+1, f"{q}/{ans_q}")
        elif int(p) < int(q):
            root_q = q-p
            print(i+1, f"{q}/{root_q}")

## First Approach
# dq = deque()
# dq.append("1/1")
# flag = False
# while dq:
#     cur_pq = dq.popleft()
#     print(cur_pq)
#     if flag != False:
#         target[flag] = cur_pq
#         flag = False
#         answer += 1
#         if answer == P:
#             for t in target:
#                 print(target[t])
#             sys.exit()
#     if cur_pq in target:
#         flag = cur_pq
#     cur_p, cur_q = cur_pq.split("/")
#     sum_pq = int(cur_p) + int(cur_q)
#     dq.append(f"{cur_p}/{sum_pq}")
#     dq.append(f"{sum_pq}/{cur_q}")

explain = """
처음에는 bfs를 이용한 시뮬레이션으로 답을 찾으려고 했지만 시간초과가 발생하였다.
두번째 접근에서는 왼쪽 노드일 경우에는 바로 이전 루트 노드를 통해 옆 노드를 구하고
오른쪽 노드일 경우에는 더이상 대각선 왼쪽으로 이동할 수 없는 루트 노드까지 이동해서
그 노드의 오른쪽 노드를 구해서 이동한 깊이만큼 q값을 갱신해줘서 답을 구했다.
"""