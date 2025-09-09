import sys

N = int(sys.stdin.readline())
dp = [0]*(N)

num_l = list(map(int, sys.stdin.readline().split()))

for n in num_l:
    if n >=N:
        print(0)
        sys.exit()
    dp[n] += 1

answer = 1

pre_n = dp[0]
cnt = 0
for i in dp:
    if (i == 2 and pre_n != 2) or i>2:
        print(0)
        sys.exit()
    answer *= i
    pre_n = i
    cnt += i
    if cnt == N:
        break

if pre_n == 1:
    answer *= 2

print(answer)