import sys
import math

N, Q = map(int, sys.stdin.readline().split())
x_l = list(map(int, sys.stdin.readline().split()))
y_l = list(map(int, sys.stdin.readline().split()))
acc_sum = [0]*N
acc_sum_r = [0]*N

for i in range(N-1):
    y_diff = y_l[i+1]-y_l[i]
    temp = 0
    temp_r = 0
    dist = math.sqrt(y_diff ** 2 + (x_l[i] - x_l[i + 1])**2)
    if y_diff >0:
        temp += 3*dist
    elif y_diff < 0:
        temp += dist
    else:
        temp += 2*dist
    acc_sum[i+1] = acc_sum[i] + temp

for i in range(N-1, 0, -1):
    y_diff = y_l[i-1]-y_l[i]
    temp = 0
    dist = math.sqrt(y_diff ** 2 + (x_l[i-1] - x_l[i])**2)
    if y_diff >0:
        temp += 3*dist
    elif y_diff < 0:
        temp += dist
    else:
        temp += 2*dist
    acc_sum_r[i-1] = acc_sum_r[i] + temp

for _ in range(Q):
    i, j = map(int, sys.stdin.readline().split())

    if i < j:
        print(acc_sum[j-1]-acc_sum[i-1])
    else:
        print(acc_sum_r[j-1]-acc_sum_r[i-1])


## 누적합을 이용해서 빠르게 특정 구간의 합을 구하면 된다.
## 이때, 왼쪽에서 오른쪽으로 가는 것과 오른쪽에서 왼쪽으로 가는 것의 같은 길이에 대해 가중치가 달라지므로
## 누적합 배열이 2개 존재해야 한다.