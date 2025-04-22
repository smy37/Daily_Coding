import sys
from collections import deque
N = int(sys.stdin.readline())
tree = {}
tree[("root", 0)] = []
for _ in range(N):
    t = list(sys.stdin.readline().split())
    t[0] = int(t[0])
    if (t[1], 1) not in tree[("root", 0)]:
        tree[("root", 0)].append((t[1], 1))
    for i in range(t[0]-1):
        s = t[1+i]
        e = t[2+i]

        if (s, i+1) not in tree:
            tree[(s, i+1)] = []
        tree[(s, i+1)].append((e, i+2))
for k in tree:
    tree[k] = sorted(tree[k], key= lambda x : [-x[1], x[0]], reverse=True)

s = []
for next_n in tree[("root", 0)]:
    s.append(next_n)

answer = ""
while s:
    t = s.pop()
    answer = answer + "--"*(t[1]-1) + t[0] + "\n"
    if t in tree:
        for next_n in tree[t]:
            s.append(next_n)
print(answer)