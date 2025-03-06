import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())


### 첫번째 시도.
# if x1 == x2 and x3 == x4:
#     print(1)
#     sys.exit()
# elif x1 == x2:
#     m2 = (y3 - y4) / (x3 - x4)
#     c2 = -(m2 * x3) + y3
#
#     x = x1
#     y = m2*x + c2
#     x = round(x, 10)
#     y = round(y, 10)
#     if (min(x1, x2) <= x <= max(x1, x2)) and (min(x3, x4) <= x <= max(x3, x4)) and (
#             min(y1, y2) <= y <= max(y1, y2)) and (min(y3, y4) <= y <= max(y3, y4)):
#         print(1)
#     else:
#         print(0)
# elif x3 == x4:
#     m1 = (y1 - y2) / (x1 - x2)
#     c1 = -(m1 * x1) +y1
#
#     x = x3
#     y = m1 * x + c1
#     x = round(x, 10)
#     y = round(y, 10)
#     if (min(x1, x2) <= x <= max(x1, x2)) and (min(x3, x4) <= x <= max(x3, x4)) and (
#             min(y1, y2) <= y <= max(y1, y2)) and (min(y3, y4) <= y <= max(y3, y4)):
#         print(1)
#     else:
#         print(0)
# else:
#     m1 = (y1-y2)/(x1-x2)
#     m2 = (y3-y4)/(x3-x4)
#
#     c1 = -m1*x1 +y1
#     c2 = -m2*x3 + y3
#
#     if m1 == m2:
#         if c1 == c2:
#             if min(x3,x4)<=min(x1,x2)<=max(x3,x4):
#                 print(1)
#             else:
#                 print(0)
#         else:
#             print(0)
#         sys.exit()
#
#     x = (-c1+c2)/(m1-m2)
#     y = m1*x + c1
#     x = round(x, 10)
#     y = round(y, 10)
#     if (min(x1,x2) <= x <= max(x1,x2)) and (min(x3,x4) <= x <= max(x3, x4)) and (min(y1,y2) <= y <= max(y1, y2)) and (min(y3,y4) <= y <= max(y3, y4)):
#         print(1)
#     else:
#         print(0)


### 두번째 접근방법
A1 = y2-y1
B1 = x1-x2
C1 = A1*x1 + B1*y1

A2 = y4-y3
B2 = x3-x4
C2 = A2*x3 + B2*y3

D = A1*B2-B1*A2

if D == 0:
    if A1*x3+B1*y3 == C1:
        if (min(x1,x2) <=max(x3,x4) and max(x1,x2) >= min(x3,x4)) and (min(y1,y2) <=max(y3,y4) and max(y1,y2) >= min(y3,y4)):
            print(1)
        else:
            print(0)
        sys.exit()
    else:
        print(0)
        sys.exit()

x = (B2*C1-B1*C2)/D
y = (A1*C2-A2*C1)/D

if (min(x1,x2) <= x <= max(x1,x2)) and (min(x3,x4) <= x <= max(x3, x4)) and (min(y1,y2) <= y <= max(y1, y2)) and (min(y3,y4) <= y <= max(y3, y4)):
    print(1)
else:
    print(0)