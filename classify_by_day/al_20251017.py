import sys 
import math 

x1, y1, x2, y2, x3, y3 = map(int, sys.stdin.readline().split())
S = abs((x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3))*0.5

c_x, c_y = (x1+x2+x3)/3, (y1+y2+y3)/3
A1 = S*c_y*2*math.pi
A2 = S*c_x*2*math.pi

print(A1, A2)

explain = """
직관적으로 부피가 2차원에서의 면적에 도심까지의 거리를 반지름으로 해서 구성한 입체도형이라고 생각하였는데
그렇게 풀이되었다.
"""