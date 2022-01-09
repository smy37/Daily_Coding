import sys
from collections import deque

max_num = int(sys.stdin.readline())


dq = deque([i for i in range(1, max_num+1)])

while len(dq) > 1:
    dq.popleft()
    temp = dq.popleft()
    dq.append(temp)

print(dq[0])