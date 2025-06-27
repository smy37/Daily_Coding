import sys

N, M = map(int, sys.stdin.readline().split())

graph = {"main": {}}
file_l = {}
for _ in range(N+M):
    top_file, down_file, b_folder = sys.stdin.readline().strip().split()
    if b_folder == "0":
        file_l[down_file] = True
    if top_file not in graph:
        graph[top_file] = {}
    if down_file not in graph[top_file]:
        graph[top_file][down_file] = 0
    graph[top_file][down_file] += 1

Q = int(sys.stdin.readline())

for _ in range(Q):
    query = sys.stdin.readline().strip()
    query_folder = query.split("/")
    s = [query_folder[-1]]
    visited = {}

    while s:
        t = s.pop()

        if t in graph:
            for n_f in graph[t]:
                if n_f in file_l:
                    if n_f not in visited:
                        visited[n_f] = 0
                    visited[n_f] += 1
                else:
                    s.append(n_f)

    print(len(visited), sum(visited.values()))

    explain = """
    겹치는 이름의 폴더가 없기 때문에 간선만 dictionary에 저장해두고 그래프 탐색을 사용하면 되었다. 
    만약 폴더가 겹치는 이름이 있다면 트라이 처럼 경로를 기록 해주는 방식이 필요하다. 그리고 이때, 현재는 바로 위 경로만 주어지지만
    같은 이름의 폴더가 존재한다면 전체 경로가 필요하게 된다. 같은 이름의 파일도 세줘야 하므로 일반적으로 visited로 이미 방문한
    노드를 안방문 안하도록 기록하는데 이 문제에서는 방문한 횟수를 기록해둬야 했다. 그리고 트리 형태이므로 한번 방문한 노드를 다시 
    방문할 가능성이 없다.
    """