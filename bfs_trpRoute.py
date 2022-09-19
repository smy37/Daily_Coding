tickets = [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
t1 =[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
t2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
r_final = []
def dfs(stack, visited, graph, tickets):
    if len(visited) == len(tickets):
        if [visited[-1], stack[-1]] in tickets:
            r_final.append(visited)
            return
        else:
            return False
    else:
        temp = stack.pop()
        if graph[temp] == []:
            return False
        for i in graph[temp]:
            if [temp, i] in tickets:
                dfs(stack+[i], visited+[temp], graph, tickets)
                print(stack, visited)


def solutions(tickets):
    final = []
    graph = {}
    for i in tickets:
        if i[0] not in graph:
            graph[i[0]] = [i[1]]
            if i[1] not in graph:
                graph[i[1]] = []
        else:
            graph[i[0]].append(i[1])
    for i in graph:
        graph[i] = sorted(graph[i])

    stack = []
    visited = []
    stack.append("ICN")
    final.append(dfs(stack,visited,graph,tickets))
    print(r_final)
    return r_final
solutions(t2)

