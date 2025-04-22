import sys
from collections import deque
import math
T = int(sys.stdin.readline())

cnt = 0
for _ in range(T):
    s_n , e_n = map(int, sys.stdin.readline().split())
    s = deque([[s_n, ""]])
    record = {s_n:True}
    answer = ""
    while True:
        t, cmd = s.popleft()
        if t == e_n:
            answer = cmd
            break
        for i in range(4):
            if i == 0:
                cur_t = (t*2)%10000
                c_cmd = "D"
            elif i == 1:
                cur_t = t-1 if t!= 0 else 9999
                c_cmd = "S"
            elif i == 2:
                cur_t = (t%1000)*10 + (t//1000)
                c_cmd = "L"
            elif i == 3:
                cur_t = (t%10)*1000 + (t//10)
                c_cmd = "R"

            if cur_t not in record:
                s.append([cur_t, cmd + c_cmd])
                record[cur_t] = True

    print(answer)