import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(M)] for _ in range(N)]

### 1. First Try
# for i in range(N):
#     for j in range(M):
#         left_s = j-1
#         up_s = i-1
#         cri_l = 0
#         cri_u = 0
#         if left_s >=0 and dp[i][left_s] !=0:
#             cri_l = dp[i][left_s]-1
#         if up_s >= 0 and dp[up_s][j] != 0:
#             cri_u = dp[up_s][j]-1
#
#         n = max(cri_l, cri_u)
#         while 1:
#             flag = True
#             if i+n < N and j+n < M:
#                 for add_x in range(n+1):
#                     if board[i+add_x][j+n] != 0:
#                         flag = False
#                         break
#                 if flag:
#                     for add_y in range(n):
#                         if board[i+n][j+add_y] != 0:
#                             flag = False
#                             break
#             else:
#                 break
#             if flag:
#                 n += 1
#             else:
#                 break
#
#         dp[i][j] = n
#
# answer = 0
#
# for i in dp:
#     answer = max(answer, max(i))
#
# print(answer)


### 2. Second Try
for i in range(N):
    if board[i][0] == 0:
        dp[i][0] = 1
for i in range(M):
    if board[0][i] == 0:
        dp[0][i] = 1

for i in range(1, N):
    for j in range(1, M):
        if board[i][j] == 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

answer = 0
for i in dp:
    answer = max(answer, max(i))
print(answer)

explain = """
첫번째 시도에서는 좌상단을 기준으로 우측 하단으로 그릴수 있는 최대 크기를 저장하여 특정 지점에서 그릴 수 있는 크기를 판별할 때, 
좌측과 상단의 있는 점에서 얻은 길이를 이용 하였다. 얻은 길이를 기준으로 우측과 하단의 지점들을 검토 해준 후, 크기를 갱신하였다.
그러나 이러한 방법은 시간 복잡도가 효율적이지 못하였고 우측 하단을 기준으로 좌측 상단 방향으로 정사각형을 그렸을때의 최대 길이를
저장하는 방식으로 두번째 시도를 하였다. 두번째 시도의 핵심은 특정 지점에서 좌측 상단으로 그릴 수 있는 정사각형의 최대 크기는 
특정 지점을 기준으로 상단, 좌측, 그리고 대각선 방향으로 하나 떨어진 좌측-상단에서 그릴 수 있는 정사각형의 크기들 중 
가장 작은 크기 +1 이 된다는 것이다. 
두 방법의 공통점은 특정 지점을 기준으로 O(x*y) 만큼 탐색을 해야 되는 것을 미리 저장 해둔 값(최대 길이)을 이용해서 시간을 줄이는 것이다.
차이점은 첫번째 시도는 좌측 상단을 기준으로 두번째 방법은 우측 하단을 기준으로 그릴 수 있는 사각형을 생각한 것이다.
"""