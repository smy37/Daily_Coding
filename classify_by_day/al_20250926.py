import sys 
import math
a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y = map(int, sys.stdin.readline().split())

d1 = math.sqrt((a_x-b_x)**2+(a_y-b_y)**2)
d2 = math.sqrt((c_x-d_x)**2 +(c_y-d_y)**2)



dx1 = (b_x-a_x)
dy1 = (b_y-a_y)

dx2 = (d_x-c_x)
dy2 = (d_y-c_y)
if (dx1-dx2)**2 + (dy1-dy2)**2 == 0:
    t = 0
else:
    t = -((dx1-dx2)*(a_x-c_x)+(dy1-dy2)*(a_y-c_y))/((dx1-dx2)**2 + (dy1-dy2)**2)

if t < 0:
    t = 0
elif t > 1:
    t = 1

xmin_1 = a_x+dx1*t
ymin_1 = a_y+dy1*t

xmin_2 = c_x+dx2*t
ymin_2 = c_y+dy2*t

print(math.sqrt((xmin_1-xmin_2)**2 + (ymin_1-ymin_2)**2))

explain = """
시간이 같다는게 조건이므로 동시에 도착하는데 걸리는 시간을 t=1이라고 하면 
속력은 dx와 dy가 되고 t초 후에 위치는 x0+dx, y0+dy가 된다.
"""