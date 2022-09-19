import copy
from collections import deque
n = 9
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

def bfs(start, graph):
    dq = deque([])
    visited = []
    dq.append(start)

    while dq:
        temp = dq.popleft()
        if temp not in visited:
            visited.append(temp)
            for i in graph[temp]:
                if i not in visited:
                    dq.append(i)
    return visited

def solution(n, wires):
    answer = 100000000
    graph = {}
    for i in range(n):
        graph[i+1] = []
    for i in range(len(wires)):
        t_wires = wires[:i] + wires[i+1:]
        t_graph = copy.deepcopy(graph)
        cri_1, cri_2 = wires[i]
        for j in t_wires:
            if j[0] not in t_graph[j[1]]:
                t_graph[j[1]].append(j[0])
            if j[1] not in t_graph[j[0]]:
                t_graph[j[0]].append(j[1])

        s_1 = bfs(cri_1, t_graph)
        s_2 = bfs(cri_2, t_graph)
        answer = min(answer, abs(len(s_1)-len(s_2)))
    print(answer)
    return answer

solution(n, wires)