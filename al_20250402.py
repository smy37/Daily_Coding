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
            return True
        return False

    t = cross(qp, s)/ denom
    u = cross(qp, r)/ denom

    return 0<=t<=1 and 0<=u<=1



N = int(sys.stdin.readline())

node_l = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    node_l.append([[x1,y1], [x2,y2]])

line_group = {i:-1 for i in range(N)}
cur = 1
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if intersect(node_l[i][0], node_l[i][1], node_l[j][0], node_l[j][1]):
            if line_group[i] == -1 and line_group[j] == -1:
                line_group[i] = cur
                line_group[j] = cur
                cur += 1
            elif line_group[i] == -1:
                line_group[i] = line_group[j]
            elif line_group[j] == -1:
                line_group[j] = line_group[i]
answer = {}
for k in line_group:
    if line_group[k] not in answer:
        answer[line_group[k]] = 0
    answer[line_group[k]] += 1

print(len(answer))
print(max(answer.values()))