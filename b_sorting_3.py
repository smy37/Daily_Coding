import sys
import math

cri = 1000000007

def factorial(n:int, mod:int):
    result = 1
    for i in range(n,1,-1):
        result = (result * i)%mod
    return result

def divide(mit:int, gisu:int, mod : int):
    if gisu == 1:
        return mit % mod

    elif gisu % 2 != 0:
        return (divide(mit, (gisu-1)//2, mod)**2)*mit%mod

    elif gisu % 2 == 0:
        return divide(mit, gisu//2, mod)**2%mod


n, k = list(map(int, sys.stdin.readline().strip().split(' ')))

A = factorial(n, cri)
B = factorial(k, cri)*factorial(n-k, cri)

print(A*divide(B, cri-2, cri)%cri)