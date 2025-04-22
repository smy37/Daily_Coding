from collections import deque


def solution(n, results):
    answer = 0
    graph_w = {}
    graph_l = {}
    graph_score = {}
    for i in range(n):
        graph_w[i + 1] = []
        graph_l[i + 1] = []
        graph_score[i + 1] = 0
    for result in results:
        graph_w[result[0]].append(result[1])
        graph_l[result[1]].append(result[0])

    for node in range(1, n + 1):
        cnt = 0
        visited = []
        stack = deque()
        stack.append(node)
        while stack:
            start = stack.pop()
            for t_node in graph_w[start]:
                if t_node not in visited:
                    visited.append(t_node)
                    stack.append(t_node)
                    cnt += 1
        graph_score[node] += cnt
    for node in range(1, n + 1):
        cnt = 0
        visited = []
        stack = deque()
        stack.append(node)
        while stack:
            start = stack.pop()
            for t_node in graph_l[start]:
                if t_node not in visited:
                    visited.append(t_node)
                    stack.append(t_node)
                    cnt += 1
        graph_score[node] += cnt

    for score in graph_score.values():
        if score == n - 1:
            answer += 1

    return answer