import sys

T, W = map(int, sys.stdin.readline().split())
dp = [{i:[0,0] for i in range(W+1)} for _ in range(T+1)]

dp[0][0][0] = 1

for i in range(T):
    cur = int(sys.stdin.readline())
    cur_add = [0,0]
    cur_add[cur-1] = 1
    for move_num in range(W+1):
        if dp[i][move_num][0] > 0:
            dp[i+1][move_num][0] = max(dp[i][move_num][0] + cur_add[0], dp[i+1][move_num][0])
            if move_num < W:
                dp[i+1][move_num+1][1] = max(dp[i][move_num][0] + cur_add[1], dp[i+1][move_num+1][1])

        if dp[i][move_num][1] > 0:
            dp[i+1][move_num][1] = max(dp[i][move_num][1] + cur_add[1], dp[i+1][move_num][1])
            if move_num < W:
                dp[i+1][move_num+1][0] = max(dp[i][move_num][1] + cur_add[0], dp[i+1][move_num+1][0])

answer = 0
for k in dp[-1]:
    answer = max(answer, max(dp[-1][k]))

print(answer-1)

explain = """
각 시간별로 0부터 최대 이동횟수까지 메모리를 만들어놓고 바로 이전 단계에서 기록이 있던 값들을
다음 단계의 메모리에 업데이트 해준다.
"""