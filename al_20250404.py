import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a <= root_b:
        parent[root_b] = root_a
    elif root_a > root_b:
        parent[root_a] = root_b


n, m = map(int, sys.stdin.readline().split())

parent = {i: i for i in range(n+1)}

for _ in range(m):
    cmd, a, b = map(int, sys.stdin.readline().split())
    if cmd == 0:
        union(a, b)
    elif cmd == 1:
        ra = find(a)
        rb = find(b)

        if ra == rb:
            print("YES")
        else:
            print("NO")



