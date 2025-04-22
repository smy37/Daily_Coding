def solution(N, M, Edge):
    visited = {}
    graph = {i+1:[] for i in range(N)}
    for i in Edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    cnt = 0
    for x in range(1,N+1):
        if x not in visited:
            visited[x] = 0
            s= [x]

            while s:
                t = s.pop()
                for i in graph[t]:
                    if i not in visited:
                        s.append(i)
                        visited[i] = 1
            cnt +=1
    return cnt-1