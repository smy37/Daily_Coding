import sys
import math

N, L = map(int, sys.stdin.readline().split())

cord_list = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    cord_list.append([x, y])

cord_list.sort(key = lambda x : [x[1], x[0]])

def cal_dist(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def cross_product(x1, y1, x2, y2):
    return x1*y2 - y1*x2

def ccw(x1, y1, x2, y2, x3, y3):
    v1 = [x1-x2, y1-y2]
    v2 = [x1-x3, y1-y3]

    ccw_v = cross_product(*v1, *v2)
    if ccw_v >= 0:
        return True
    else:
        return False

s = []
for i in range(len(cord_list)):
    x, y = cord_list[i]

    if len(s) <= 1:
        s.append([x,y])
    else:
        if ccw(*s[-2], *s[-1], x, y):
            s.append([x, y])
        else:
            while 1:
                s.pop()
                if len(s) <=1:
                    s.append([x, y])
                    break
                if ccw(*s[-2], *s[-1], x, y):
                    s.append([x, y])
                    break

s2 = []
for i in range(len(cord_list)-1, -1, -1):
    x, y = cord_list[i]

    if len(s2) <= 1:
        s2.append([x, y])
    else:
        if ccw(*s2[-2], *s2[-1], x, y):
            s2.append([x, y])
        else:
            while 1:
                s2.pop()
                if len(s2) <= 1:
                    s2.append([x, y])
                    break
                if ccw(*s2[-2], *s2[-1], x, y):
                    s2.append([x, y])
                    break

s = s[:-1]+ s2[:-1]

answer = 0
for i in range(len(s)):
    if i == len(s)-1:
        cur_dist = cal_dist(*s[i], *s[0])
    else:
        cur_dist = cal_dist(*s[i], *s[i+1])
    answer += cur_dist

cri = L*math.pi*2
answer += cri

print(round(answer))

explain = """If two lines are offset in parallel by the same distance, a curve is formed at the corner.  
The central angle of this curve is equal to (180° minus the internal angle between the two lines). 
"""
