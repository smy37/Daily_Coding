import sys
import math

def check_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

while 1:
    p, a = map(int, sys.stdin.readline().split())
    fake_prime_flag = False
    if p == 0 and a == 0:
        break
    next_a = 1
    if not check_prime(p):
        next_a = pow(a, p, p)
        if next_a == a:
            if not check_prime(p):
                fake_prime_flag = True

    if fake_prime_flag:
        print("yes")
    else:
        print("no")

explain = """
문제에서 제시한 연산을 수행하고 소수인지 판단하면 간단하게 해결하는 문제. 
그러나 처음에 pow 함수를 안쓰고 해보려고 했지만 ** 연산을 하면 메모리 초과, 
for문에 p개만큼 a를 곱해주는 연산을 하면 시간초과가 발생하였다. pow(a,b,c) 처럼 사용해서
중간중간에 모듈러 연산을 하면서도 제곱 연산을 빠르게 수행해야 한다.
"""