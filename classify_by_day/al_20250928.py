import sys

T = int(sys.stdin.readline())
for _ in range(T):
    cord_l = []
    for _ in range(4):
        x, y = map(int, sys.stdin.readline().split())
        cord_l.append([x,y])
    d1 = (cord_l[0][0]-cord_l[1][0])**2 + (cord_l[0][1]-cord_l[1][1])**2
    d2 = (cord_l[0][0]-cord_l[2][0])**2 + (cord_l[0][1]-cord_l[2][1])**2
    d3 = (cord_l[0][0]-cord_l[3][0])**2 + (cord_l[0][1]-cord_l[3][1])**2

    dist_l = sorted([[d1, cord_l[1]], [d2, cord_l[2]], [d3, cord_l[3]]], key = lambda x : x[0])
    ori_x, ori_y = cord_l[0]
    if dist_l[0][0] == dist_l[1][0] and 2*dist_l[0][0] == dist_l[2][0]:
        x1, y1 = dist_l[0][1][0]-ori_x, dist_l[0][1][1]-ori_y
        x2, y2 = dist_l[1][1][0]-ori_x, dist_l[1][1][1]-ori_y
        x3, y3 = dist_l[2][1][0]-ori_x, dist_l[2][1][1]-ori_y

        if x3 == (x1+x2) and y3 == (y1+y2):
            print(1)
        else:
            print(0)
    else:
        print(0)

explain = """
한 점 기준 다른 세점과의 거리를 측정하고 거리를 기반으로 가장 먼점을 판별한다. 
나머지 길이의 제곱합이 가장 긴 길이와 같고 벡터 역시 나머지 두 벡터가 가장 거리가
큰 벡터와 같다면 정사각형을 만족한다.
"""