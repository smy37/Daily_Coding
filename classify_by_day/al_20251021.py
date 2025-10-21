import sys 
import math

### First Approach
# def One2Two(x, y, z):
#     return math.sqrt(x**2+y**2), math.acos(x/(math.sqrt(x**2+y**2))), z

# def Two2One(r, phi, z):
#     return r*math.cos(phi), r*math.sin(phi), z

# def One2Three(x, y, z):
#     return math.sqrt(x**2+y**2+z**2), math.acos(z/math.sqrt(x**2+y**2+z**2)), math.acos(x/math.sqrt(x**2+y**2))

# def Three2One(rho, theta, phi):
#     return rho*math.sin(theta)*math.cos(phi), rho*math.sin(theta)*math.sin(phi), rho*math.cos(theta)

### Second Approach
def One2Two(x, y, z):
    phi = math.atan2(y, x)
    if phi < 0: 
        phi += 2*math.pi
    return math.sqrt(x**2+y**2), phi, z

def Two2One(r, phi, z):
    return r*math.cos(phi), r*math.sin(phi), z

def One2Three(x, y, z):
    phi = math.atan2(y, x)
    if phi < 0: 
        phi += 2*math.pi
    return math.sqrt(x**2+y**2+z**2), math.atan2(math.sqrt(x**2+y**2), z), phi

def Three2One(rho, theta, phi):
    return rho*math.sin(theta)*math.cos(phi), rho*math.sin(theta)*math.sin(phi), rho*math.cos(theta)

T = int(sys.stdin.readline())

for _ in range(T):
    in_cord, out_cord = map(int, sys.stdin.readline().split())
    a, b, c = map(float, sys.stdin.readline().split())

    if in_cord == 1:
        if out_cord == 2:
            print(*One2Two(a, b, c))
        elif out_cord == 3:
            print(*One2Three(a, b, c))
    elif in_cord == 2:
        if out_cord == 1:
            print(*Two2One(a, b, c))
        elif out_cord == 3:
            print(*One2Three(*Two2One(a, b, c)))
    elif in_cord == 3:
        if out_cord == 1:
            print(*Three2One(a, b, c))
        elif out_cord == 2:
            print(*One2Two(*Three2One(a, b, c)))


explain = """
사실상 직교, 원통, 구면간의 좌표 변환의 식을 세우는건 어렵지 않았다. 그러나 cos역함수를 이용해서 각을 구했을 때, 
분모가 0이되는 상황을 처리해야 했고 쉽지 않았다. 이때, 파이썬에서는 atan2를 이용하면 분모가 0이되는 상황에서 손쉽게 각을 구할 수 있다.
또한 각 phi를 구해주는 과정에서 atan2는 -pi와 pi 사이의 값을 도출하기 때문에 이를 0과 2*pi 사이로 변환하는 과정이 필요하다.
"""