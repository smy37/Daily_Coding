import sys

T = int(sys.stdin.readline())

num_l = []
for _ in range(T):
    num_l.append(int(sys.stdin.readline()))

max_n = max(num_l)

dp = [[0,0,0] for _ in range(max_n+1)]
dp[1][0], dp[2][1], dp[3][2] = 1, 1, 1

for i in range(max_n+1):
    for j in [1, 2, 3]:
        if i+j <= max_n:
            if j == 1:
                dp[i+j][0] += dp[i][1]
                dp[i+j][0] += dp[i][2]
            elif j == 2:
                dp[i+j][1] += dp[i][0]
                dp[i+j][1] += dp[i][2]
            elif j == 3:
                dp[i+j][2] += dp[i][0]
                dp[i+j][2] += dp[i][1]
    print(dp)
for n in num_l:
    print(max(dp[n]))
        