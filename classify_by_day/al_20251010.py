import sys

n, k = map(int, sys.stdin.readline().split())

tree = {}
for _ in range(n-1):
    p, c = map(int, sys.stdin.readline().split())
    if p not in tree:
        tree[p] = {}
    if c not in tree:
        tree[c] = {}
    tree[p][c] = True
    tree[c][p] = True

dp = {i: [0 for _ in range(k+1)] for i in range(n)}

apple_cnt = list(map(int, sys.stdin.readline().split()))

stack = [[0, 1, apple_cnt[0]]]
visited = {0:True}
dp[0][1] = apple_cnt[0]

def dfs(s: list):
    cur_n, node_cnt, apple_n = s.pop()

    if node_cnt >= k:
        return

    for next_n in tree[cur_n]:
        if next_n not in visited:
            visited[next_n] = True
            next_apple = apple_cnt[next_n]
            dp[next_n][node_cnt+1] = max(dp[next_n][node_cnt+1], apple_n+next_apple)
            dfs(s+[[next_n, node_cnt+1, apple_n+next_apple]])
            for idx, a_c in enumerate(dp[next_apple]):
                dp[cur_n][idx] = max(dp[cur_n][idx], a_c)
dfs(stack)
print(dp)


