import sys 

cri = 1000000007
T = int(sys.stdin.readline())
max_n = 0
n_l = []
for _ in range(T):
    N = int(sys.stdin.readline())
    max_n = max(max_n, N)
    n_l.append(N)

dp = [[0,0] for _ in range(max_n)]
dp[0][0] = 3
dp[0][1] = 4

for i in range(1, max_n):
    left_n = dp[i-1][0]*2 + sum(dp[i-1])
    right_n = dp[i-1][0]*2 + sum(dp[i-1])*2
    dp[i][0] = left_n%cri
    dp[i][1] = right_n%cri

for n in n_l:
    print(sum(dp[n-1])%cri)

explain = """
N이 커질수록 이전 모양을 기반으로 새로운 모양이 추가되는데 마지막 조각이 1x1 정사각형인 경우와 2x1 직사각형의
일부인 경우 2가지로 나누어 기록해두었다가 업데이트 한다. 이전 단계에서 1x1 정사각형의 경우 곱하기 2 개수만큼 
마지막 조각이 1x1인 정사각형과 곱하기 2 개수만큼 마지막 조각이 2x1인 직사각형이 된다. 또한 이전 단계의 전체 개수는
곱하기 1 만큼 마지막 조각이 1x1인 정사각형이 되고 곱하기 2만큼 마지막 조각이 2x1인 직사각형이 된다.
"""

