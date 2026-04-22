import sys

board = []
for _ in range(4):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)

d1 = board[0][1]
d2 = board[0][2]
d3 = board[1][2]

if d1 <= d2+d3 and d1 >= abs(d2-d3):

    d41 = board[0][3]
    d42 = board[1][3]

    if abs(d41-d42) <= d1 <= d41+d42:
        cos1 = (d3**2 - d2**2 -d1**2)/(-2*d1*d2)
        sin1 = (1-cos1**2)**0.5
        x1 = d2*cos1
        y1 = d2*sin1

        cos2 = (d42**2 - d41**2 -d1**2)/(-2*d41*d1)
        sin2 = (1-cos2**2)**0.5
        x2 = d41*cos2
        y2 = d41*sin2

        if (x1-x2)**2 + (y1-y2)**2 <= board[2][3]**2 <= (x1-x2)**2 + (y1+   y2)**2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

else:
    print("NO")