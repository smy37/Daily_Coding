import sys

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
score = [0 for _ in range(N+1)]

for i in range(len(board)):
    cur = max(score[:i+1])
    score[i+1] = max(score[i+1], cur)
    if board[i][0] + i <= N:
        score[board[i][0]+i] = max(score[board[i][0]+i], cur + board[i][1])

print(score[-1])