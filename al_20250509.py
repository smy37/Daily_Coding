import sys
import bisect

N, M, L = map(int, sys.stdin.readline().split())
stage = list(map(int, sys.stdin.readline().split()))
stage.sort()
answer = 0

### Method 1. 수동 이분탐색 구현현
# for _ in range(M):
#     x, y = map(int, sys.stdin.readline().split())

#     left = 0
#     right = N-1

#     temp_idx = -1
#     while left <= right:
#         mid = (left+right)//2
#         cur_n = stage[mid]

#         if cur_n >=x:
#             temp_idx = mid
#             right = mid -1
#         else:
#             left = mid +1
#     if stage[temp_idx]-x+y <= L:
#         answer += 1
#     elif temp_idx!= 0 and x-stage[max(temp_idx-1, 0)]+y <= L:
#         answer += 1

# print(answer)


### Method 2. Bisect 사용
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())

    idx = bisect.bisect_left(stage, x)
    if idx < N and stage[idx]-x+y <= L:
        answer += 1
    elif idx != 0 and x-stage[idx-1]+y <= L:
        answer += 1 
print(answer)


explain = """
처음에는 이분 탐색을 수동 구현 했는데 bisect가 C로 되어 있어서 수동으로 구현하는 것 보다 무조건 훨씬 빠르다.
속도가 중요한 경우에는 bisect를 사용하자. bisect_left(arr, x)는 x 이상인 arr 원소의 인덱스 최솟값을 구해준다.
사대를 정렬후에 동물의 좌표에 대하여 가장 먼저 동물과 사대의 x좌표가 가장 가까운 사대를 찾고(이분 탐색으로 찾을 경우 2개 나온다)
이 사대와의 거리 + 동물의 y 좌표가 사정거리 L 이하인지 체크해서 이하면 그 동물이 사정거리에 있다는 것이 문제풀이의 핵심이다.
"""