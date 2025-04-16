import sys

N, M = map(int, sys.stdin.readline().split())

x_cord = []
y_cord = []
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    x_cord.append(x)
    y_cord.append(y)

x_cord = sorted(x_cord)
y_cord = sorted(y_cord)
mid_x = int(len(x_cord)/2)
mid_y = int(len(y_cord)/2)

answer = 0
for i in range(len(x_cord)):
    answer += abs(x_cord[i]-x_cord[mid_x])

for i in range(len(y_cord)):
    answer += abs(y_cord[i]-y_cord[mid_y])

print(answer)

## 맨하탄 거리의 최소값은 중앙값이 되는 원리를 기억하자