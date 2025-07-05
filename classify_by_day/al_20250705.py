import sys 

def find(cur, parent):
    if cur != parent[cur]:
        parent[cur] = find(parent[cur], parent)
    return parent[cur]

def union(a, b, parent):
    parent_a = find(a, parent)
    parent_b = find(b, parent)

    if parent_a <= parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cord_l = []
    for i in range(N):
        x,y,r = map(int, sys.stdin.readline().split())
        cord_l.append([x,y,r])

    parent = [i for i in range(len(cord_l))]
    
    for i in range(len(cord_l)):
        x1,y1,r1 = cord_l[i]
        for j in range(i+1, len(cord_l)):
            x2,y2,r2 = cord_l[j]

            if (x1-x2)**2+(y1-y2)**2 <= (r1+r2)**2 :
                union(i, j, parent)
    answer = {}
    for i in parent:
        p = find(i, parent)
        answer[p] = 1
    print(len(answer))


explain = """
O(n^2)으로 좌표를 비교해도 통과를 할 수 있을까 의문이었지만 pypy3로 제출시 통과 가능하였다.
union-find를 이용해서 겹치는 원들을 그룹화 하였고 주의해야 할점은 union시 
parent 집합에서 바꿔주는건 parent 원소의 값이다. 즉, parent[a] 대신에 parent[parent_a]를 
바꿔줘야 한다.
"""