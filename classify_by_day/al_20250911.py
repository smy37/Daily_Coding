import sys 

c, m = map(int, sys.stdin.readline().split())
dp = list(map(int, sys.stdin.readline().split()))
for _ in range(m-1):
    cur_m = list(map(int, sys.stdin.readline().split()))
    for i in range(c):
        for j in range(c-i-1):
            dp[i+j+1] = max(dp[i+j+1], dp[j]+cur_m[i])

print(dp)