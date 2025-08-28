import sys 

N, M, D = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dp = [[-float("inf") for _ in range(M)] for _ in range(N)]
for i in range(M):
    dp[0][i] = 0
for i in range(N):
    for j in range(M):
        cur = board[i][j]
        for k in range(1, D+1):
            cur_r = i+k
            if 0<=cur_r<N:
                cri = D-k
                for l in range(-cri, cri+1):
                    cur_c = j+l
                    if 0<=cur_c<M:
                        next_v = board[cur_r][cur_c]
                        dp[cur_r][cur_c] = max(dp[cur_r][cur_c], dp[i][j]+cur*next_v)

print(max(dp[-1]))

