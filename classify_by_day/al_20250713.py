import sys
import math

X, Y, D, T = map(int, sys.stdin.readline().split())
dist = math.sqrt(X**2+Y**2)
cur = dist

answer = 0
flag = False
while cur > 0:
    if cur <= D:
        if flag:
            answer = answer + min(T, cur)
        else:
            answer = answer + min(2*T, cur, D-cur+T)
        cur = 0
    elif cur > D:
        if cur <= T:
            answer = answer + cur
            cur = 0
        elif cur > T:
            answer += T
            cur -= D
            flag = True

print(min(answer, dist))

explain = """
상황에 따라 분기문이 많은 문제. 점프 거리보다 현재 남은 거리가 적을때와 클 때를 기준으로
나누어지고 현재 남은거리가 크더라도 걸어서 가는 것이 점프하는 것보다 빠른 경우에 대한 분기
도 있다. 또한 현재 남은 거리가 점프 거리보다 작을 때, 이미 점프를 한번 한 경우와
처음 점프하는 경우가 나뉘고 처음 점프한 경우에 점프 점프해서 가능 경우와 걸어서 가는경우
점프 후 걸어서 가는 경우를 비교해줘야 한다.
"""