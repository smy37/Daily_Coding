import sys
N = int(sys.stdin.readline())

dp = [1 for _ in range(11)]
dp[0] = 0

if N == 1:
    print(sum(dp))
    sys.exit()

for i in range(N-1):
    for j in range(1,11):
        dp[j] += (dp[j-1]%10007)

result = sum(dp)%10007

print(result)