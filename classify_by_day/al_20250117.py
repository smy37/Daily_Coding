import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())

snake = {}
ladder = {}
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    ladder[s] = e

for _ in range(K):
    s, e = map(int, sys.stdin.readline().split())
    snake[s] = e


s = deque([[1,0]])
visited = {1: 1}
while s:
    t = s.popleft()
    cur, num = t[0], t[1]
    if cur == 100:
        print(num)
        sys.exit()
    for i in range(1, 7):
        next_loc = cur + i
        if next_loc in ladder:
            next_loc = ladder[next_loc]
        elif next_loc in snake:
            next_loc = snake[next_loc]
        if next_loc not in visited:
            visited[next_loc] = 1
            s.append([next_loc, num+1])

