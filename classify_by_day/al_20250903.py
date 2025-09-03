import sys
import math

l = int(sys.stdin.readline())
r = int(sys.stdin.readline())
k = int(sys.stdin.readline())

### 1. First Approach
# ans = set()
# for x in range(1, r//k):
#     lower_b = (2*l/k - 2*x)/(k-1)
#     upper_b = (2*r/k - 2*x)/(k-1)
    
#     for d in range(max(1, math.ceil(lower_b)), int(upper_b)+1):
#         ans.add(int((2*x+(k-1)*d)*k/2))
    

# print(len(ans))


### 2. Second Approach
sum_v = 0
if k == 2:
    sum_v = max(0, r - max(l, 3) +1)
elif k == 3:
    sum_v = max(0, r//3 - ((max(l, 6)-1)//3))
elif k == 4:
    
    if l<= 10 <= r:
        sum_v += 1
    sum_v += max(0, r//2- (math.ceil(max(14, l)/2)-1))
elif k == 5:
    sum_v = max(0, r//5 - ((max(l, 15)-1)//5))

print(sum_v)


explain = """
처음에는 범위를 좁히고 합을 구하는 공식을 정리한 식에 하나씩 넣어보면서 가능한
경우의수를 카운트 했지만 시간초과가 발생하였다. 두번째 접근에서는 2<=k<=5가 조건인
것을 이용해서 각 경우에 따라 공식을 간소화 해서 카운트했다.
"""