import sys
import math

def factorial(n):
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result

N = int(sys.stdin.readline())
temp = list(map(int, sys.stdin.readline().split()))

if temp[0] == 1:
    k = temp[1]
    record = {}
    rest = [i for i in range(1, N+1)]
    for i in range(N):
        cnt = 0
        fact_v = factorial(N-i-1)
        t = math.ceil(k/fact_v)     ## 핵심이 되는 부분 1.
        record[rest[t-1]] = True
        del rest[t-1]
        k -= fact_v*(math.floor(k/fact_v))   ## 핵심이 되는 부분 2.
        if k == 0:
            rest = sorted(rest, reverse=True)
            break
    for t in record:
        print(t, end=" ")
    for t in rest:
        print(t, end=" ")

elif temp[0] == 2:
    answer = 0
    record = {}
    for i in range(N):
        cur_n = temp[i+1]
        fact_v = factorial(N-i-1)
        for j in range(1, cur_n):
            if j not in record:
                answer += fact_v
        record[cur_n] = True
    print(answer+1)


## k가 주어졌을 때, 해당하는 순열을 구하는 과정에서 k를 factorial 값으로 나눈 결과에 따라 해당 자리의 숫자를 결정하는게 쉽지만은 않았다.
## 특히나 k가 factorial 값으로 나누어질 때의 처리를 나는 if k == 0: rest = sorted(rest, reverse=True) 하였는데
## 실제로는 idx = (k-1)//factorial_v 로 함으로써 쉽게 해결할 수 도 있다. 단, k-=factorial_v*idx 를 통해 k 가 0이 되는 지점에 대한 처리가 이해하기 쉽진 않다.