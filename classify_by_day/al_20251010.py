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

stack = [[0, 1]]
visited = {0:True}
dp[0][1] = apple_cnt[0]

def dfs(s: list):
    cur_n, node_cnt = s.pop()

    if node_cnt >= k:
        return

    for next_n in tree[cur_n]:
        if next_n not in visited:
            visited[next_n] = True
            next_apple = apple_cnt[next_n]
            for idx in range(1, k+1):
                a_c = dp[cur_n][idx]
                if idx>=k:
                    break
                dp[next_n][idx + 1] = max(dp[next_n][idx + 1], a_c+next_apple)
            dfs(s+[[next_n, node_cnt+1]])
            for idx in range(1, k+1):
                a_c = dp[next_n][idx]
                dp[cur_n][idx] = max(dp[cur_n][idx], a_c)


dfs(stack)
print(max(dp[0]))

explain = """
트리에서 특정 노드에 도달 했을 때, 현재 노드를 도달하는데 가능한 소요 노드 개수에 대해서 그 값의 
1을 더한 것으로 다음 노드의 dp를 업데이트 해준다. 그리고 dfs를 한번더 호출하고 그 호출이 끝난다음에 현재
노드의 dp를 다음 노드의 dp를 기반으로 업데이트 해준다. 
단, 이때 첫번째 노드는 무조건 방문해야 하고 그래서 소요 노드가 0인것은 불가함을 주의해줘야 한다. 
"""


