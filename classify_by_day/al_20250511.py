import sys

N, M, L = map(int, sys.stdin.readline().split())

cut_l = []
for _ in range(M):
    cut_l.append(int(sys.stdin.readline()))

def checK_cutting_num(cut_list, cri_l, L):
    cnt = 0
    cur = 0

    for l in cut_list:
        if l-cur >= cri_l and L-l >= cri_l:
            cnt += 1
            cur = l
    return cnt


for _ in range(N):
    cut_num = int(sys.stdin.readline())

    left = 1
    right = L-1
    temp_answer = -1

    while left <= right:
        mid = (left+right)//2

        cut_cnt = checK_cutting_num(cut_l, mid, L)

        if cut_cnt < cut_num:
            right = mid-1
        else:
            left = mid+1
            temp_answer = mid

    print(temp_answer)

explain = """
특정 길이로 잘라지는 케익의 개수를 세준 후(케익이 자르는 위치는 고정되서 주어짐을 유의해야함) 잘라져야 하는 개수 이상이면 특정 길이를 늘려주고 미만이라면 특정 길이를
줄여주는데 이러한 과정을 이분탐색을 통해서 찾는 것이 핵심. 
이때, 자르는 기준으로 잘랐을 때, 좌측에서의 길이 뿐만 아니라 우측 끝과의 거리도 함께 고려해 줘야 한다는게 놓치기 쉬운 포인트이다. 
즉 다음과 같이 좌측에서 부터의 거리와 우측에서부터의 거리 모두 기준 길이보다 길어야 함을 유의하자. (if l-cur >= cri_l and L-l >= cri_l)
"""