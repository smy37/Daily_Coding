import sys

N = int(sys.stdin.readline())
target_l = []

for _ in range(N):
    target_l.append(list(map(int, sys.stdin.readline().split())))

vector_l = []
for i in range(1, len(target_l)):
    vector_l.append([target_l[i][0]-target_l[0][0], target_l[i][1]-target_l[0][1]])

M = int(sys.stdin.readline())
star_dict = {}
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())

    star_dict[(x, y)] = 1

for cord in star_dict:
    x, y = cord

    for vector in vector_l:
        v_x, v_y = vector

        if (x+v_x, y+v_y) not in star_dict:
            break
    else:
        print(x-target_l[0][0], y-target_l[0][1])

explain = """
찾아야 하는 타겟이 점의 좌표 모음일 때, 한 점을 기준으로 다른점으로 이동하는 벡터를 기록해둔다. 
그 후, 실제 점들의 좌표가 주어질 때 한 점에서 이전 단계에서 구한 벡터로 이동한 좌표가 모두 존재한다면
그 점의 좌표와 맨 처음 단계에서 기준으로 잡은 점을 빼준다면 평행 이동해야 하는 x크기, y크기가 구해진다.
"""
