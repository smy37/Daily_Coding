import sys

N = int(sys.stdin.readline())

graph = {}
node_cnt = {}
for _ in range(N):
    temp = sys.stdin.readline().split()
    source = temp[0]
    number = int(temp[1])
    rest = temp[2:2+number]

    if source not in node_cnt:
        node_cnt[source] = len(node_cnt)

    if source not in graph:
        graph[node_cnt[source]] = {}

    for r in rest:
        if r not in node_cnt:
            node_cnt[r] = len(node_cnt)
        graph[node_cnt[source]][node_cnt[r]] = True

target = sys.stdin.readline().strip()
if target not in node_cnt:
    print(1)
    sys.exit()
target_id = node_cnt[target]

node_id = 0
node_id_list = [-1]*len(node_cnt)
finished = [-1]*len(node_cnt)

group = []
stack = []

def tarjan_scc(cur_node):
    global node_id
    low_index = node_id_list[cur_node] = node_id
    node_id += 1
    stack.append(cur_node)

    if cur_node in graph:
        for next_node in graph[cur_node]:
            if node_id_list[next_node] == -1:
                low_index = min(low_index, tarjan_scc(next_node))
            elif finished[next_node] == -1:
                low_index = min(low_index, node_id_list[next_node])

    if low_index == node_id_list[cur_node]:
        mini_group = []
        while stack:
            other_node = stack.pop()
            mini_group.append(other_node)
            finished[other_node] = 1
            if cur_node == other_node:
                break
        group.append(mini_group)

    return low_index

for i in range(len(node_cnt)):
    if finished[i] == -1 :
        tarjan_scc(i)


node_converter = {}

for g in group:
    cri = min(g)
    for n in g:
        node_converter[n] = cri

### First Approach
# def cal_score(cur_node, visit):
#     cur_score = 1
#     for next_node in graph.get(cur_node, {}):
#         if node_converter[next_node] != node_converter[cur_node] and next_node not in visit:
#             visit[next_node] = True
#             temp_score = cal_score(next_node, visit)
#             del visit[next_node]
#             cur_score += temp_score
#     return cur_score
#
# answer = 1
# visit = {target_id: True}
# for next_node in graph.get(target_id, []):
#     if node_converter[next_node] != node_converter[target_id]:
#         temp_score = cal_score(next_node, visit)
#         answer += temp_score
#
# print(answer)

### Second Approach
converted_graph = {}
for cur in graph:
    converted_graph[cur] = {}
    for next in graph[cur]:
        if node_converter[cur] != node_converter[next]:
            converted_graph[cur][next] = True

graph = converted_graph
memory = {i: -1 for i in range(len(node_cnt))}

def cal_score(cur_node):
    if memory[cur_node] != -1:
        return memory[cur_node]
    cur_score = 1
    for next_node in graph.get(cur_node, {}):
        temp_score = cal_score(next_node)
        cur_score += temp_score
    memory[cur_node] = cur_score
    return cur_score




print(cal_score(target_id))



explain = """The first step is to find strongly connected components (SCCs) using Tarjan's algorithm.  

Then, we construct a condensed graph where each SCC is treated as a single node.  
In this graph, edges between nodes within the same SCC are removed.

Initially, I tried to compute the score of each node using backtracking, 
but this approach resulted in a time limit exceeded (TLE).  

Although nodes within the same group can all contribute to the target node, 
backtracking was too slow due to redundant computations.  

By using memoization, we can visit each node only once and accumulate scores efficiently, 
which significantly improves performance compared to backtracking.
"""