import sys
import math

ball_r = 10
target_r = 6

T = int(sys.stdin.readline())

for _ in range(T):
    dist, angle = sys.stdin.readline().split()
    dist = float(dist)
    angle = int(angle)

    angle_dist = 6/(math.sin(math.radians(angle)))
    target_dist = 42/(math.tan(math.radians(angle)))

    base = 2*target_dist
    upper = base + 2*angle_dist
    lower = base - 2*angle_dist

    if lower <= dist <= upper:
        print("yes")
    else:
        print("no")
