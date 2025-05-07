import sys

def cal_num(a, N):
    return (a+1)*(N-a+1)

N, K = map(int, sys.stdin.readline().split())

left = 0
right = N//2

while left <= right:
    mid = (left+right)//2
    cur_num = cal_num(mid, N)

    if cur_num == K:
        print("YES")
        sys.exit()

    if cur_num > K:
        right = mid -1
    elif cur_num < K:
        left = mid +1

print("NO")


### 일단 사각형의 변에 평행하게 잘랐을 때, 잘라지는 전체 사격형의 개수를 구하는 식은
### (a+1)*(b+1)임을 생각해야 한다. 이때, a는 가로축으로의 가위질 횟수, b는 세로축으로의 가위질 횟수이다.
### 그리고 a+b=N 이 주어지므로 (a+1)*(N-a+1)이 만들어지는 사각형의 개수임을 알 수 있다.
### N은 1<=N<=2^31-1을 만족하므로 a를 평범하게 for 문을 통해서 찾으면 시간초과가 발생하므로 N//2를 상한으로 하고
### 0을 하한으로 해서 이분탐색을 통해서 a 값을 찾는다. 처음에 a의 하한을 1로 생각했었는데 N의 하한이 1이고 a는 0이 될 수 있다는 것도 기억하자.