import sys
import math
N, H = map(int, sys.stdin.readline().split())

### Method 1.
# dp = [0 for _ in range(H)]
# for i in range(N):
#     t = int(sys.stdin.readline())
#     if i % 2 == 0:
#         for j in range(t):
#             dp[j] += 1
#     else:
#         for j in range(t):
#             dp[H-j-1] += 1


# dp = sorted(dp)
# cri = dp[0]

# left = 0
# right = H-1
# answer = 0

# while left <= right:
#     mid = (left+right)//2
#     cur_num = dp[mid]

#     if cur_num > cri:
#         right = mid-1
#     else:
#         answer = mid
#         left = mid+1

# print(cri, answer+1)


### Method 2.
lower_l = []
upper_l = []
for i in range(N):
    t = int(sys.stdin.readline())
    if i % 2 == 0:
        lower_l.append(t)
    else:
        upper_l.append(t)

lower_l.sort()
upper_l.sort()

answer = math.inf
answer_cnt = 0
for h in range(1, H+1):
    left = 0
    right = N//2-1
    temp_idx = N//2
    while left <= right:
        mid = (left+right)//2
        cur_h = lower_l[mid]

        if cur_h >= h:
            right = mid-1
            temp_idx = mid
        else:
            left = mid+1

    
    left = 0
    right = N//2-1
    temp_idx2 = N//2
    cri = H-h+1
    while left <= right:
        mid = (left+right)//2
        cur_h = upper_l[mid]
        
        if cur_h >= cri:
            right = mid-1
            temp_idx2 = mid
        else:
            left = mid+1
   
    temp = (N//2-temp_idx) + (N//2-temp_idx2)
    if answer > temp:
        answer = temp
        answer_cnt = 1
    elif answer == temp:
        answer_cnt +=1
print(answer, answer_cnt)


### 첫번째 방법은 주어진 돌의 높이를 for문을 통해 메모리에 저장해주는 방식이다. 그러나 이러한 방식은 O(N*H)의 시간복잡도를 가진게 된다.
### 두번째 방법은 답이 되는 높이를 산정하고 해당 높이 보다 크거나 같은 높이의 돌들을 이분탐색으로 구해주는 방법이다. 
### 여기서 이분탐색을 적용하는 핵심 아이디어는 돌들의 높이를 위, 아래를 구분하여 정렬해 놓은 후, 산정한 높이에 해당하는 돌의 인덱스를 구한후에 
### 인덱스를 전체 길이에서 빼줌으로써 산정한 높이에서 부셔야 하는 돌의 개수를 구해준다. 
### 이 방법을 통해서는 O(H*log(N))의 시간 복잡도가 가능해진다.
### 이분탐색에서는 다소 추상화된 변수가 2개 이상 나와서 이 처리를 주의해야 하는 것은 다른 이분탐색과 동일하다.