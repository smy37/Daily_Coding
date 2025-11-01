import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

if x3 > x2 or x4 < x1 or y3 > y2 or y4 < y1:
    print("NULL")
elif x3 == x2:
    if y3 == y2 or y4 == y1:
        print("POINT")
    else:
        print("LINE")
elif x4 == x1:
    if y4 == y1 or y3 == y2:
        print("POINT")
    else:
        print("LINE")
elif y3 == y2:
    if x3 == x2 or x4 == x1:
        print("POINT")
    else:
        print("LINE")
elif y4 == y1:
    if x4 == x1 or x3 == x2:
        print("POINT")
    else:
        print("LINE")
else:
    print("FACE")

explain = """
사각형 하나를 고정해두고 다른 사각형을 움직이며 조건을 수립하는 것이 핵심.
"""