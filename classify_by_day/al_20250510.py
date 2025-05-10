import sys

N = int(sys.stdin.readline())
num_l = list(map(int, sys.stdin.readline().split()))

### Method 1.
# sum_l = []
# for i in range(N):
#     for j in range(i+1, N):
#         sum_l.append([num_l[i]+num_l[j], i, j])


# sum_l.sort()

# answer = {}

# for i in range(N):
#     cur_num = -num_l[i]

#     left = 0
#     right = len(sum_l)-1

#     while left <= right:
#         mid = (left+right)//2
#         sum_num = sum_l[mid][0]

#         if cur_num == sum_l[mid][0] \
#             and i != sum_l[mid][1] and i != sum_l[mid][2]:
#             temp = [i, sum_l[mid][1], sum_l[mid][2]]
#             temp.sort()
#             answer[tuple(temp)] = True
#         if sum_num > cur_num:
#             right = mid - 1
#         elif sum_num < cur_num:
#             left = mid + 1
#         else:
#             if mid+1 < N and sum_l[mid+1][0] == cur_num:
#                 left = mid+1
#             elif mid-1 >= 0 and sum_l[mid-1][0] == cur_num:
#                 right = mid-1
#             else:
#                 right = mid - 1

# print(len(answer.keys()))

### Method 2.
num_l.sort()
answer = 0
for i in range(N):
    if num_l[i] > 0:
        break
    for j in range(i + 1, N):
        target = -(num_l[i] + num_l[j])
        if target < 0:
            break
        left = j + 1
        right = N - 1
        idx1 = -1
        while left <= right:
            mid = (left + right) // 2
            cur_num = num_l[mid]

            if cur_num >= target:
                right = mid - 1
                if cur_num == target:
                    idx1 = mid
            else:
                left = mid + 1
        left = j + 1
        right = N - 1
        idx2 = -1

        while left <= right:
            mid = (left + right) // 2
            cur_num = num_l[mid]

            if cur_num > target:
                right = mid - 1
            else:
                left = mid + 1
                if cur_num == target:
                    idx2 = mid
        if idx1 != -1 and idx2 != -1:
            answer += (idx1-idx2+1)
print(answer)


explain = """
세개의 수 중 2개의 수를 합친 값을 구하고 이 값의 음수값이 처음에 주어진 숫자 배열에 있는지 이분탐색으로 푸는것이 핵심인 문제이다. 
첫번째 시도에서는 먼저 2개의 수를 합친 값으로 이루어진 배열을 구하는 방식으로 했는데 중복되는 수 처리가 까다로워서 두번째 방법을 사용하였다. 
두번째 방법에서는  i번째 수와 j 번째 수를 더한 값과 j+1에서 N번째 배열을 비교한다. 이렇게 하면 자연스럽게 i, j , k는 겹치지 않게 된다. 
또한 같은 수가 중복해서 등장 할 수 있으므로 이분탐색을 2번 돌려서 가장 우측에 있는값과 가장 좌측에 있는 값의 인덱스를 구해준다.
이때, cur_num <= target 일때, idx 값을 갱신해 죽 된다면 가장 우측에 있는 값을 가져오고 cur_num >= target 일때, idx 값을 갱신해 준다면
가장 좌측에 있는 값을 가져오는 것임을 인지 해야 한다.  
"""