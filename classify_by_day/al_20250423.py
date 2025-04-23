import sys
import math

T = int(sys.stdin.readline())

### 1. 첫번째 시도, 탄젠트를 이용하여 각도를 구한 후, 기대값을 합-분해 공식으로 구할 수 있음을 이용
# for _ in range(T):
#     N = int(sys.stdin.readline())
#     answer = 0
#     g_l = []
#     for i in range(N):
#         x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#         g1 = math.atan2(y1, x1)
#         g2 = math.atan2(y2, x2)
#         min_g = min(g1, g2)
#         max_g = max(g1, g2)
#
#         answer += min(abs(min_g-max_g), abs(min_g+max_g))
#     print(round(answer/(2*math.pi), 6))

### 2. 두번째 시도, 탄젠트를 이용 시, x축에서의 각도 처리가 어려움이 있어 사잇각을 코사인을 이용하여 구함.
def in_product(x1, y1, x2, y2):
    return x1*x2 + y1*y2

for _ in range(T):
    N = int(sys.stdin.readline())
    answer = 0
    for i in range(N):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        cos_v = in_product(x1, y1, x2, y2)/(math.sqrt(x1**2+y1**2)*math.sqrt(x2**2+y2**2))
        cos_v = min(1, max(-1, cos_v))
        answer += math.acos(cos_v)
    print(f"{answer/(2*math.pi):.5f}")


### 처음에는 각도를 삼각함수 역함수로 구해준 후에, 겹치는 부분을 구할려고 하였다.
### 좌측 끝점으로 정렬 후에, 오른쪽 끝점을 stack에 넣고 선분의 교차를 판별하는 것 처럼 할려고 했지만 개수를 누적해서 세주다가 최종적으로
### 모든 선분을 고려했을 때의 각 개수에 따른 구간을 구하는 것이 쉽지 않았다.
### 그런데 기대값의 성질을 생각해보면 1*(1개 맞을 구간의 각도) + 2*(2개 맞을 구간의 각도) + 3*(3개 맞을 구간의 각도) + ...
### 을 하는 것과 1*(선분 1의 각도) + 1*(선분 2의 각도) + ... 을 하는 것이 같음을 알 수 있다.
### 이러한 성질을 이용하고 선분의 각도를 구할 때, 탄젠트를 이용하는 것보다는 내적을 통해 코사인을 구하는 것이 좋다는 것을 이용하면 풀 수 있다.