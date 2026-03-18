import sys 

N = int(sys.stdin.readline())

## First Approach
# num_list = [0]
# for i in range(N):
#     n = int(sys.stdin.readline())
#     num_list.append(num_list[-1]+n)

# total_value = num_list[-1]
# answer = 0
# for right, n in enumerate(num_list):
#     cur = num_list[right]
#     for left in range(right):
#         left_side = num_list[right]-num_list[left]
#         right_side = total_value-left_side
#         temp_max = min(left_side, right_side)
#         answer = max(answer, temp_max)
#         if cur > abs(total_value//2-left_side):
#             cur = abs(total_value//2-left_side)
#         else:
#             break

## Second Approach
answer = 0
left = 0
window_sum = 0

num_list = []
for i in range(N):
    n = int(sys.stdin.readline())
    num_list.append(n)
total = sum(num_list)

for right in range(N):
    window_sum += num_list[right]
    print("!", window_sum)
    while left < right and window_sum > total/2:
        window_sum -= num_list[left]
        left += 1
        answer = max(answer, min(window_sum, total-window_sum))

    answer = max(answer, min(window_sum, total-window_sum))


print(answer)