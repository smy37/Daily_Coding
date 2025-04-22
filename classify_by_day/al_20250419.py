import sys
import math

N = int(sys.stdin.readline())

### Method 1. 소수를 미리 저장. -> 메모리 초과
# max_cri = 10**N
# prime_l = [0]*(max_cri)
#
# for i in range(2, max_cri):
#     if prime_l[i] == 0:
#         prime_l[i] = 1
#         for j in range(2, math.ceil(max_cri/i)):
#             prime_l[i*j] = 2
#
#
# for i in range(10**(N-1), 10**N):
#     for j in range(N):
#         idx = i//10**j
#         if prime_l[idx] != 1:
#             break
#     else:
#         print(i)

### Method 2. 그때 그때, 소수를 판별 -> 시간 초과
# def check_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if n % i == 0 :
#             return False
#     return True
#
# max_cri = 10**N
#
# for i in range(10**(N-1), 10**N):
#     for j in range(N-1, -1, -1):
#         idx = i//10**j
#         if not check_prime(idx):
#             break
#     else:
#         print(i)

### Method 3. 가장 왼쪽수부터 숫자를 더해가면서 (더해가는 숫자는 1, 3, 5, 7, 9 중에 있어야함.) 소수인지를 판별.
def check_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0 :
            return False
    return True

def prime_depth_check(n, depth):
    if depth == N:
        print(n)
        return
    for i in [1, 3, 5, 7, 9]:
        next_n = 10*n + i
        if check_prime(next_n):
            prime_depth_check(next_n, depth+1)

for i in [2, 3, 5, 7]:
    prime_depth_check(i, 1)

