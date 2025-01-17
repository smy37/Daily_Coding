import sys

node_num = int(sys.stdin.readline())
tree = {i+1 : [] for i in range(node_num)}

for _ in range(node_num-1):
    s, e = map(int, sys.stdin.readline().split())
    tree[s].append(e)
    tree[e].append(s)

visited = {1:1}
s = [[1,0]]
answer = 0

while s:
    t = s.pop()

    if t!= 1 and len(tree[t[0]]) == 1:
        answer += t[1]
    for n_n in tree[t[0]]:
        if n_n not in visited:
            visited[n_n] = 1
            s.append([n_n, t[1]+1])

if answer%2 == 0:
    print("No")
else:
    print("Yes")