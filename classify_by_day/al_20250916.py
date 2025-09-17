import sys

num_list = []

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    num_list.append(n)

upper_limit = max(num_list)
dp = [0]*(upper_limit+1)

for i in range(1, upper_limit//2+1):
    dp[i*2] = 1

prime = {}
for i in range(3, upper_limit+1):
    if dp[i] == 0:
        prime[i] = 1
        for j in range(1, upper_limit//i + 1):
            dp[i*j] = 1

prime_v = list(prime.keys())
for n in num_list:
    for i in range(len(prime_v)-1, 0, -1):
        p = prime_v[i]
        if n-p in prime:
            print(f"{n} = {n-p} + {p}")
            break