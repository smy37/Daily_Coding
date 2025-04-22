from collections import deque
def solution(n, edge):
    answer = 0
    node_list = {}
    node_length = {}
    node_num = {}
    for i in range(n):
        node_list[i+1] = []
        node_length[i+1] = n+1
        node_num[i+1] = 0
    node_length[1] = 0
    for edg in edge:
        if edg[1] not in node_list[edg[0]]:
            node_list[edg[0]].append(edg[1])
        if edg[0] not in node_list[edg[1]]:
            node_list[edg[1]].append(edg[0])

    # visited =[]
    stack = deque()
    stack.append(1)
    cur = 0
    while stack:
        start = stack.popleft()
        for node in node_list[start]:
            if node_length[node]==n+1:
                stack.append(node)
                # visited.append(node)
                if node_length[node]>node_length[start]+1:
                    node_length[node] = node_length[start]+1
                    node_num[node_length[start]+1] +=1
    final = 0
    for i in range(n-1,0, -1):
        if node_num[i] >0:
            final = node_num[i]
            break
    return final