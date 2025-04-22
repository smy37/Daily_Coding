import sys
N = int(sys.stdin.readline())

gradient = {"inf_1":0, "inf_4":0}
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    plane = ""
    if x >=0 and y>= 0:
        plane = "1"
    elif x < 0 and y>= 0 :
        plane = "2"
    elif x < 0 and y < 0 :
        plane = "3"
    elif x >= 0 and y < 0 :
        plane = "4"
    if x == 0:
        if y>=0:
            gradient["inf_1"] += 1
        else:
            gradient["inf_4"] += 1
    else:
        grad = y/x
        name = f"{grad}_{plane}"
        if name not in gradient:
            gradient[name] = 0
        gradient[name] += 1

print(max(gradient.values()))