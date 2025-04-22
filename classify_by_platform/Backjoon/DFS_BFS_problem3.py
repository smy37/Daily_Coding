import sys

n = int(sys.stdin.readline())


apart_list = []
for i in range(n):
    apart_list.append(sys.stdin.readline().rstrip())

visited = []
stack = []
cnt = 0

def dfs(stack):
    global cnt
    while stack:
        v = stack.pop(0)
        if v not in visited:
            visited.append(v)
            if v[0]+1 <n and apart_list[v[0]+1][v[1]] == '1' and [v[0]+1, v[1]] not in visited:
                stack.append([v[0]+1, v[1]])
                cnt+=1
                dfs(stack)
            if v[0]>0 and apart_list[v[0]-1][v[1]] == '1' and [v[0]-1, v[1]] not in visited:
                stack.append([v[0]-1, v[1]])
                cnt+=1
                dfs(stack)
            if v[1]+1 <n and apart_list[v[0]][v[1]+1] == '1' and [v[0], v[1]+1] not in visited:
                stack.append([v[0], v[1]+1])
                cnt+=1
                dfs(stack)
            if v[1] > 0 and apart_list[v[0]][v[1]-1] == '1' and [v[0], v[1]-1] not in visited:
                stack.append([v[0], v[1]-1])
                cnt+=1
                dfs(stack)

    return

final = []
for i in range(len(apart_list)):
    for j in range(len(apart_list[i])):
        if apart_list[i][j] == '1':
            if [i,j] not in visited:
                temp = 0
                cnt = 0
                stack = []
                stack.append([i,j])
                dfs(stack)
                final.append(cnt+1)
print(len(final))
for i in sorted(final):
    print(i)
