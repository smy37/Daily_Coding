import sys
from collections import deque


N = int(sys.stdin.readline())
num_l = list(map(int, sys.stdin.readline().split()))
mod_num_l = []
num_cnt = {}

for i in range(len(num_l)):
    mod_num_l.append([num_l[i], i])
    if num_l[i] not in num_cnt:
        num_cnt[num_l[i]] = 0
    num_cnt[num_l[i]] += 1

dq = deque()
answer = [-1 for _ in range(N)]

for i in range(len(mod_num_l)):
    t,idx = mod_num_l[i]
    if len(dq) == 0:
        dq.append([t, idx])
    else:
        flag = True
        while len(dq):
            if num_cnt[t] <= num_cnt[dq[-1][0]]:
                dq.append([t, idx])
                flag = False
                break
            else:
                out = dq.pop()
                answer[out[1]] = t
        if flag:
            dq.append([t,idx])
for i in answer:
    print(i, end=' ')