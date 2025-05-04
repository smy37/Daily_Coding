import sys

N, P, Q = map(int, sys.stdin.readline().split())


## Method 1. 
# dp = {0: 1}
# for i in range(1, N+1):
#     dp[i] = dp[int(i/P)] + dp[int(i/Q)]

# print(dp[N])

## Method 2.
# dp = {0: 1}
# for i in range(1, N+1):
#     dp[i] = dp[int(i/P)] + dp[int(i/Q)]

# print(dp[N])

## Method 3.
dp = {0:1}
def dfs(n):
    if n in dp:
        return dp[n]
    dp[n] = dfs(int(n/P)) + dfs(int(n/Q))
    return dp[n]

print(dfs(N))


### 실제로 최종 풀이된 내용만 보면 간단하지만 메모리 문제, 무한 재귀의 늪에 빠지는 문제등 고려해야 될게 은근히 있었다.
### 처음에는 크기 N+1을 가지는 DP용 리스트를 만들어서 시도하였는데 메모리 문제가 발생하였다. 
### 다음으로는 Dictionary를 사용했는데 마찬가지였다. 이러한 메모리 문제를 줄이는 방식으로 bottom-up이 아닌 top-down으로 
### 필요한 숫자에 대해서만 DP 메모이제이션을 적용하는게 핵심이였다. 그리고 재귀를 사용하는데 if n in dp: return dp[n] 이라는 로직이 추가되지 않으면
### 계속 같은 dfs(0)을 무한히 호출하게 되는 재귀의 늪에 빠지게 된다.