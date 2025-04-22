import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

total = []
start_tomato = []
flag = True
for i in range(H):
    box = []
    for j in range(N):
        t = list(map(int, sys.stdin.readline().split()))
        box.append(t)
        for k in range(len(t)):
            if t[k] == 1:
                start_tomato.append((i,j,k))
            elif t[k] == 0:
                flag = False
    total.append(box)
if flag:
    print(0)
    sys.exit()
def checkTomato(t_box):
    for h in range(len(t_box)):
        for n in range(len(t_box[h])):
            for m in range(len(t_box[h][n])):
                if t_box[h][n][m] == 0:
                    return False
    return True

def MaxTomato(t_box):
    ans = 0
    for h in range(len(t_box)):
        for n in range(len(t_box[h])):
            ans = max(ans, max(t_box[h][n]))
    return ans

dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]



dq = deque()
visited = {}
for s_t in start_tomato:
    dq.append([s_t, 0])
    visited[s_t] = 1

while dq:
    temp = dq.popleft()
    cur_h, cur_n, cur_m = temp[0]
    dist = temp[1]

    for i in range(6):
        n_m = cur_m + dx[i]
        n_n = cur_n + dy[i]
        n_h = cur_h + dz[i]

        if 0<=n_m < M and 0<=n_n < N and 0<=n_h < H and total[n_h][n_n][n_m]!= -1:
            if total[n_h][n_n][n_m] == 0:
                total[n_h][n_n][n_m] = dist+1
                dq.append([(n_h,n_n,n_m), dist+1])
            else:
                if total[n_h][n_n][n_m] > dist+1:
                    total[n_h][n_n][n_m] = dist + 1
                    dq.append([(n_h, n_n, n_m), dist + 1])

if checkTomato(total):
    answer = MaxTomato(total)
    print(answer)
else:
    print(-1)