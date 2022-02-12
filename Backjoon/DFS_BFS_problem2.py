import sys


computer_num = int(sys.stdin.readline())
start_com = int(sys.stdin.readline())

graph = {}
for i in range(computer_num):
    graph[i+1] = []
for i in range(start_com):
    temp = list(map(int, sys.stdin.readline().strip().split(' ')))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])



visited = [1]
stack = []
def dfs(start_num):
    stack.append(start_num)

    while stack:
        v = stack.pop(0)

        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                dfs(i)

    return visited

print(len(dfs(1))-1)