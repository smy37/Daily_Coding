import sys

elec_cost = {100*2:[100, 2], 9900*3:[9900, 3], (1000000-10000)*5:[1000000-10000, 5]}
elec_usage = {100:2, 9900:3, (1000000-10000):5}
def cal_total_usage(cost):
    usage = 0
    cur = cost
    for ec in elec_cost:
        if cur >= ec:
            usage += elec_cost[ec][0]
            cur -= ec
        else:
            usage += cur//elec_cost[ec][1]
            cur = 0
            break
    if cur !=0:
        usage += cur//7
    return usage

def cal_cost(usage):
    cost = 0
    cur = usage

    for eu in elec_usage:
        if cur >= eu:
            cost += eu*elec_usage[eu]
            cur -= eu
        else:
            cost += cur*elec_usage[eu]
            cur = 0
    if cur!= 0:
        cost += 7*cur
    return cost


while 1:
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0:
        break
    total_w = cal_total_usage(A)

    left = 0
    right = total_w//2+1

    while left <= right:
        mid = (left+right)//2
        s_c = cal_cost(mid)
        n_c = cal_cost(total_w-mid)

        if n_c - s_c == B:
            print(cal_cost(mid))
            break
        if n_c-s_c > B:
            left = mid + 1
        else:
            right = mid -1


explain = """
이분탐색을 적용할 때는, 이분탐색으로 찾아야만 하는 값을 발견하여 정의 하는 것이 가장 중요하다. 
이 문제에서도 전력 사용량의 구간에 따라 요금이 바뀌므로 먼저 A 값으로 전체 전력 사용량을 구하고
이분탐색으로 상근의 전력사용량을 구한다. 이때, B 값과 비교는 요금으로 변환해야 한다. 
즉, 요금 -> 사용량 -> 요금의 변환 과정이 필요하고 사용량의 값에 대해서 이분 탐색으로 찾아주는것이 풀이의 핵심이다.
"""