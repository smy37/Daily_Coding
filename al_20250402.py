import sys

def cross(v, w):
    return v[0]*w[1]-v[1]*w[0]

def subtract(v, w):
    return (v[0]-w[0], v[1]-w[1])

def intersect(p, p2, q, q2):
    r = subtract(p2, p)
    s = subtract(q2, q)
    qp = subtract(q, p)

    denom = cross(r, s)

    if denom == 0:
        if cross(qp, r) == 0:
            if (max(p[0], p2[0]) >= min(q[0], q2[0]) and max(p[1], p2[1]) >= min(q[1], q2[1]))\
                    and (max(q[0], q2[0]) >= min(p[0], p2[0]) and max(q[1], q2[1]) >= min(p[1], p2[1])):
                return True
        return False

    t = cross(qp, s)/ denom
    u = cross(qp, r)/ denom

    return 0<=t<=1 and 0<=u<=1

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_parent = find(x)
    y_parent = find(y)

    if x_parent <= y_parent:
        parent[y_parent] = x_parent
    else:
        parent[x_parent] = y_parent
N = int(sys.stdin.readline())

node_l = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    node_l.append([[x1,y1], [x2,y2]])

parent = [i for i in range(N)]

line_group = {i:-1 for i in range(N)}
cur = 1
for i in range(N):
    for j in range(i+1, N):
        if intersect(node_l[i][0], node_l[i][1], node_l[j][0], node_l[j][1]):
            union(i, j)

answer = {}
for i in parent:
    root = find(i)
    if root not in answer:
        answer[root] = 0
    answer[root] += 1

print(len(answer))
print(max(answer.values()))
