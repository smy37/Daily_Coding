import sys
import math

l = int(sys.stdin.readline())
r = int(sys.stdin.readline())
k = int(sys.stdin.readline())

## 1. First Approach
ans = set()
for x in range(1, r//k):
    lower_b = (2*l/k - 2*x)/(k-1)
    upper_b = (2*r/k - 2*x)/(k-1)
    
    for d in range(max(1, math.ceil(lower_b)), int(upper_b)+1):
        ans.add(int((2*x+(k-1)*d)*k/2))
    

print(len(ans))

