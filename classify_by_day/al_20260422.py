import sys

N = int(sys.stdin.readline())

if N <=3:
    print("TAK")
    sys.exit()

cord_list = []
rest_list = []
for _ in range(2):
    cord_list.append(list(map(int, sys.stdin.readline().split())))

x1, y1, z1 = cord_list[0]
x2, y2, z2 = cord_list[1]
v1 = [x1-x2, y1-y2, z1-z2]

flag = False
for _ in range(N-2):
    x_t, y_t, z_t = map(int, sys.stdin.readline().split())
    v_t = [x1-x_t, y1-y_t, z1-z_t]

    cross_v = [v1[1]*v_t[2]-v1[2]*v_t[1], -(v1[0]*v_t[2])+v1[2]*v_t[0], v1[0]*v_t[1]-v1[1]*v_t[0]]
    if cross_v == [0,0,0]:
        continue
    else:
        if not flag:
            x3, y3, z3 = x_t, y_t, z_t
            flag = True
        else:
            rest_list.append([x_t, y_t, z_t])

if not flag:
    print("TAK")
    sys.exit()

v2 = [x1-x3, y1-y3, z1-z3]

n_vector = [v1[1]*v2[2]-v1[2]*v2[1], -(v1[0]*v2[2])+v1[2]*v2[0], v1[0]*v2[1]-v1[1]*v2[0]]

def check_on_plane(x, y, z, n_v):
    if n_v[0]*(x-x1)+n_v[1]*(y-y1)+n_v[2]*(z-z1) == 0:
        return True
    else:
        return False

for i in range(len(rest_list)):
    x, y, z = rest_list[i]
    if not check_on_plane(x, y, z, n_vector):
        print("NIE")
        sys.exit()

print("TAK")

explain = """Cross product can get a normal vector of a plane
"""
