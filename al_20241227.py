import sys

N = int(sys.stdin.readline())

tree = {i+1 : {} for i in range(N)}
animal_num = {}
dq = [1]
visited = {1:True}

cur = 2
for _ in range(N-1):
    cri, number, connect = sys.stdin.readline().split()
    number = int(number)
    connect = int(connect)

    tree[cur][connect] = 1
    tree[connect][cur] = 1

    animal_num[cur] = number if cri == "S" else -number
    cur +=1

animal_num[1] = 0

answer = 0
def dfs(s, visited):
    result = 0
    node = s.pop()
    for k in tree[node]:
        if k not in visited:
            visited[k] = True
            result = result + dfs(s + [k], visited)
    result += animal_num[node]
    result = max(0, result)
    return result

print(dfs(dq, visited))
