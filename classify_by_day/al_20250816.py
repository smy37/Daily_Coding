import sys
from itertools import combinations

N = int(sys.stdin.readline())
answer = 0
cord_hash = {}
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x not in cord_hash:
        cord_hash[x] = {}
    cord_hash[x][y] = 1

for comb in combinations(cord_hash.keys(), 2):
    for y_comb in combinations(cord_hash[comb[0]], 2):
        y1, y2 = y_comb
        if y1 in cord_hash[comb[1]] and y2 in cord_hash[comb[1]]:
            answer +=1

print(answer)


explain = """
처음에 점들이 들어올 때, x좌표에 따른 y좌표의 값을 해시에 저장해 둔다. 그 후 x좌표들 중 2개를 
combination으로 조합을 가져오고 이 조합의 한 x좌표에 대해 combination으로 y좌표 조합 2개를 가져온다.
그리고 처음에 구성한 해시를 이용해서 이 y좌표 조합 2개의 값이 다른 x좌표에서 존재하는지 판단한다.
"""