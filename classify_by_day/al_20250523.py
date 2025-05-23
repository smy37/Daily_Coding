import sys 
from collections import deque
import copy

a, b, c = map(int, sys.stdin.readline().split())
water = [a, b, c]
mv = []
for i in range(3):
    for j in range(3):
        if i!=j:
            mv.append([i ,j])

dq = deque()
dq.append([0,0,c])
visited = {(0,0,c): 1}
answer = set()
answer.add(c)

while dq:
    tt = dq.popleft()
    for i in range(6):
        t = copy.deepcopy(tt)
        s, d = mv[i]
        if t[s] != 0 and t[d] < water[d]:
            s_can = max(0, t[s]-(water[d]-t[d]))
            d_can = min(water[d], t[d]+t[s])
            
            t[s] = s_can
            t[d] = d_can
            
            if tuple(t) not in visited:
                visited[tuple(t)] = 1
                dq.append(t)
                if t[0] == 0:
                    answer.add(t[2])

for i in sorted(answer):
    
    print(i, end=' ')

explain = """
경우의 수를 세기 위해 수형도를 그려가는 과정도 어떻게 보면 트리이고 트리는 그래프의 일종이기 때문에 DFS 또는 BFS가 가능하다.
보통은 격자에서 4방향의 움직임으로 그래프를 탐색하는데 이 경우에는 특정 물통에서 특정 물통으로 옮기는 총 6개의 경우의 수가 가능하고
이중에서 물을 옮기려는 물통이 비어있지 않고 물이 옮겨지는 물통이 꽉차 있지 않는지를 확인하면 된다. 
그리고 주의해야할 점은 가장 첫번째 물통이 비어있을 경우에 마지막 물통에 물이 차는 경우를 찾아야 한다.
"""