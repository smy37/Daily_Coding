import sys

N, S, D = map(int, sys.stdin.readline().split())

tree = {}
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    if a not in tree:
        tree[a] = {}
    if b not in tree:
        tree[b] = {}
    tree[a][b] = True
    tree[b][a] = True

answer = 0
stack = [[S, D]]
visited = {S: True}
def dfs(s):
    global answer
    cur_n, r_d = s.pop()

    if cur_n in tree:
        for next_n in tree[cur_n]:
            if next_n not in visited:
                visited[next_n] = True
                if r_d == 0:
                    answer += 2
                    dfs(s+[[next_n, D]])
                else:
                    dfs(s+[[next_n, r_d-1]])

dfs(stack)
print(answer)




