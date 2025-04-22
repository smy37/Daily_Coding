import sys

N, M, K = map(int, sys.stdin.readline().split())

dp = {i : {} for i in range(1, M+1)}
graph = {i+1 : {} for i in range(N)}
for _ in range(K):
    a, b, w = map(int, sys.stdin.readline().split())
    if a > b:
        continue
    if b in graph[a]:
        graph[a][b] = max(graph[a][b], w)
    else:
        graph[a][b] = w
dp[1][1] = 0
answer = 0
for i in range(1, M):
    for cur in dp[i]:
        for next in graph[cur]:
            weight = graph[cur][next]

            if next not in dp[i+1]:
                dp[i+1][next] = dp[i][cur]+ weight
            else:
                dp[i + 1][next] = max(dp[i+1][next], dp[i][cur] + weight)
            if next == N:
                answer = max(answer, dp[i + 1][next])
print(answer)