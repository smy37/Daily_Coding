import sys
flag = True
def dfs(stack: list, visited: dict, graph: dict):
    global flag
    cur, p = stack.pop()

    for n_n in graph[cur]:
        if n_n != p:
            if n_n in visited:
                flag = False
                return
            visited[n_n] = 1
            stack.append([n_n, cur])
            dfs(stack, visited, graph)
    return


T = int(sys.stdin.readline())

for _ in range(T):
    flag = True
    stop = False
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())

    graph = {i+1:{} for i in range(N)}
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        if b in graph[a]:
            stop = True
        if a in graph[b]:
            stop = True
        graph[a][b] = 1
        graph[b][a] = 1
    if stop:
        print("graph")
        continue
    stack = [[1,0]]
    visited = {1: True}
    dfs(stack, visited, graph)

    if len(visited) < N:
        print("graph")
    else:
        if flag:
            print("tree")
        else:
            print("graph")


explain = """
DFS를 수행하는데 현재 노드와 이전 부모 노드를 같이 스택에 넣어줘서 현재 노드에서 이동하려는 노드중
이미 방문한 노드인데 부모 노드가 아닌 경우가 있다면 cycle이 발생하는 것이고 그래프를 출력하는 로직.
주의 해야할점은 29번째 줄과 31번째 줄에서 중복된 엣지가 발생할 경우 플래그를 바꾸고 break를 수행하면
TypeError를 발생시키므로 주의해야 한다.
"""