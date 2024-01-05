def solution(N, E, M, Q):
    answer = []
    graph = {i+1 : [] for i in range(N)}
    s = []
    for i in range(len(E)):
        graph[E[i][0]].append(E[i][1])
        graph[E[i][1]].append(E[i][0])
    s.append(1)
    parent = {}
    while s:
        t = s.pop()
        for i in graph[t]:
            if i not in parent:
                parent[i] = t
                s.append(i)

    for i in range(len(Q)):
        answer.append(parent[Q[i]])
    return answer

print(solution(4,[[1,2],[2,3],[1,4]],3,[2,4,3]))
print(solution(8,[[2,5],[4,1],[4,7],[1,2],[2,3],[6,3],[3,8]],7\
               ,[2,3,4,5,6,7,8]))