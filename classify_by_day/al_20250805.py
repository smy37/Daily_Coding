import sys
from itertools import combinations
from math import gcd

N = int(sys.stdin.readline())

# ### 1. First Approach
# cord_list = []
# answer = 0
# for _ in range(N):
#     x, y = map(int, sys.stdin.readline().split())
#     cord_list.append([x,y])
#
# for comb in combinations(range(N), 3):
#     x1, y1 = cord_list[comb[0]]
#     x2, y2 = cord_list[comb[1]]
#     x3, y3 = cord_list[comb[2]]
#     d1 = (x1-x2)**2 + (y1-y2)**2
#     d2 = (x2-x3)**2 + (y2-y3)**2
#     d3 = (x1-x3)**2 + (y1-y3)**2
#
#     if 2*max(d1,d2,d3) == d1+d2+d3:
#         answer += 1
#
# print(answer)
#
# ### 2. Second Approach
# cord_list = []
# answer = 0
# for _ in range(N):
#     x, y = map(int, sys.stdin.readline().split())
#     cord_list.append([x,y])
#
# for i in range(N-2):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             x1, y1 = cord_list[i]
#             x2, y2 = cord_list[j]
#             x3, y3 = cord_list[k]
#             d1 = (x1 - x2) ** 2 + (y1 - y2) ** 2
#             d2 = (x2 - x3) ** 2 + (y2 - y3) ** 2
#             d3 = (x1 - x3) ** 2 + (y1 - y3) ** 2
#
#             if 2 * max(d1, d2, d3) == d1 + d2 + d3:
#                 answer += 1
# print(answer)


### 3. Third Approach
answer = 0
def norm(dx, dy):
    g = gcd(abs(dx), abs(dy))
    dx = dx//g
    dy = dy//g

    if dx < 0 or (dx == 0 and dy < 0 ):
        dx, dy = -dx, -dy

    return dx, dy

cord_list = []
for _ in range(N):
    cord_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    xi, yi = cord_list[i]
    cnt = {}

    for j in range(N):
        if i == j:
            continue
        tdx, tdy = cord_list[j]
        dx = xi - tdx
        dy = yi - tdy
        nx, ny = norm(dx, dy)
        if (nx, ny) not in cnt:
            cnt[(nx,ny)] = 0
        cnt[(nx,ny)] += 1

    for (nx, ny) in cnt:
        ox, oy = -ny, nx
        o = norm(ox, oy)

        if tuple(o) in cnt:
            answer += cnt[tuple(o)]*cnt[(nx, ny)]

answer //= 2

print(answer)


explain = """
두번째 풀이는 pypy로 세번째 풀이는 python과 pypy로 모두 통과 가능하다. 
두번째 풀이에서 보이는 것처럼 combination을 사용하는 것은 for 문을 여러개 연결해서 구현 가능하다.
벡터를 hash에 넣을 수 있도록 단위 벡터로 정규화 하지말고 최대 공약수를 나눠주고(좌표가 정수이므로)
x가 양수이고 x가 0일때는 y가 양수인 벡터로 통일 후에 수직인 벡터를 구해서 해당 벡터가 hash에 있는지 
판단하는 식으로 시간을 줄일 수 있다.  
"""