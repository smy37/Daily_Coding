import sys

### Method 1. 이진 탐색 이용
N = int(sys.stdin.readline())
num_l = []
for _ in range(N):
    num_l.append(int(sys.stdin.readline()))

num_l = sorted(num_l, reverse= True)

sum_l = []
minus_l = []

for i in range(N):
    for j in range(N):
        sum_l.append(num_l[i]+num_l[j])
        minus_l.append([num_l[i]-num_l[j], num_l[i]])

sum_l.sort()
for i in range(N**2):
    temp_ans = minus_l[i][1]
    minus_v = minus_l[i][0]

    left = 0
    right = N**2-1

    while left <= right:
        mid = (left + right)//2
        cri_v = sum_l[mid]

        if minus_v == cri_v:
            print(temp_ans)
            sys.exit()

        if cri_v < minus_v:
            left = mid + 1
        elif cri_v > minus_v:
            right = mid - 1



### 2. Method 2. Set 자료 구조 이용
N = int(sys.stdin.readline())
num_l = []
for _ in range(N):
    num_l.append(int(sys.stdin.readline()))
num_l.sort()
sum_set = {}
for i in range(N):
    for j in range(N):
        sum_set[num_l[i]+num_l[j]] = True

for i in range(N-1, -1, -1):
    for j in range(N):
        if num_l[i]-num_l[j] in sum_set:
            print(num_l[i])
            sys.exit()


### 핵심은 x+y+z = k에서 x+y = k-z로 바꿔줌으로써, O(n^3)에서 O(n^2)으로 시간복잡도를 낮추는데 있다.
### 그 후에 처음에는 이분 탐색 문제라고 생각하여, k-z값이 x+y 리스트에 있는지 이분탐색을 통해서 찾았다.
### 그러나 python dictionary 사용하면 hash로 되어 있어 탐색에 대해서 O(1)의 시간으로 찾을 수 있어 더 빠른 코드 작성이 가능하다.
### 물론 dictionary 대신에 set을 사용해도 된다.(set 역시 hash로 되어 있으므로)
