import sys 

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    parent_a = find(a, parent)
    parent_b = find(b, parent)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    elif parent_a > parent_b:
        parent[parent_a] = parent_b


N = int(sys.stdin.readline())
parent = [i for i in range(N)]

for _ in range(N-2):
    a, b = map(int, sys.stdin.readline().split())
    union(a-1, b-1, parent)
    
memory = {}
for p in parent:
    memory[find(p, parent)+1] = 1

for p in memory:
    print(p, end = " ")

explain = """
분리 집합을 union-find를 이용하여 구해서 푸는 문제. union-find시 항상 주의해야 할점은
최종 parent 배열에 있는 원소가 좌표 압축이 완벽한게 일어난건 아니라서 parent 원소에 대해서
find를 통해 조상 원소의 값을 구해야 한다.
"""