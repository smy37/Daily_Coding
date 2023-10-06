import sys
import math
N, cri = map(int, sys.stdin.readline().split())
num_l = list(map(int, sys.stdin.readline().split()))
s,e, p_sum = 0, 0, 0

answer = math.inf
flag = False
while s < N:
    if s == e:
        e+=1
        p_sum += num_l[e-1]
    if p_sum >= cri:
        answer = min(e-s, answer)
        flag = True
        s+=1
        p_sum -= num_l[s-1]
    else:
        if e < N:
            e+=1
            p_sum += num_l[e-1]
        else:
            s+=1
            p_sum -= num_l[s-1]

if flag:
    print(answer)
else:
    print(0)