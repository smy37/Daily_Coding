import sys

T = int(sys.stdin.readline())

num_l = []
for _ in range(T):
    num_l.append(int(sys.stdin.readline()))

max_n = max(num_l)
cri = 1000000009

dp = [[0,0,0] for _ in range(max_n+1)]
dp[1][0], dp[2][1], dp[3][2] = 1, 1, 1

for i in range(1, max_n+1):
    for j in [1, 2, 3]:
        if i+j <= max_n:
            if j == 1:
                dp[i+j][0] += dp[i][1]%cri
                dp[i+j][0] += dp[i][2]%cri
            elif j == 2:
                dp[i+j][1] += dp[i][0]%cri
                dp[i+j][1] += dp[i][2]%cri
            elif j == 3:
                dp[i+j][2] += dp[i][0]%cri
                dp[i+j][2] += dp[i][1]%cri
        
for n in num_l:
    print(sum(dp[n])%cri)

explain = """
특정수를 만드는 경우의 수에 대하여 이전에 1을 사용하였는지 2를 사용하였는지 3을 사용하였는지
나눠서 기록해둔다.
"""