import sys

N = int(sys.stdin.readline())
cord_list = []

cen_x, cen_y = 0, 0
for _ in range(N):
    x, y = map(float, sys.stdin.readline().split())
    cord_list.append([x,y])
    cen_x += x
    cen_y += y

cen_x /= N
cen_y /= N

w = 0.1
max_dist = 0
for _ in range(1000000):
    max_dist = 0
    max_idx = 0
    for i in range(len(cord_list)):
        x, y = cord_list[i]
        cur_dist = (cen_x-x)**2 + (cen_y-y)**2
        if max_dist < cur_dist:
            max_dist = cur_dist
            max_idx = i
    max_x, max_y = cord_list[max_idx]
    cen_x += (max_x-cen_x)*w
    cen_y += (max_y-cen_y)*w

    w *= 0.999
radius = (max_dist**0.5)*2
print(f"{radius:0.2f}")