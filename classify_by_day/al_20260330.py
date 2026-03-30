import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
cri = 100000
flag = False
answer = abs(N-K)
cnt = 0

dq = deque()
dq.append([N, 0])

while dq:
    cur_location, t = dq.popleft()
    if cur_location == K and answer >= t:
        flag = True
        answer = t
        cnt += 1

    if t > answer:
        break
    if not flag:
        if cur_location*2 <= cri:
            dq.append([cur_location*2, t+1])
        if cur_location +1 <= cri:
            dq.append([cur_location +1, t + 1])
        if cur_location -1 <= cri:
            dq.append([cur_location - 1, t + 1])

print(answer)
print(cnt)