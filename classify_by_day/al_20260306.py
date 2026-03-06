import sys
from collections import deque

s, t = map(int, sys.stdin.readline().split())

if s == t:
    print(0)
    sys.exit()

cal_list = ["*", "+", "-", "/"]
cal_list.sort()

dq = deque()
dq.append([s, ""])
visited = {s:1}

while dq:
    cur_s, accumul_cal = dq.popleft()

    for cal in cal_list:
        next_value = int(eval(f"{cur_s}{cal}{cur_s}"))
        if next_value == t:
            print(accumul_cal+cal)
            sys.exit()
        if next_value not in visited:
            visited[next_value] = 1
            if next_value != 0 and next_value <= t:
                dq.append([next_value, accumul_cal+cal])
print(-1)
