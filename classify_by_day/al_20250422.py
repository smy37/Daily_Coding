import sys

N = int(sys.stdin.readline())


## Method 1. O(n^2)의 시간 복잡도를 가지는 브루트 포스 방식.
# data_l = []
# for _ in range(N):
#     x, r = map(int, sys.stdin.readline().split())
#     data_l.append([x, r])
#
# data_l = sorted(data_l, key = lambda x : x[0])
#
# for i in range(len(data_l)):
#     for j in range(i+1, len(data_l)):
#         if data_l[i][0] == data_l[j][0]:
#             if data_l[i][1] == data_l[j][1]:
#                 print("NO")
#                 sys.exit()
#         elif abs(data_l[i][1]-data_l[j][1]) <=data_l[j][0]-data_l[i][0] <= data_l[i][1]+data_l[j][1]:
#             print("NO")
#             sys.exit()
# print("YES")


### Method 2. 기하학적 성질을 이용
data_l = []
for _ in range(N):
    x, r = map(int, sys.stdin.readline().split())
    data_l.append([x-r, x+r])

data_l = sorted(data_l)
s = [data_l[0][1]]

for i in range(1, len(data_l)):
    while s and s[-1] < data_l[i][0]:
        s.pop()
    if s and data_l[i][1] >= s[-1]:
        print("NO")
        sys.exit()
    s.append(data_l[i][1])
print("YES")
### 수평선에서 선분들을 좌측 끝 점을 기준으로 오름 차순으로 정렬 했을때, 왼쪽에 있는 선분의 우측 끝점이 오른쪽에 있는 선분의 좌측 끝점보다 크다면 두 선분은 겹친다.
### 원의 교차를 수평선 위에서의 겹침, 선분의 교차 처럼 생각해야 했음.
### 단, 인접한 두개를 비교한다는 개념보다는 현재까지의 최대값을 저장 해뒀다가 그값을 비교후 갱신하는 방식을 떠올려야함!!