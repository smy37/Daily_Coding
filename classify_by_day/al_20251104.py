import sys 
from itertools import combinations

N = int(sys.stdin.readline())
board = []

for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)
pair= {}
for i in range(N):
    for j in range(i+1, N):
        pair[(i, j)] = board[i][j] + board[j][i]

upper_limit = N//2

answer = float("inf")
for n in range(1, upper_limit+1):
    for comb in combinations(range(N), n):
        t1 = 0
        t2 = 0

        for i in range(len(comb)):
            for j in range(i+1, len(comb)):
                n1, n2 = comb[i], comb[j]
                t1 += pair[(n1, n2)]

        rest = [i for i in range(N) if i not in set(comb)]

        for i in range(len(rest)):
            for j in range(i+1, len(rest)):
                n1, n2 = rest[i], rest[j]
                t2 += pair[(n1, n2)]
        
        answer = min(answer, abs(t1-t2))


print(answer)

explain = """
팀을 나누는 것을 combination을 통해서 수행하였다. 단, 1팀은 0 2팀은 1로 표지해서
DFS를 통해 팀의 경우의 수를 조회하는 방법도 존재한다.
"""