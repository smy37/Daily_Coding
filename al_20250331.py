import sys
import copy

N = int(sys.stdin.readline())

board =[]
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

## 절대값을 풀어준 총 4가지의 경우의 수에 대해 처리, sorting 되면 (a,b)와 (c,d)의 구분은 무의미 해지므로 경우의수가 4개에서 2개로 준다.
plus_board = sorted(copy.deepcopy(board), key = lambda x : x[0]+x[1])
minus_board = sorted(copy.deepcopy(board), key = lambda x : x[0]-x[1])

answer = 0

answer = max(answer, (plus_board[-1][0]+plus_board[-1][1])-(plus_board[0][0]+plus_board[0][1]))
answer = max(answer, (minus_board[-1][0]-minus_board[-1][1])-(minus_board[0][0]-minus_board[0][1]))

print(answer)
