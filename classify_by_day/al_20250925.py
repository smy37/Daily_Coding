import sys
import math

X, Y, c = map(int, sys.stdin.readline().split())
dist = math.sqrt(X**2+Y**2)

if dist%c == 0:
    print(dist//c)
else:
    print(int(dist/c)+1)
