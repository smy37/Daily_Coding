import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cord_l = []

    ori_x, ori_y = map(int, sys.stdin.readline().split())
    cord_l.append([ori_x, ori_y])
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        cord_l.append([x, y])

    target_x, target_y = map(int, sys.stdin.readline().split())
    cord_l.append([target_x, target_y])

    graph = {i:{} for i in range(N+2)}

    for i in range(len(cord_l)):
        for j in range(len(cord_l)):
            if abs(cord_l[i][0]-cord_l[j][0]) + abs(cord_l[i][1]-cord_l[j][1]) <= 1000:
                graph[i][j] = True
                graph[j][i] = True

    
    dq = deque()
    dq.append(0)
    visit = {0: True}
    flag = False
    while dq:
        cur = dq.popleft()
        if cur == N+1:
            flag = True
            break
        
        for n in graph[cur]:
            if n not in visit:
                visit[n] = True
                dq.append(n)

    if flag:
        print("happy")
    else:
        print("sad")

explain = """
좌표들을 리스트에 담고 맨하탄 거리가 1000이하인 좌표들은 이어줌으로써 그래프를 구성한다.
0에서 시작해서 N+1번 노드에 접근할 수 있는지 BFS로 판별한다. 
"""