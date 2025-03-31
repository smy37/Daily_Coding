import sys

N = int(sys.stdin.readline())
tree = {}
tree[("root", 0)] = []
for _ in range(N):
    t = list(sys.stdin.readline().split())
    t[0] = int(t[0])
    if ("root."+t[1], 1) not in tree[("root", 0)]:
        tree[("root", 0)].append(("root."+t[1], 1))

    for i in range(t[0]-1):
        s = "root."+".".join(t[1:2+i])
        e = "root."+".".join(t[1:3+i])

        if (s, i+1) not in tree:
            tree[(s,i+1)] = []
        if (e, i+2) not in tree[(s, i+1)]:
            tree[(s, i+1)].append((e, i+2))

for k in tree:
    tree[k] = sorted(tree[k], key= lambda x : [-x[1], x[0]], reverse=True)

s = []
for next_n in tree[("root", 0)]:
    s.append(next_n)

answer = []
while s:
    t = s.pop()
    char_name = t[0].split(".")[-1]
    print("--"*(t[1]-1)+char_name)

    if t in tree:
        for next_n in tree[t]:
            s.append(next_n)
tt = "\n".join(answer)