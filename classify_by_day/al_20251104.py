import sys 
from itertools import combinations

N = int(sys.stdin.readline())
board = []

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)

upper_limit = N//2

answer = float("inf")
for n in range(1, upper_limit+1):
    for comb in combinations(range(N), n):
        t1 = 0
        t2 = 0

        for i in range(len(comb)):
            for j in range(i+1, len(comb)):
                n1, n2 = comb[i], comb[j]
                t1 += (board[n1][n2]+board[n2][n1])

        