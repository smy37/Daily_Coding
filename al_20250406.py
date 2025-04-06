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


N, M = map(int, sys.stdin.readline().split())

parent = {i:i for i in range(N)}
answer = {}
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    p_a = find(parent, a)
    p_b = find(parent, b)
    if p_a == p_b:
        print(i+1)
        break
    union(parent, a, b)
else:
    print(0)
