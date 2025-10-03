import sys

H, W = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

x = max(H, W)
y = min(H, W)

s_l = []
for _ in range(N):
    r, c = map(int, sys.stdin.readline().split())
    s_l.append([r, c])

s_l = sorted(s_l, key = lambda x : [x[0], x[1]], reverse= True)

max_area = 0
for i in range(len(s_l)):
    for j in range(i+1, len(s_l)):
        s1 = s_l[i]
        s2 = s_l[j]

        x1, y1 = max(s1), min(s1)
        x2, y2 = max(s2), min(s2)

        if x >= x1 and y >= y1:
            r_x = x-x1
            
            rest_x, rest_y = max(r_x, y), min(r_x, y)

            if rest_x >= x2 and rest_y >= y2:
                max_area = max(max_area, x1*y1 + x2*y2)

            r_y = y-y1
            if x >= x2 and r_y >= y2:
                max_area = max(max_area, x1*y1 + x2*y2)
        
        if x >= y1 and y >= x1:
            r_x = x-y1
            rest_x, rest_y = max(r_x, y), min(r_x, y)
            
            if rest_x >= x2 and rest_y >= y2:
                max_area = max(max_area, x1*y1 + x2*y2)
            r_y = y-x1
            if x>= x2 and r_y >= y2:
                max_area = max(max_area, x1*y1 + x2*y2)

print(max_area)

explain = """
긴변을 배경의 긴변에 붙히는 경우와 긴변을 배경의 짧은변에 붙히는 경우로 일단 나누고
그안에서 두번째 사각형을 x축으로 붙히는 경우와 y축으로 붙히는 경우를 생각해준다.
"""