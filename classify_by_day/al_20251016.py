import sys 

N = int(sys.stdin.readline())
x_dist, y_dist = map(int, sys.stdin.readline().split())
cord_l = {}

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x not in cord_l:
        cord_l[x] = {}
    cord_l[x][y] = 1

x_list = sorted(list(cord_l.keys()))

answer = 0
for x1 in x_list:
    x2 = x1+x_dist
    if x2 in cord_l:
        for y1 in cord_l[x1]:
            y2 = y1+y_dist
            if y2 in cord_l[x1] and y1 in cord_l[x2] and y2 in cord_l[x2]:
                answer += 1

print(answer)

explain = """
좌표를 해시에 저장해두고 현재 좌표를 기준으로 직사각형을 이루는 3점이 존재하는지 판단해준다.
"""



