import sys

for _ in range(4):
    temp_line = list(map(int, sys.stdin.readline().split()))
    l_x1,l_y1,r_x1,r_y1 = temp_line[:4]
    l_x2,l_y2,r_x2,r_y2 = temp_line[4:]

    if (l_x1 > r_x2 or l_x2 > r_x1 or l_y1 > r_y2 or l_y2 > r_y1):
        print("d")
    elif (l_x1 == r_x2 and (l_y1 == r_y2 or r_y1 == l_y2)) or\
    (r_x1 == l_x2) and (r_y1 == l_y2 or l_y1 == r_y2):
        print("c")
    elif (l_x2 < r_x1 and l_x1 < r_x2) and ((l_y2 < r_y1) and (l_y1 < r_y2)):
        print("a")
    else:
        print("b")
    

explain = """
사각형 두개중에 한개를 고정하고 나머지 한개를 움직이면서 생각하면 더 쉬운 문제.
안만나는 경우, 점에서 만나는 경우, 겹치는 부분이 직사각형인 부분, 겹치는 부분이 선분인 선으로 생각해준다.
"""