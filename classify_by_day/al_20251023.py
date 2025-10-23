import sys
from collections import deque

P = int(sys.stdin.readline())
answer = 0
target = {}
for _ in range(P):
    num, pq = sys.stdin.readline().split()
    p, q = pq.split("/")
    target[pq] = num

dq = deque()
dq.append("1/1")
flag = False
while dq:
    cur_pq = dq.popleft()
    print(cur_pq)
    if flag != False:
        target[flag] = cur_pq
        flag = False
        answer += 1
        if answer == P:
            for t in target:
                print(target[t])
            sys.exit()
    if cur_pq in target:
        flag = cur_pq
    cur_p, cur_q = cur_pq.split("/")
    sum_pq = int(cur_p) + int(cur_q)
    dq.append(f"{cur_p}/{sum_pq}")
    dq.append(f"{sum_pq}/{cur_q}")

