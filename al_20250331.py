import sys
import copy

N = int(sys.stdin.readline())

board =[]
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

plus_board = sorted(copy.deepcopy(board), key = lambda x : x[0]+x[1])
minus_board = sorted(copy.deepcopy(board), key = lambda x : x[0]-x[1])

answer = 0

answer = max(answer, (plus_board[-1][0]+plus_board[-1][1])-(plus_board[0][0]+plus_board[0][1]))
answer = max(answer, (minus_board[-1][0]-minus_board[-1][1])-(minus_board[0][0]-minus_board[0][1]))

print(answer)
