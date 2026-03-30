import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
flag = False
answer = abs(N-K)

dq = deque()
dq.append([N, 0])
visit = {N: 0}
cnt = {N: 1}
if N == K:
    print(0)
    print(1)
    sys.exit()
while dq:
    cur_location, t = dq.popleft()

    for i in range(3):
        if i == 0:
            next_location = cur_location*2
        elif i == 1:
            next_location = cur_location+1
        else:
            next_location = cur_location-1

        if next_location == K and t+1 <= answer:
            flag = True
            answer = t+1

        if next_location not in visit:
            visit[next_location] = t+1
            cnt[next_location] = 0

            if not flag and (next_location >=0 and next_location <= 100000):
                dq.append([next_location, t+1])

        if t+1 == visit[next_location]:
            cnt[next_location] += cnt[cur_location]

print(answer)
print(cnt[K])
