import sys 

N = int(sys.stdin.readline())

num_list = [0]
for i in range(N):
    n = int(sys.stdin.readline())
    num_list.append(num_list[-1]+n)

total_value = num_list[-1]
answer = 0
for right, n in enumerate(num_list):
    cur = num_list[right]
    for left in range(right):
        left_side = num_list[right]-num_list[left]
        right_side = total_value-left_side
        temp_max = min(left_side, right_side)
        answer = max(answer, temp_max)
        if cur > abs(total_value//2-left_side):
            cur = abs(total_value//2-left_side)
        else:
            break

print(answer)