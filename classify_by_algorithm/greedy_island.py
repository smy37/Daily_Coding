num = 11
test = [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]

def solution(n, costs):
    answer = 0
    costs = sorted(costs, key = lambda x : x[2])
    parent_node = {}
    for i in range(n):
        parent_node[i] = i

    for i in costs:
        max_v = max(i[0], i[1])
        min_v = min(i[0], i[1])
        if parent_node[min_v] < parent_node[max_v]:

            answer += i[2]
            cri = parent_node[max_v]
            for j in parent_node:
                if parent_node[j] == cri:
                    parent_node[j] = parent_node[min_v]
        elif parent_node[min_v] > parent_node[max_v]:

            answer += i[2]
            cri = parent_node[min_v]
            for j in parent_node:
                if parent_node[j] == cri:
                    parent_node[j] = parent_node[max_v]

    print(answer)

    return answer

solution(num, test)