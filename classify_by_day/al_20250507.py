import sys

def cal_sum(n, a, d):
    return (2*a+(n-1)*d)*n//2

N = int(sys.stdin.readline())

for _ in range(N):
    a, d, x = map(int, sys.stdin.readline().split())
    left = 1
    right = (-2*a+1+((2*a-1)**2+8*x)**0.5)//2 + 1
    floor = -1
    while left <= right:
        mid = (left+right)//2
        temp_sum = cal_sum(mid, a, d)
        if temp_sum >= x:
            floor = mid
            right = mid-1
        else:
            left = mid+1
    if floor == 1:
        print(1, x)
    else:
        print(int(floor), int(x-cal_sum(floor-1, a, d)))

### 층의 경계를 등차수열의 합으로 나오는 값을 기준으로 나올 수 있는 것을 이용하는 문제.
### 층의 값을 바꿔가면서 구하려는 x가 몇층에 속하는지 구한다. 이때, 이분탐색을 통해서 log 시간에 가져올 수 있도록 최적화하고
### 찾은 층을 기준으로 이전층 까지의 합을 구해서 해당 x가 다음 층의 몇번째인지도 구한다.
### 이때, 처음 이분탐색의 우측 상한을 구해줄 때, a에 따라서 d가 1인 경우에 구해지는 층의 높이로 해준다. 아래와 같이
### right = (-2*a+1+((2*a-1)**2+8*x)**0.5)//2 + 1 이 되고 특히 +1을 끝에 해줘야 함을 꼭 명심해야한다.