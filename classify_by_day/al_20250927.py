import sys

N = int(sys.stdin.readline())

tree = {i+1:[-1,-1] for i in range(N)}
for _ in range(N):
    p, l, r = map(int, sys.stdin.readline().split())
    tree[p][0] = l
    tree[p][1] = r

visited = {}
history = []

def search():
    if len(visited) == N:
        print(len(history))
        sys.exit()
    