import sys
import math

N = int(sys.stdin.readline())
number_l = list(map(int, sys.stdin.readline().split()))

sum_v = math.inf
answer_l = -1
answer_r = -1
for i in range(N-1):
    cur = number_l[i]
    left_idx = i+1
    right_idx = N-1

    while left_idx <= right_idx:
        mid = (left_idx+right_idx)//2

        temp = cur + number_l[mid]

        if abs(temp) < sum_v:
            sum_v = abs(temp)
            answer_l = i
            answer_r = mid

            if temp == 0:
                print(number_l[answer_l], number_l[answer_r])
                sys.exit()

        if temp < 0:
            left_idx = mid+1
        elif temp > 0:
            right_idx = mid-1

print(number_l[answer_l], number_l[answer_r])

## mid 값을 (left + right)//2 로 한 것 과 left = mid+1, right = mid-1로 한 것 그리고 whlie left <= right 로 조건을 선택 한 것은 모두 연결이 되어 있다.
## 가장 먼저 mid 값을 (left+right)//2 로 했기 때문에 2,4와 같은 상황에서 mid값이 3이 되어 3,4로 갔고 idx 3일 때 상한이 아닌 하한이 갱신되는 상황이라고 생각해보자.
## 그렇다면 while 루프를 돌아도 3,4가 되서 무한루프에 빠져버리게 된다. 그래서 이를 방지하기 위해 left = mid +1 ,right = mid -1 이라는 조건이 추가되었다.
## 물론 탐색이고 mid에 해당하는 값에 대해 체크를 했기 때문에 +1, -1을 해도 빠지는게 없게 된다. 그리고 이러한 +1, -1 조건이 있기 때문에 left와 right가 같은 값이 될 수 있게 된다.
## 그렇기 때문에 while문에 left < right 가 아닌 left <= right를 사용하게 된다.