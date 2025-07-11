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

explain = """
시작 숫자에서 타겟 숫자까지, 연산자에 대해서 BFS를 수행함으로써 도달하는지 탐색하면 된다. 
다만, 시작 숫자가 중간 숫자로 변환될 때 목표 숫자보다 커지는 순간에 대한 처리와 중간 숫자가
0이 될때의 처리에 유의해야 한다.
"""