import sys
import copy

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    board.append(temp)


### 1. First Try
# dp = {}
# for i in range(N):
#     for j in range(N):
#         temp_dp = [[set() for _ in range(j, N)] for _ in range(i, N)]
#         up_l = set()
#         left_l = set()
#         for k in range(i, N):
#             left_l.add(board[k][j])
#             temp_dp[k-i][0] = copy.deepcopy(left_l)
#         for k in range(j, N):
#             up_l.add(board[i][k])
#             temp_dp[0][k-j] = copy.deepcopy(up_l)
#
#         up_l = set()
#         left_l = set()
#         for a in range(1, N-i):
#             for b in range(1, N-j):
#                 up_x_idx, up_y_idx = a-1, b
#                 left_x_idx, left_y_idx = a, b-1
#
#                 up_l = temp_dp[up_x_idx][up_y_idx]
#                 left_l = temp_dp[left_x_idx][left_y_idx]
#                 new_l = up_l.union(left_l)
#                 new_l.add(board[i+a][j+b])
#                 temp_dp[a][b] = new_l
#
#         score = [[len(temp_dp[x][y]) for y in range(len(temp_dp[0]))] for x in range(len(temp_dp))]
#         dp[(i,j)] = score
#
# Q = int(sys.stdin.readline())
# for _ in range(Q):
#     x1, y1, x2, y2 = [t-1 for t in list(map(int, sys.stdin.readline().split()))]
#     temp_dp = dp[(x1, y1)]
#     print(temp_dp[x2-x1][y2-y1])


### 2. Second Try
dp = {}
for i in range(1, 11):
    dp[i] = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        val = board[i][j]
        dp[val][i+1][j+1] = 1

for val in range(1, 11):
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[val][i][j] += (dp[val][i-1][j]+dp[val][i][j-1]-dp[val][i-1][j-1])

Q = int(sys.stdin.readline())

for _ in range(Q):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    cnt = 0
    for val in range(1, 11):
        temp_dp = dp[val]
        unique_value = temp_dp[x2][y2]-temp_dp[x2][y1-1]-temp_dp[x1-1][y2]+temp_dp[x1-1][y1-1]
        if unique_value >0:
            cnt +=1
    print(cnt)

explain = """
첫번째 시도에서는 N X N 에 해당하는 시작점에 대해서 그 이후 만들 수 있는 모든 부분 수열에 대해 값을 구했다. 
두번째 시도에서는 각 고유한 값의 개수를 누적으로 저장해두고 그 저장된 값을 이용하여 부분 수열에서 고유한
정수의 개수를 구하였다.
핵심은 고유한 정수가 혼재되어 값을 세는 방법에서 고유한 정수마다 개수를 누적하는 누적합 배열을 만들어 사용하는 것이다.
"""