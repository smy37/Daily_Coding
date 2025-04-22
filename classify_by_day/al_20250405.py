import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a <= root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = {i+1 : i+1 for i in range(N)}

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            union(parent, i+1, j+1)

result = {}
plan = list(map(int, sys.stdin.readline().split()))
for p in plan:
    root_p = find(parent, p)
    result[root_p] = True

if len(result) == 1:
    print("YES")
else:
    print("NO")