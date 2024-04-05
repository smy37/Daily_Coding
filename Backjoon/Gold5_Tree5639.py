import sys
from collections import deque

dq = deque()
tree = {}


for i in sys.stdin:
    if i == '\n':
        break
    i = int(i)
    flag = True
    if len(dq) == 0:
        dq.append(i)
        tree[i] = [-1,-1]
    else:
        while flag:
            cur = dq.popleft()
            if cur > i:
                dq.appendleft(cur)
                dq.appendleft(i)
                tree[cur][0] = i
                tree[i] = [-1, -1]
                flag = False
            else:
                if len(dq) == 0:
                    dq.append(i)
                    tree[i] = [-1,-1]
                    tree[cur][1] = i
                    flag = False
                else:
                    if dq[0] > i:
                        tree[cur][1] = i
                        dq.appendleft(i)
                        tree[i] = [-1, -1]
                        flag = False
                    else:
                        continue

root = list(tree.keys())[0]
def back_circuit(node):
    if tree[node][0] != -1:
        back_circuit(tree[node][0])
    if tree[node][1] != -1:
        back_circuit(tree[node][1])
    print(node)

back_circuit(root)
