import sys
import math

X, Y, c = map(int, sys.stdin.readline().split())
dist = math.sqrt(X**2+Y**2)

if X==0 and Y == 0:
    print(0)
elif dist < c:
    print(2)
else:
    if dist%c == 0:
        print(int(dist//c))
    else:
        print(int(dist/c)+1)

explain = """
도달해야 하는 길이와 반지름을 비교하면 된다. 다만, 도달해야 하는 길이가 0일 때와
도달해야 하는 길이가 반지름보다 짧은 경우를 예외 처리 해줘야 한다.
"""