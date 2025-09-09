import sys 
import math
from collections import deque

K = int(sys.stdin.readline())

### 1. First Approach
# dq = deque()
# dq.append([K, 0])

# max_scar = 0
# while dq:
#     k, scar_cnt = dq.popleft()
    
#     max_scar = max(max_scar, scar_cnt)
#     for i in range(int(math.sqrt(k)), 1, -1):
#         if k % i == 0:
#             dq.append([i, scar_cnt+1])
#             dq.append([k//i, scar_cnt+1])
#             break
# print(max_scar)

### 2. Second Approach
n = K
d = 2
r = 0

while d*d <= n:
    if n%d == 0:
        r += 1
        n = n//d
    else:
        d += 1

if n > 1:
    r += 1

print(math.ceil(math.log2(r)))

explain = """
처음에는 가장 큰 약수로 나눠가는 접근을 취했지만 40과 같은 경우에는 원래는 depth 2번만에 분할이 가능한데
해당 로직으로는 3번에 가능했다. 
두번째 로직은 소인수분해를 하고 인수의 개수에 log2를 씌우고 올림한 것이 총 분할하는데 걸리는 횟수가 된다.
"""