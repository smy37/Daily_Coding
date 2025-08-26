import sys 

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

dp = [0]*N
for i in range(N):
    for j in range(i, -1, -1):
        temp = num_list[j:i+1]
        if j == 0:
            dp[i] = max(dp[i], max(temp)-min(temp))
        else:
            dp[i] = max(dp[i], dp[j-1] + max(temp)-min(temp))

print(dp[-1])

explain = """"
처음 시도에서는 i번째부터 j번째까지 min, max의 차이를 저장해두는 방식의 2차원 dp 접근을 시도하였다.
그러나 전체 배열의 크기가 1일 때, 2일 때, 3일 때, ... 이런식으로 이전 값을 누적해두다가 새로운 값이 들어오면
새로운 값으로 인해 생기는 조합을 빠르게 검토하는 dp 방식이 해답이 되었다.
"""