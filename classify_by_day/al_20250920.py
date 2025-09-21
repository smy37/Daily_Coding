import sys
import math

upper = 1000000000

sum_l = [1, 2]

while sum_l[-1] <= upper:
    sum_l.append(sum_l[-1]+sum_l[-2]+1)


T = int(sys.stdin.readline())
for _ in range(T):
    cur_n = int(sys.stdin.readline())

    for i in range(len(sum_l)):
        if cur_n < sum_l[i]:
            print(i)
            break
        elif cur_n == sum_l[i]:
            print(i+1)
            break

explain = """
루트를 기준으로 왼쪽 오른쪽 생각했을 때, 왼족에 높이 h-1을 만드는데 필요한 최소 개수 그리고 오른쪽에 높이 h-2를 만드는 노드의 최소개수가 있다면
높이가 h가 된다. 주의해야 할점은, 이렇게 구한 원소들과 같을때와 작을때는 1차이가 난다는 것이다. 
"""