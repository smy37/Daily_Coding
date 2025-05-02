import sys
import math

N, M = map(int, sys.stdin.readline().split())

num_l = []
for _ in range(N):
    num_l.append(int(sys.stdin.readline()))
num_l = sorted(num_l)

upper_bound = M*min(num_l)
answer = math.inf

left = 1
right = upper_bound

while left <= right:
    mid = (left+right)//2
    temp_sum = 0
    for i in range(len(num_l)):
        temp_sum += mid//num_l[i]
    if M<= temp_sum and mid < answer:
        answer = mid

    if temp_sum >= M:
        right = mid-1
    else:
        left = mid+1

print(answer)

### Binary Search 역시 DP와 마찬가지로 관점을 바꿀 필요가 있다.
### 요구사항과 구해야 하는 것을 명확히 한 후, 구해야 하는 값을 직접 구할려고 하는 것도 상황에 따라서 가장 효율적인 방법이 될 수 도 있다.
### 이 문제에서도 소요되는 시간을 구해야 되는 값으로 하고 해당 값을 이분 탐색을 통해서 찾았다. 소요되는 시간에 대해서 각 게이트의 소요시간으로 몫을 구해서 합한 것이
### 해당 소요시간에서 처리할 수 있는 최대 인원이 된다는 것이 문제 해결의 키 포인트이다.
### 해당 시간에서 처리할 수 있는 최대 인원을 각 탐색 마다 구해야 하고 소요 되는 일자를 저장해 두었다가 최솟값을 갱신해야 한다.
### 이렇게 직관적이지 않은 변수가 2개 존재할 때, 이 2개를 조건문에서 사용할 때 헷갈릴 수가 있는데, 하나씩 차근차근 정리하는 것이 유일한 답인 것 같다.
### 가끔은 이걸 직접적으로 구하는 방벙이 가능해? 라는 생각이 들더라도 직접적으로 구하는 방법을 찾아볼려고 하는 관점의 전환이 필요하다.