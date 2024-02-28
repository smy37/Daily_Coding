import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
board = [-1 for _ in range(100001)]
dq = deque()
dq.append(N)
board[N] = 0

dx1 = [1, 1, 2]
dx2 = [1, -1, 0]

while dq:
    cur_idx = dq.popleft()
    if cur_idx == K:
        print(board[cur_idx])
        sys.exit()
    for i in range(3):
        next_idx = cur_idx*dx1[i]+dx2[i]
        if 0<=next_idx<100001 and board[next_idx] == -1:
            board[next_idx] = board[cur_idx] +1
            dq.append(next_idx)