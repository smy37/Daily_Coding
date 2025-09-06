import sys 

N = int(sys.stdin.readline())
graph = {i: {} for i in range(N)}
score = [[float("inf") for _ in range(N)] for _ in range(N)]
while 1:
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break
    graph[a-1][b-1] = True
    graph[b-1][a-1] = True
    score[a-1][b-1] = 1
    score[b-1][a-1] = 1


for k in range(N):
    for i in range(N):
        for j in range(N):
            if score[i][j] > score[i][k]+score[k][j]:
                score[i][j] = score[i][k]+score[k][j]
                

candi = {}
for i in range(N):
    score[i][i] = 1
    i_max = max(score[i])
    if i_max not in candi:
        candi[i_max] = []
    candi[i_max].append(i+1)

cri = min(candi.keys())
print(cri, len(candi[cri]))
for n in sorted(candi[cri]):
    print(n, end=" ")

explain = """
플로이드 워셜 알고리즘을 이용해서 모든 두 노드 사이의 거리를 구해준다. 
단 주의해야 할점은 자기 자신까지의 거리가 알고리즘을 거친후에 2가 되는데 
이를 1로 수정해주고 점수를 계산해줘야 한다.
"""