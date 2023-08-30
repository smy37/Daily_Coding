import sys

N = int(sys.stdin.readline())
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

# Method 1. Greedy?! 현재 배열에서 곱이 가장 작은 수를 먼저 곱해간다면 결국에는 가장 적을 것이다?!
# result = 0
# min_idx = -1
# mid_idx2 = -1
# min_sum = 1250000000
# min_sum2 = 2500000
# while len(board)>1:
#     for i in range(len(board)-1):
#         temp_sum = board[i][0]*board[i+1][1]*board[i][1]
#         if temp_sum < min_sum:
#             min_idx = i
#             min_sum = temp_sum
#             min_sum2 = board[i][0]*board[i+1][1]
#         elif temp_sum == min_sum:
#             if  board[i][0]*board[i+1][1] < min_sum2:
#                 min_idx = i
#                 min_sum = temp_sum
#                 min_sum2 = board[i][0]*board[i+1][1]
#     result += board[min_idx][0] * board[min_idx][1] * board[min_idx + 1][1]
#     if min_idx +2 < len(board):
#         board = board[:min_idx] +[[board[min_idx][0], board[min_idx+1][1]]] +board[min_idx+2:]
#     else:
#         board = board[:min_idx] + [[board[min_idx][0], board[min_idx + 1][1]]]
#
#     min_sum = 1250000000
#     min_sum2 = 2500000
# print(result)


# Method 2. Using DP
limit = 1250000000

dp = [[limit for _ in range(N)] for _ in range(N)]
for i in range(N):
    dp[i][i] = 0
for i in range(1, N):
    for j in range(N-i):
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k]+dp[k+1][j+i]+board[j][0]*board[k][1]*board[j+i][1])

print(dp[0][N-1])