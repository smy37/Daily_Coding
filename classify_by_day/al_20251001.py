import sys 
from bisect import bisect_right


N = int(sys.stdin.readline())
cord_l = []
foul_l = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())

    if x >= 0:
        if x > y:
            foul_l.append([x,y])
        else:
            cord_l.append(x*x+y*y)
    else:
        if -x > y:
            foul_l.append([x,y])
        else:
            cord_l.append(x*x+y*y)

Q = int(sys.stdin.readline())
cord_l.sort()
for _ in range(Q):
    r = int(sys.stdin.readline())
    hit_cnt = 0
    ### 1. First Approach
    # for d in cord_l:
    #     if d <= r**2:
    #         hit_cnt += 1
    #     else:
    #         break

    ### 2. Second Appraoch
    # r2 = r*r
    # hit_cnt = bisect_right(cord_l, r2)

    # print(len(foul_l), hit_cnt, len(cord_l)-hit_cnt)

    ### 3. Third Approach
    r2 = r*r
    left = 0
    right = len(cord_l)-1
    while left<=right:
        mid = (left+right)//2

        if cord_l[mid] > r2:
            right = mid-1
        else: 
            left = mid+1
        
    print(len(foul_l), left, len(cord_l)-left)

explain = """
좌표와 원의 관계를 나타내는건 쉬웠지만 거리 리스트와 반지름을 비교하느 과정에서
속도를 위해서 이분탐색이 필요하였다.
"""

