import sys
import math

while 1:
    try:
        r, h, d1, A1, d2, A2 = map(float, sys.stdin.readline().split())
    except:
        break
    angle = min(abs(A1-A2), 360-(abs(A1-A2)))
    angle *= (math.pi/180)

    l = angle*r
    d = math.sqrt(r**2+h**2)
    theta = l/d

    answer = d1**2 + d2**2 + (-2*d1*d2)*math.cos(theta)
    answer = answer**0.5
    print(f"{answer:.2f}")

explain = """"
There are three steps to solve this problem.
First, calculate the arc length using the angles A1 and A2.  
Second, compute theta using the relation d (the hypotenuse length) × theta = arc length.  
Finally, apply the law of cosines to find the shortest distance between the two points. 
"""