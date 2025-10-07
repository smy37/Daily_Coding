import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

tree = {}
for _ in range(N-1):
    p, c = map(int, sys.stdin.readline().split())
    if p not in tree:
        tree[p] = {}
    tree[p][c] = True

score = list(map(int, sys.stdin.readline().split()))

stack = [0]
visited = {0: True}
node_max_v = [-float("inf") for _ in range(N)]
node_max_v[0] = score[0]


def dfs(s):
    cur_n = s.pop()
    max_value = score[cur_n]
    if cur_n in tree:
        for next_n in tree[cur_n]:
            if next_n not in visited:
                visited[next_n] = True
                value = dfs(s+[next_n])

                if value > 0:
                    max_value += value
    node_max_v[cur_n] = max(node_max_v[cur_n], max_value)
    
    return max_value

dfs(stack)

print(max(node_max_v))


