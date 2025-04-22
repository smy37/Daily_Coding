### 주요사항...!
### 첫번째 시도에서 자료구조로 Dictionary를 사용하였는데 데이터의 개수가 많아지면
# Hash가 복잡해져 List보다 접근 속도가 느릴 수 있다는 점 때문에 시간초과가 발생하였다!
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split(' '))

arr = []
dp = [[[0,0] for _ in range(m)] for _ in range(n)]
for i in range(n):
    arr.append(sys.stdin.readline().strip())

dp[0][0][0] = 1

dq = deque()
dq.append((0,0))


m_x = [-1,1,0,0]
m_y = [0,0,-1,1]

while dq:
    cur = dq.popleft()
    x, y = cur[0], cur[1]

    for i in range(4):
        n_x = x+m_x[i]
        n_y = y+m_y[i]
        if 0<= n_x < n and 0<= n_y <m:
            if arr[n_x][n_y] == '0':
                if dp[x][y][0] > 0 and dp[n_x][n_y][0] == 0:
                    dp[n_x][n_y][0] = dp[x][y][0] + 1
                    dq.append((n_x, n_y))
                elif dp[x][y][1] > 0 and dp[n_x][n_y][1] == 0:
                    dp[n_x][n_y][1] = dp[x][y][1] + 1
                    dq.append((n_x, n_y))
            elif arr[n_x][n_y] == '1' and dp[x][y][0] > 0 and dp[n_x][n_y][1] == 0:
                dp[n_x][n_y][1] = dp[x][y][0] + 1
                dq.append((n_x, n_y))

if dp[n-1][m-1][0] == 0 and dp[n-1][m-1][1] == 0:
    print(-1)
elif dp[n-1][m-1][0] == 0:
    print(dp[n-1][m-1][1])
elif dp[n-1][m-1][1] == 0:
    print(dp[n-1][m-1][0])
else:
    print(min(dp[n-1][m-1]))

