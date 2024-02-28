def solution(n, computers):
    answer = 0
    graph = {}
    for i in range(len(computers)):
        graph[i] = {}
        for j in range(len(computers[i])):
            if computers[i][j] == 1:
                graph[i][j] = 1
            else:
                graph[i][j] = 0
    checker = [i for i in range(n)]
    visited = {i :0 for i in range(n)}
    s = []
    while len(checker):
        t = checker[0]
        s.append(t)
        visited[t] =1
        checker.remove(t)
        while s:
            tt = s.pop()
            for i in graph[tt].keys():
                if visited[i] == 0 and graph[tt][i] == 1:
                    s.append(i)
                    visited[i] = 1
                    checker.remove(i)

        answer +=1
    return answer

if __name__ == "__main__":
    com = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    n = 3
    print(solution(n, com))