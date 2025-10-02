import sys

sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())

parent = {i+1:-1 for i in range(N)}
tree = {i+1:[-1,-1] for i in range(N)}
for _ in range(N):
    p, l, r = map(int, sys.stdin.readline().split())
    tree[p][0] = l
    tree[p][1] = r
    parent[l] = p
    parent[r] = p

last_node = -1

def mid_search(cur: int):
    global last_node
    l, r = tree[cur]

    if l != -1:
        mid_search(l)
    last_node = cur
    if r != -1:
        mid_search(r)

mid_search(1)

visited = {}
history = []

## First Appraoch
# def search(cur: int):
#     history.append(cur)
#     visited[cur] = 1
#     l, r = tree[cur]

#     if len(visited) == N:
#         print(len(history)-1)
#         sys.exit()

#     if l not in visited and r in visited:
#         if l != -1:
#             search(l)
#             history.append(cur)
#     elif l not in visited and r not in visited:
#         if l != -1:
#             search(l)
#             history.append(cur)
#         if r != -1:
#             search(r)
            
#             history.append(cur)

## Second Approach
def search(cur):
    l, r = tree[cur]
    history.append(cur)
    visited[cur] = 1

    if l != -1 and l not in visited:
        search(l)
        history.append(cur)
    if r != -1 and r not in visited:
        search(r)
        history.append(cur)
    if len(visited.keys()) == N and cur == last_node:
        print(len(history)-1)
        sys.exit()
search(1)

explain = """
처음 시도에서는 유사 중위 순회를 시뮬레이션 하는 방식을 사용했지만 순회의 끝이 아닌 점에서
방문한 횟수가 N에 도달하는 경우가 발생하여 먼저 중위 순회로 순회의 끝을 구하고 방문하 횟수가
N이고 현재 노드가 순회의 끝일 경우에만 history를 출력하는 방식을 채택하였다.
"""