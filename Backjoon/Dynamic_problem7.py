import sys

iter = int(sys.stdin.readline())

score_board = []
for i in range(iter):
    score_board.append([int(sys.stdin.readline()),[],[]])

if len(score_board) == 1:
    print(score_board[0][0])
    sys.exit()
if len(score_board) == 2:
    print(score_board[0][0]+score_board[1][0])
    sys.exit()
score_board[0][2] = [score_board[0][0]]
score_board[1][2] = [score_board[1][0]]


for i in range(iter-2):
    if i !=0:
        score_board[i+2][2].append(max(score_board[i][1])+score_board[i+2][0])
    score_board[i+1][1].append(max(score_board[i][2])+score_board[i+1][0])
    score_board[i+2][2].append(max(score_board[i][2])+score_board[i+2][0])
score_board[iter-1][1].append(max(score_board[iter-2][2]) + score_board[iter-1][0])
score_board[iter-1][2].append(max(score_board[iter-2][2])+score_board[iter-1][0])

a = max(score_board[iter-1][1])
b = max(score_board[iter-1][2])
print(max(a,b))