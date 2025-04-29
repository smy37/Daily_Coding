import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
stop_road = {}

for _ in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split())
    stopped = sorted([[a,b], [c,d]], key = lambda x : [x[0], x[1]])
    stop_road[(stopped[0][1], stopped[0][0], stopped[1][1], stopped[1][0])] = True

move_l = [[0, 1], [1, 0]]
dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
s = deque()
s.append([0,0])
dp[0][0] = 1
visited = {}
while s:
    t = s.popleft()
    for i in range(2):
        nx, ny = t[0] + move_l[i][0], t[1] + move_l[i][1]

        if 0<= nx <= M and 0<= ny <= N:
            if (t[0], t[1], nx, ny) not in stop_road:
                if (nx, ny) not in visited:
                    s.append([nx, ny])
                    visited[(nx, ny)] = True
                dp[nx][ny] += dp[t[0]][t[1]]

print(dp[-1][-1])

## BFS를 사용함으로써 depth 기준으로 잡히는 대각선에 위치한 Node들에 대하여 해당 Node 까지의 누적 경로를 기록할 수 있다. 
## 처음에는 visited를 사용하지 않아서 누적된 값이 한번만 우측과 하단에 적용되는게 아니라 해당 node에 도달하는 경로 수를 곱한 만큼 더해졌다.
## 따라서 queue에는 visited 하지 않은 node만 추가해주고 모든 경로에 대하여 dp를 업데이트 하게되면
## BFS의 성질에 따라서 특정 Node의 모든 경로를 업데이트 한 후에 한번만 다음 경로에 반영해 줄 수 있게 된다.