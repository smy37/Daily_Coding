import sys

N, K = map(int, sys.stdin.readline().split())

upper_limit = int(K/N) + 1

day_l = list(map(int, sys.stdin.readline().split()))

def cal_cost(X):
    def _cal_sum(n):
        return n * (n + 1) // 2
    global N
    cost = _cal_sum(X)
    for i in range(N-1):
        during = day_l[i+1]-day_l[i]
        temp_cost = _cal_sum(X)
        rest = max(0, X-during)
        temp_cost -= _cal_sum(rest)
        cost += temp_cost

    return cost

left = 1
right = upper_limit
min_X = 0
while left <= right:
    mid = (left+right)//2
    cur_cost = cal_cost(mid)
    if cur_cost >= K:
        min_X = mid
        right = mid-1
    else:
        left = mid+1

print(min_X)

### 정수 X가 주어졌을 때, 해당 X로 벌어들이는 금액을 계산할 수 있는 함수를 만들어놓고
### X를 함수에 넣고 원하는 값보다 크거나 같은지 작은지 판단하면서 이분탐색으로 X를 찾아나가면 된다.
### X가 주어졌을 때, 그리고 날짜들이 주어지므로 X*(X+1)/2 를 통해 1부터 X까지 수의 합을 구할 수 있고 날짜들 간의 간격을 통해서
### 그 날짜 간격동안 벌어들이는 돈을 구할 수 있다. 원하는 K보다 금액이 크거나 같다면 이분탐색에서 right를 줄이는 것으로 변경하고
### K보다 금액이 작다면 left를 변경해서 구해지는 값을 키운다. 이렇게 log(upper_limit)의 시간으로 최소로 만족하는 정수값을 구할 수 있다.
### 이 문제에서 처음에는 시간초과가 발생하였는데 _cal_sum 함수에서 n*(n+1)/2를 n*(n+1)//2로 바꿈으로써 시간초과를 통과할 수 있었다.
### 이러한 상황은 처음이었는데 기억해 두면 좋을 것 같다. /연산보다 //연산이 훨씬 빠른 것을.