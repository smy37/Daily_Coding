import sys
import math

N = int(sys.stdin.readline())

node_l = []
for _ in range(N):
    node_l.append(list(map(int, sys.stdin.readline().split())))

center_x = sum([x[0] for x in node_l])/N
center_y = sum([x[1] for x in node_l])/N

def cal_angle(cri, point):
    dx = point[0]-cri[0]
    dy = point[1]-cri[1]

    angle = math.atan2(dy, dx)

    return angle

## 정렬을 안해도 되는가? 순서대로 주어진다고 안주어졌는데...
# node_l = sorted(node_l, key = lambda x : cal_angle([center_x, center_y], x))

plus_sum = 0
minus_sum = 0
for i in range(N-1):
    plus_sum += node_l[i][0]*node_l[i+1][1]
    minus_sum += node_l[i+1][0]*node_l[i][1]
plus_sum += node_l[-1][0]*node_l[0][1]
minus_sum += node_l[0][0]*node_l[-1][1]
print(round(abs(plus_sum-minus_sum)/2, 2))