import sys
import math
N = int(sys.stdin.readline())
coordinate = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append([x,y])

coordinate.sort(key=lambda x : [x[0], x[1]])
cord_dict = {}

for cord in coordinate:
    x,y = cord
    if x not in cord_dict:
        cord_dict[x] = []
    cord_dict[x].append([y, 0])

keys = list(cord_dict.keys())

for i in range(1, len(keys)):
    k = keys[i]
    pre_k = keys[i-1]
    x_dist = (k-pre_k)**2
    for j in range(len(cord_dict[k])):
        temp_max = 0
        for l in range(len(cord_dict[pre_k])):
            temp_max = max(temp_max, \
            math.sqrt((cord_dict[k][j][0]-cord_dict[pre_k][l][0])**2+x_dist)\
                +cord_dict[pre_k][l][1])
        cord_dict[k][j][1] = temp_max

answer = 0
for t in cord_dict[keys[-1]]:
    answer = max(answer, t[1])

print(answer)


explain = """
좀 더 우아한 효율적인 방법이 있을거 같아서 고민해봤지만 위 방법이 최선인 것 같다.
좌표들을 x 오름차순으로 그리고 y 오름차순으로 정렬 후에 x 좌표를 key로 하는 dictionary를 구성하고
거기에 y좌표와 그동안의 누적 거리를 저장해둔다. x_i에 있는 점들에서 x_{i+1}에 있는 점들과 비교하면서
거리가 가장 최장이 되는 값을 x_{i+1}에 저장해 두고 전체 dictionary key에 대해 업데이트를 진행한다.
"""