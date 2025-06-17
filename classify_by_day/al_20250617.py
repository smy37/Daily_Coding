import sys 
from collections import deque

N = int(sys.stdin.readline())
cri = int((N*(N-1)/2))+1
answer = ["a1"]

str_l = []
cnt = {i:0 for i in range(1, N+1)}

for i in range(1, N+1):
    str_l.append(f"a{i}")

graph = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:
            graph[i][j] = 1


s = [i for i in range(N, 0, -1)]

while s:
    if answer == cri -1:
        break
    t = s.pop()

    for i in range(1, N+1):
        if graph[t-1][i-1] == 1 and cnt[i] < N-2:   ## 핵심이 되는 조건문
            cnt[i] += 1
            cnt[t] += 1

            graph[i-1][t-1] = 0
            graph[t-1][i-1] = 0

            s.append(i)

            answer.append(f"a{i}")
            break

answer.append("a1")

for i in answer:
    print(i, end=" ")

explain = """
경로를 찾기 위해 그래프 탐색을 수행해야 한다. 그래프 자체가 사전순으로 생성되었다면 그래프 조회시에 사전순으로 가장 빠른 것부터
가능한지 체크 하기 때문에 자연스럽게 사전순으로 가장 빠른 경로가 나오게 된다. 하나 유의해야 할점은 if 문에 cnt[i] < N-2 라는 조건이 들어가는 것인데
특정 노드를 다음 노드로 추가했을 때, 해당 노드에서 이미 모든 간선에 대해 지나온 점이라면 탐색이 끝나게 된다. 따라서 다음으로 진행하려는 Node가 
해당 노드로 진행 후에도 갈 수 있는 간선이 있을 때만, 해당 노드로 이동한다.
"""