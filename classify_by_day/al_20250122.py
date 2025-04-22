import sys

r, c = map(int, sys.stdin.readline().split())

graph = []
for _ in range(r):
    row = sys.stdin.readline().strip()
    graph.append(row)

move = [[-1, 1], [0, 1], [1, 1]]

visited = [False for _ in range(r*c)]
answer = 0

def dfs(s):
    global answer
    t = s.pop()

    flag = False
    for i in range(len(move)):
        n_y = t[0] + move[i][0]
        n_x = t[1] + move[i][1]
        idx = n_y*c + n_x

        if n_x == c:
            answer +=1
            return True
        if 0<=n_y <r and 0<=n_x<c and graph[n_y][n_x] != "x" and visited[idx] != True:
            visited[idx] = True
            flag = dfs(s + [[n_y, n_x]])
        if flag:
            break
    return flag

for i in range(r):
    s = [[i, 0]]
    dfs(s)

print(answer)