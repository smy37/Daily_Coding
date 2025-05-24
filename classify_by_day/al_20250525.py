import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

### 1. Graph Search to create True Joint
# true_p = {i:True for i in list(map(int, sys.stdin.readline().split()))[1:]}
# graph = {}
# party_l = []
# for _ in range(M):
#     party_p = list(map(int, sys.stdin.readline().split()))[1:]
#     for i in range(len(party_p)):
#         for j in range(i+1, len(party_p)):
#             if party_p[i] not in graph:
#                 graph[party_p[i]] = {}
#             graph[party_p[i]][party_p[j]] = True
#             if party_p[j] not in graph:
#                 graph[party_p[j]] = {}
#             graph[party_p[j]][party_p[i]] = True
#     party_l.append({people: True for people in party_p})

# visited = {}
# for s in true_p:
#     if s not in visited:
#         visited[s] = True
#         dq = deque()
#         dq.append(s)

#         while dq:
#             t = dq.popleft()
#             if t in graph:
#                 for n in graph[t]:
#                     if n not in visited:
#                         visited[n] = True
#                         dq.append(n)

# answer = 0
# for party in party_l:
#     for people in party:
#         if people in visited:
#             break
#     else:
#         answer += 1

# print(answer)


### 2. Union-Find to create True Joint
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a <= parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

parent = [i for i in range(N+1)]
true_p = list(map(int, sys.stdin.readline().split()))
if len(true_p)>=2:
    true_p = true_p[1:]

for people in true_p:
    parent[people] = true_p[0]

party_l = []

for _ in range(M):
    temp_party = list(map(int, sys.stdin.readline().split()))[1:]
    if len(temp_party) >= 2:
        temp_parent = find(temp_party[0])
        for i in range(1, len(temp_party)):
            union(temp_party[0], temp_party[i])
    party_l.append(temp_party)

true_parent = find(true_p[0])

answer = 0
for party in party_l:
    for people in party:
        parent_people = find(people)
        if parent_people == true_parent:
            break
    else:
        answer += 1

print(answer)


explain= """
일단, 진실을 알고 있는 사람들과 그 사람들과 같은 파티에 참석한 적이 있는 사람들이 묶인 집합을 만들어야 한다. 
그 이후에, 파티 리스트를 한번 더 돌면서 해당 집합에 속하는 사람이 없는 파티가 있다면 그 파티를 카운트 해주면된다. 
이러한 진실을 알고 있는 사람들과 파티에 참여한적이 있는 사람들의 집합을 만들기 위해서는 그래프 알고리즘 또는 Union-Find를 적용해주면 된다.
"""