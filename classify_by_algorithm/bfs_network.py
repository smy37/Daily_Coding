import sys

def solution(n, computers):
    c_graph = {}
    answer = 0
    for i in range(n):
        c_graph[i+1] = []

    for i in range(n):
        for j in range(n):
            if i!=j:
                if computers[i][j] == 1:
                    c_graph[i+1].append(j+1)

    visited = []
    stack = []
    for i in range(n):
        if i+1 not in visited:
            answer +=1
            stack.append(i+1)
            while stack:
                num = stack.pop()
                if num not in visited:
                    visited.append(num)
                    for j in c_graph[num]:
                        if j not in visited:
                            stack.append(j)

    return answer



print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

