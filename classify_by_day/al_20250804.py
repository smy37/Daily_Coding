import sys
import heapq

N = int(sys.stdin.readline())

### 1. First Approach
# cur_pos = 0
#
# hq = []
# heapq.heapify(hq)
#
# answer = 0
#
# for _ in range(N):
#     cmd = list(map(int, sys.stdin.readline().split()))
#
#     if cmd[0] == 1:
#         heapq.heappush(hq, [abs(cur_pos-cmd[1]), cmd[1]])
#     elif cmd[0] == 2:
#         while len(hq) >0:
#             cur_item = heapq.heappop(hq)
#             answer += abs(cur_pos-cur_item[1])
#             cur_pos = cur_item[1]
#
# print(answer)


### 2. Second Approach
right_tree = []
left_tree = []
answer = 0
cur_pos = 0
for _ in range(N):
    cmd = list(map(int, sys.stdin.readline().split()))
    rt_idx = 0
    lt_idx = 0
    if cmd[0] == 1:
        if cur_pos <= cmd[1]:
            right_tree.append(cmd[1])
        else:
            left_tree.append(cmd[1])

    elif cmd[0] == 2:
        right_tree.sort()
        left_tree.sort()

        while 1:
            if rt_idx < len(right_tree) and lt_idx < len(left_tree):
                if abs(cur_pos-right_tree[rt_idx]) < abs(cur_pos-left_tree[lt_idx]):
                    answer += abs(cur_pos-right_tree[rt_idx])
                    cur_pos = right_tree[rt_idx]
                    rt_idx +=1
                else:
                    answer += abs(cur_pos - left_tree[lt_idx])
                    cur_pos = left_tree[lt_idx]
                    lt_idx += 1
            elif rt_idx < len(right_tree):
                answer += abs(cur_pos - right_tree[rt_idx])
                cur_pos = right_tree[rt_idx]
                rt_idx += 1

            elif lt_idx < len(left_tree):
                answer += abs(cur_pos - left_tree[lt_idx])
                cur_pos = left_tree[lt_idx]
                lt_idx += 1
            else:
                break
        right_tree = []
        left_tree = []

print(answer)