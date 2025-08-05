import sys
from itertools import combinations

N = int(sys.stdin.readline())
cord_list = []
answer = 0
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    cord_list.append([x,y])

for comb in combinations(range(N), 3):
    x1, y1 = cord_list[comb[0]]
    x2, y2 = cord_list[comb[1]]
    x3, y3 = cord_list[comb[2]]
    d1 = (x1-x2)**2 + (y1-y2)**2
    d2 = (x2-x3)**2 + (y2-y3)**2
    d3 = (x1-x3)**2 + (y1-y3)**2

    if 2*max(d1,d2,d3) == d1+d2+d3:
        answer += 1

print(answer)