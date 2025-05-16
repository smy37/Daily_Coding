import sys

N, M = map(int, sys.stdin.readline().split())
dp = {i+1:{} for i in range(N)}
for _ in range(M):
    t = int(sys.stdin.readline())
    del dp[t]

if 2 in dp:
    dp[2][1] = 1
mv = [-1, 0, 1]
for i in range(2, N+1):
    if i in dp:
        for j in dp[i]:
            for k in mv:
                next_x = j+k
                if next_x >0 and i+next_x <= N and i+next_x in dp:
                    if next_x in dp[i+next_x]:
                        dp[i+next_x][next_x] = min(dp[i][j] + 1, dp[i+next_x][next_x])
                    else:
                        dp[i+next_x][next_x] = dp[i][j] + 1

if dp[N]:
    print(min(dp[N].values()))
else:
    print(-1)
    

explain = """
일반적으로 1차원이나 2차원 배열로 저장하던 dp와는 다르게 이중 딕셔너리를 이용하였다. 첫번째 키에는 위치를 두번째 키에는 현재 점프 범위를 저장하였고 
그 값으로는 현재까지 점프한 횟수이다. 이 횟수가 더 많은 횟수로 잘못 갱신될 수 있으므로 min 값일때만 갱신하도록 하였고 2번째 돌이 건널 수 없는 돌인
엣지케이스를 처리하기 위해 if 2 in dp: dp[2][1] = 1 부분을 추가하였다. dp에서 크게 2가지 값을 저장해두면서 현재 값을 기준으로 앞으로의 값을 갱신하는경우와
현재 값을 갱신하기 위해 이전의 값들을 처리하는 방법이 있는데 이번에는 전자의 방법이 사용되었다.
"""