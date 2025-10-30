import sys 
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
dq = deque()
dq.append([S, 0])
visited = {}
flag = False
while dq:
    cur_s, cnt = dq.popleft()

    if cur_s == G:
        flag = True
        break
    
    if cur_s + U <= F and cur_s + U not in visited:
        visited[cur_s+U] = True
        dq.append([cur_s+U, cnt+1])
    if cur_s - D <= 1 and cur_s - D not in visited:
        visited[cur_s-D] = True
        dq.append([cur_s-D, cnt+1])


if flag:
    print(cnt)
else:
    print("use the stairs")

explain = """
BFS를 이용해서 위로 가는 경우와 아래로 가는 경우를 큐에 추가해준다.
"""