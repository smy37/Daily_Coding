import sys
from collections import deque
import copy

T = int(sys.stdin.readline())
case_list = {}
check_dict = {}
for _ in range(T):
    num = int(sys.stdin.readline())
    case_list[num] = []
    check_dict[num] = 0

cmd_list = [60, 10, -10, 1, -1]

dq = deque()
dq.append([0, [0,0,0,0,0]])
visited = {0:1}

while sum(check_dict.values()) < T:
    cur, accum = dq.popleft()
    if cur in check_dict:
        check_dict[cur] = 1
        case_list[cur] = accum

    for i in range(5):
        next_num = cur + cmd_list[i]
        next_accum = copy.deepcopy(accum)

        if next_num not in visited:
            next_accum[i] += 1
            dq.append([next_num, next_accum])
            visited[next_num] = 1

for k in case_list:
    for num in case_list[k]:
        print(num, end=" ")
    print()


