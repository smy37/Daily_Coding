import sys
import math

x1, y1, z1, x2, y2, z2 = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
rod = list(map(int, sys.stdin.readline().split()))

### 1. First Try
# cri_length = abs(x1-x2) + abs(y1-y2) + abs(z1-z2)
# rod.sort(reverse=True)
#
# total = 0
# for n in rod:
#     if total - cri_length <=0:
#         total += n
#     else:
#         total -= n
#
# if total == cri_length:
#     print("YES")
# else:
#     print("NO")

### 2. Second Try
cri_length = math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
rod.sort(reverse=True)

if sum(rod) < cri_length:
    print("NO")
    sys.exit()

if rod[0]-sum(rod[1:]) > cri_length:
    print("NO")
else:
    print("YES")


explain = """
처음에는 양 끝점의 좌표가 모두 정수이고 막대의 길이가 정수여서 맨해튼 거리를 막대로 만들 수 있는지 찾으려고 하였댜.
그러나 두 막대를 연결하는 경우를 생각해보면 두 막대를 일자로 이었을때 길이와 한막대를 한뱡항으로 간후 반대 방향으로 나머지 막대를
이었을때 길이 사이에 있는 모든 길이를 만들 수 있다. 따라서, 막대의 배열이 있을 때, 이 배열의 값을 모두 더한 것이 최대값이 되고
가장 긴 막대 길이에서 나머지 막대 길이를 모두 빼준 것이 최소길이가 된다. 가장 긴 막대 길이가 나머지 막대길이의 합보다 크다면 최소 길이가
그 차만큼이 되고 만약 나머지 막대 길이의 합이 더 커서 차가 음수가 되면 0부터 최대 길이 까지 모든 길이를 이을 수 있다.  
"""