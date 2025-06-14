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