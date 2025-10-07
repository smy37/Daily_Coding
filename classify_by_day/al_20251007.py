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

explain = """
dfs로 각 노드별 최대값을 저장해 두었다가 리프 노드부터 차례로 위로 올리면서 이전 노드의
최대값이 양수일 때만 더하는 식으로 현재 노드의 최대값을 갱신해준다.
주의해야 할점은 루트 노드로부터의 시작의 최대값을 구해야 된다는 것이다. 37번째 줄
"""
