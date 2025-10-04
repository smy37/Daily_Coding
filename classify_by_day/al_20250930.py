import sys
from collections import deque

N = int(sys.stdin.readline())
color = list(map(int, sys.stdin.readline().split()))

tree = {}

for _ in range(N-1):
    p, c = map(int, sys.stdin.readline().split())

    if p not in tree:
        tree[p] = {}
    if c not in tree:
        tree[c] = {}

    tree[p][c] = True
    tree[c][p] = True


s = deque()
answer = 0
if color[0]!= 0:
    answer += 1
s.append([1,color[0]])
visited = {1: True}

while s:
    cur_n, cur_color = s.popleft()
    if cur_n in tree:
        for next_n in tree[cur_n]:
            if next_n not in visited:
                next_color = color[next_n-1]
                if cur_color != next_color:
                    answer += 1
                visited[next_n] = True
                s.append([next_n, next_color])

print(answer)

explain = """
트리를 순회하는 방법은 bfs 또는 dfs로 가능하다. 위에서부터 이전의 색과 다른 개수를 bfs로 세주면 된다.
단, 첫번째 루트 노드가 흰색이 아닐 경우에 대해 예외 처리를 해줘야 한다.
"""