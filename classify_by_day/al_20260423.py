import sys
import math

PI = math.pi

n, s = map(int, sys.stdin.readline().split())
sphere_list = []

def cal_sphere_volume(radius):
    return 4/3*PI*(radius**3)

total_volume = 10**5 * 10**5 * 10**5
total_sphere_volume = 0

for _ in range(n):
    r, x, y, z = map(int, sys.stdin.readline().split())
    sphere_list.append([r,x,y,z])
    total_sphere_volume += cal_sphere_volume(r)

real_volume = total_volume-total_sphere_volume
cutting_point = []

def cal_volume(z_cord):
    bases_volume = 10**5 *10**5 *z_cord

    for sphere in sphere_list:
        r, x, y, z = sphere
        if z_cord <= z-r:
            continue
        elif z_cord >= z+r:
            bases_volume-=cal_sphere_volume(r)
        else:
            z_dist = z_cord-(z-r)
            hole_volume = (z_dist**2*r-(z_dist**3)/3)*PI
            bases_volume -= hole_volume

    return bases_volume

for i in range(1, s+1):
    target_volume = real_volume*(i/s)
    left, right = 0, 10**5
    for _ in range(37):
        mid = (left+right)/2.0

        cur_volume = cal_volume(mid)

        if cur_volume > target_volume:
            right = mid
        elif cur_volume < target_volume:
            left = mid
    mid = (left+right)/2.0
    cutting_point.append(mid)

for i in range(len(cutting_point)):
    if i != 0:
        print(round((cutting_point[i]-cutting_point[i-1])/1000, 9))
    else:
        print(round((cutting_point[i]/1000), 9))