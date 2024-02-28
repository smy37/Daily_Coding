import sys

N = int(sys.stdin.readline())
if N ==1:
    print(0)
    sys.exit()
dp = [0 for _ in range(N//2)]
dp[0] = 3
if N%2 != 0:
    print(0)
    sys.exit()
cri = N//2
for i in range(1, cri):
    dp[i] = dp[i-1]*3 + 2 + sum(dp[:i-1])*2

print(dp[-1])