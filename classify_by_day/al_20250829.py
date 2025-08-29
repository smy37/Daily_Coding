import sys
import math

def check_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

A, B = map(int, sys.stdin.readline().split())

lower = math.ceil(math.sqrt(A))
upper = math.floor(math.sqrt(B))

cnt = 0
for n in range(lower, upper+1):
    if check_prime(n):
        print(n)
        cnt += 1

print(cnt)
