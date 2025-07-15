import sys

def find(s: str, parent: dict, size):
    if s not in parent:
        return s
    if s != parent[s]:
        parent[s] = find(parent[s] , parent, size)
    return parent[s]

def union(a: str, b: str, parent: dict, size: dict):
    p_a = find(a, parent, size)
    p_b = find(b, parent, size)

    if p_a == p_b:
        return

    if p_a < p_b :
        parent[p_b] = p_a
        size[p_a] += size[p_b]
    else:
        parent[p_a] = p_b
        size[p_b] += size[p_a]

N = int(sys.stdin.readline())
parent = {}
size = {}

for _ in range(N):
    temp = sys.stdin.readline().strip().split()

    if temp[0] == "Q":
        target = find(temp[1], parent, size)
        if target not in size:
            print(1)
        else:
            print(size[target])
    elif temp[0] == "I":
        a, b = temp[1], temp[2]
        if a not in parent:
            parent[a] = a
            size[a] = 1
        if b not in parent:
            parent[b] = b
            size[b] = 1
        union(a, b, parent, size)


explain = """
처음에는 size에 저장하는 방식을 사용하지 않았고 find시에 p=parent[s] 이런식으로 복사가 일어나서 경로 압축이 되지 않아 시간초과가 발생하였다.
현재 집합의 개수를 저장해두는 size를 두고 경로 압축을 시행하였고 몇가지 주의해야 할 점은
union 시 p_a와 p_b가 같은 경우에 대한 처리(size 때문에) 그리고 find시 s가 parent에 없는게 들어올 수 있어서 그것에 대한 처리가 주요했다. 
그리고 전체 개수가 안알려져 있기 때문에 a와 b를 parent에 추가해야했고 그 과정에서 size의 크기를 1로 세팅해주는 과정이 필요했다.
"""