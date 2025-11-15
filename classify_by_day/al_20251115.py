import sys

N = int(sys.stdin.readline())

window_dependency = {i: [] for i in range(N)}
exit_l = []
for i in range(N):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    exit_x, exit_y = r1, c2


    for j in range(len(exit_l)):
        r, c = exit_l[j]

        if r1 <= r <= r2 and c1 <= c <= c2:
            window_dependency[j].append(i)
    exit_l.append([exit_x, exit_y])

answer = 0
s = [0]
visited = {0: True}
def dfs(stack, visit):
    cur = stack.pop()

    for n in window_dependency[cur]:
        if n not in visit:
            visit[n] = True
            stack.append(n)
            dfs(stack, visit)
dfs(s, visited)

print(len(visited))