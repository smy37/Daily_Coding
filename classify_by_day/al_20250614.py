import sys 
import math

H, V = map(float, sys.stdin.readline().split())

D = math.sqrt(H**2+V**2)

cos_2x = H/D
cos_x = math.sqrt((cos_2x+1)/2)

x = H/cos_x
y = math.sqrt(x**2-H**2)
w = x/2
d = V-y

h = d*cos_x

print(w, h)

explain = """
핵심은 이음줄 포스터를 만들기 위해서는 직사각형의 한 대각선에 대하여 대각선을 이루지 않는 두 꼭지점을
대각선을에 붙히는 식으로 접는 것을 통해 평행 사변형이 만들어진다. 그리고 평행 사변형의 아랫변의 중점에
대하여 아랫변을 이루는 두 양끝점을 붙히는 식으로 접는 것으로 완성된다. 이때 필요한 길이들을 삼각함수
공식을 이용하여 구하면 된다.
"""
