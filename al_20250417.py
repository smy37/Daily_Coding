import sys

N = int(sys.stdin.readline())
target_l = list(map(int, sys.stdin.readline().split()))

sum_t = sum(target_l)

if sum_t%3 != 0:
    print("NO")
else:
    two_cnt = sum([n //2 for n in target_l])

    if two_cnt >= sum_t//3:
        print("YES")
    else:
        print("NO")


## 푸는 방법을 알면 구현은 간단하지 않았지만 2를 증가시키는 케이스에 대해서 그리드하게 프로세스를 진행하는 것이
## 예외 케이스를 만들지 않는다는 것을 이해하는 것은 쉽지 않았다. 
## 핵심은 매 시행마다 결국 2가 더 해져야 하고 전체의 합이 3의 배수라면 1이 어디에 더해지는 지는 고려하지 않아도 된다.
## 1이 가장 적은 양의 정수이기 때문에 자유도가 높은점이 이러한 풀이를 가능케 한다. 결국 매 시행에서 2의 위치만 고려해서 놓을 수
## 있다면 총 합이 3의 배수가 되는 경우를 만들 수 있다. 