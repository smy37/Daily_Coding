import sys

N = int(sys.stdin.readline())
cord_list = []

cen_x, cen_y, cen_z = 0, 0, 0
for _ in range(N):
    x, y, z = map(float, sys.stdin.readline().split())
    cord_list.append([x, y, z])

    cen_x += x
    cen_y += y
    cen_z += z

cen_x /= N
cen_y /= N
cen_z /= N

w = 0.1
max_dist = 0
for _ in range(100000):
    max_dist = 0
    max_idx = 0

    for i in range(len(cord_list)):
        x, y, z = cord_list[i]
        temp_dist = (cen_x-x)**2+(cen_y-y)**2 +(cen_z-z)**2
        if max_dist < temp_dist:
            max_dist = temp_dist
            max_idx = i
    x, y, z = cord_list[max_idx]
    cen_x += (x-cen_x)*w
    cen_y += (y-cen_y)*w
    cen_z += (z-cen_z)*w

    w *= 0.999

print(f"{max_dist**0.5:.2f}")
