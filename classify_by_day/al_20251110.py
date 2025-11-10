import sys
from collections import deque

T = int(sys.stdin.readline())
num_l = []
for _ in range(T):
    num_l.append(int(sys.stdin.readline()))

num_l.sort()
num_d = {i: [] for i in num_l}

dq = deque()
dq.append([num_l[0]])

# while dq:
#     cur = dq.popleft()
#
#     if
