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
answer = 0
cur_pos = 0

right_tree = []
left_tree = []

rt_idx = 0
lt_idx = 0
for _ in range(N):
    cmd = list(map(int, sys.stdin.readline().split()))

    if cmd[0] == 1:
        if cur_pos <= cmd[1]:
            right_tree.append(cmd[1])
        else:
            left_tree.append(cmd[1])

    elif cmd[0] == 2:
        right_tree.sort()
        left_tree.sort(reverse= True)

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
        rt_idx = 0
        lt_idx = 0

print(answer)


explain = """
실시간으로 업데이트 되는 상황에서 최소 거리가 되는 점을 찾아야 하므로 처음에 heap으로 푸는 것을 시도하였다. 
그러나 heap에 들어간 값이 cur_pos가 바뀜에 따라 의미가 없어지므로 heap을 사용하는 건 적절하지 않았다.
cur_pos를 기준으로 왼쪽에 있는 배열을 만들고 오른쪽에 있는 배열을 만든다음에 cmd 2가 들어오면 cur_pos를 
중점으로 왼쪽 또는 오른쪽으로 왔다갔다 하면서 청소가 진행된다. 이때, 왼쪽에 대한 인덱스와 오른쪽에 대한 인덱스를
증가시켜 가면서 이동거리를 측정하면 된다. 하나 유의해야 할점은 left_tree 배열은 정렬시 거꾸로 해야 한다. 
cur_pos를 기준으로 더 가까운 거리가 배열의 첫번째 부터 나오게 하려면.
"""