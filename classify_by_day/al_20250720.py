import sys

N, M = map(int, sys.stdin.readline().split())
dp = [[[float("inf"),float("inf"),float("inf")] for _ in range(M)] for _ in range(N)]
temp = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    dp[0][i][0] = temp[i]
    dp[0][i][1] = temp[i]
    dp[0][i][2] = temp[i]

for i in range(1, N):
    
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if j != 0:
            dp[i][j][2] = min(dp[i][j][2], \
                             min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + temp[j])
        if j != M-1:
            dp[i][j][0] = min(dp[i][j][0], \
                             min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + temp[j])

        dp[i][j][1] = min(dp[i][j][1], \
                             min(dp[i-1][j][0], dp[i-1][j][2]) + temp[j]) 

answer = float("inf")
for i in dp[-1]:
    answer = min(answer, min(i))
print(answer)

explain= """
dp를 이용했던 문제, 다만 3중첩 리스트이다 보니 인덱스 처리가 헷갈리는 부분이 있었다.
i번재 행에 대하여 i번째 행의 j번째 열을 만들기 위한 3가지 방법을 이전 행에서 값을 가져와 
업데이트 해주면 된다.
"""