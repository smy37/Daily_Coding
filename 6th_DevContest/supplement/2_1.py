def solution(N, M, Edge):
    answer = 0
    visited = {}
    graph = {i+1:[] for i in range(N)}
    for i in Edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    visited[1] = 0
    s= [1]

    while s:
        t = s.pop()
        for i in graph[t]:
            if i not in visited:
                s.append(i)
                visited[i] = 1
    answer = len(visited)-1
    return answer


print(solution(8, 4, [[1,2],[2,4],[3,5],[5,7]]))