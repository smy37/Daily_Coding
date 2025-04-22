tickets = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"]]
t1 =[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
t2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]



r_final = []
def dfs(stack, visited, graph, tickets, cri):
    if len(visited) == cri:
        if tickets==[]:
            visited.append(stack[-1])
            r_final.append(visited)
            return r_final
        else:
            return False
    else:
        temp = stack.pop()
        if graph[temp] == []:
            return False
        for i in graph[temp]:
            if [temp, i] in tickets:
                idx = tickets.index([temp, i])
                dfs(stack+[i], visited+[temp], graph, tickets[:idx]+tickets[idx+1:], cri)



def solutions(tickets):
    global r_final
    graph = {}
    for i in tickets:
        if i[0] not in graph:
            graph[i[0]] = [i[1]]
            if i[1] not in graph:
                graph[i[1]] = []
        else:
            if i[1] not in graph:
                graph[i[1]] = []
            graph[i[0]].append(i[1])
    for i in graph:
        graph[i] = sorted(graph[i])
    print(graph)
    cri = len(tickets)
    stack = []
    visited = []
    stack.append("ICN")
    dfs(stack,visited,graph,tickets, cri)
    r_final = sorted(r_final)
    print(r_final[0])
    return r_final[0]
solutions(tickets)

