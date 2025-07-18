import sys

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent, size:dict):
    p_a = find(a, parent)
    p_b = find(b, parent)
    if p_a == p_b:
        return size[p_a]
    if p_a < p_b:
        parent[p_b] = p_a
        size[p_a] += size[p_b]
        return size[p_a]
    elif p_a > p_b:
        parent[p_a] = p_b
        size[p_b] += size[p_a]
        return size[p_b]

N, M = map(int, sys.stdin.readline().split())
num_dict = {}
parent = {i+1 : i+1 for i in range(N)}
for i in range(N):
    num_dict[i+1] = int(sys.stdin.readline())

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    check = union(a,b,parent, num_dict)
    print(check)

explain = """
연결이 가능한 행성한 하나의 집합으로 만드는데 단계별로 연결관계가 주어지므로
유니온 파인드를 이용해서 단계별로 집합을 구성한다. 이때, 행성들의 합을 기록해두는
num_dict를 따로 만들어놓고 여기에 union이 될때마다 크기를 업데이트 해준다.
"""