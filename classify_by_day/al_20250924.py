import sys
import math

N = int(sys.stdin.readline())

## 1. First Approach
# if N == 1:
#     print(0)
# else:
#     print(int(math.ceil(N/2)))


## 2. Second Approach
if N == 1:
    print(0)
elif N%2 == 0:
    print(N//2)
else:
    print(N//2+1)


explain = """
첫번째 시도에서는 ceil을 사용했지만 큰 수 N에 대하여 부동소수점 오류가 발생한다.
잘라야 하는 개수는 원통을 생각했을 때, 중심을 지나서 자르는 것을 생각하면 겉면적과 부피가 모두
같게 자를 수 있다. 또한 홀수의 경우 하나 더 많게 자르는데 마지막 2조각이 합쳐야 나머지 한조각이 되도록 자른다.
"""