import sys

num_list = []

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    num_list.append(n)

upper_limit = max(num_list)
is_prime = [False, False] + [True]*(upper_limit-1)

for i in range(4, upper_limit+1, 2):
    is_prime[i] = False

i = 3
while i*i <= upper_limit:
    if is_prime[i]:
        for j in range(i*i, upper_limit+1, i*2):
            is_prime[j] = False
    i += 2

primes = [p for p in range(3, upper_limit//2, 2) if is_prime[p]]

out = []
for n in num_list:
    found = False
    for p in primes:
        if is_prime[p] and is_prime[n-p]:
            print(f"{n} = {p} + {n-p}")
            break

explain = """
소수를 구하는 알고리즘인 에라스토네체를 최대한 속도 측면에서 빠르게 하는 것이 중요했던 문제.
범위 내 소수만 구한다면 그 외 나머지는 브루트 포스를 통해 찾을 수 있다.
"""