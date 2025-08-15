import sys
import math
from collections import deque

def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
         if n % i == 0:
             return False
    return True

T = int(sys.stdin.readline())

for _ in range(T):
    N, A, B = map(int, sys.stdin.readline().split())
    prime = {}
    for i in range(A, B+1):
        if check_prime(i):
            prime[i] = 1
    if len(prime) == 0:
        print(-1)
        continue
    dq = deque()
    dq.append([N, 0])
    visit = {N:1}
    flag = False
    while dq:
        t = dq.popleft()
        n, cur_cnt = t[0], t[1]
        if n in prime and (A<=n<=B):
            print(cur_cnt)
            break
        for i in range(4):
            if i == 0:
                next_n = n//2
            elif i == 1:
                next_n = n//3
            elif i == 2:
                next_n = n+1
            elif i == 3:
                next_n = n-1 if n > 0 else n
            if next_n not in visit:
                visit[next_n] = 1
                dq.append([next_n, cur_cnt + 1])


explain = """
소수를 구하는 함수를 제곱근과 약수의 성질을 이용하여 최적화 하고 BFS를 사용하여 간 단계별로 4가지로
분화되는 수형도에 대해서 BFS를 수행한다. 
"""

