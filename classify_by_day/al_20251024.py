import sys 

N, S, M = map(int, sys.stdin.readline().split())

volume_list = list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
dp[0][S] = 1

for i in range(1, N+1):
    cur_vol = volume_list[i-1]
    for j in range(M+1):
        if dp[i-1][j] > 0:
            if j+cur_vol <= M:
                dp[i][j+cur_vol] = 1
            if j-cur_vol >= 0:
                dp[i][j-cur_vol] = 1

    if sum(dp[i]) == 0:
        print(-1)
        sys.exit()

for i in range(M, -1, -1):
    if dp[-1][i] >0:
        print(i)
        break

explain = """
키울수 있는 볼륨의 한계 M을 각 N곡에 대하여 메모리로 만들어놓고
순서대로 현재 메모리에서 다음 메모리로 업데이트 할 수 있는 수를 기록해둔다.
"""