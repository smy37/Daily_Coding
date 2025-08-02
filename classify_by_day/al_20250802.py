import sys
from collections import deque
import copy

T = int(sys.stdin.readline())

### 1. First Approach
# case_list = {}
# check_dict = {}
# for _ in range(T):
#     num = int(sys.stdin.readline())
#     case_list[num] = []
#     check_dict[num] = 0

# cmd_list = [60, 10, -10, 1, -1]

# dq = deque()
# dq.append([0, [0,0,0,0,0]])
# visited = {0:1}

# while sum(check_dict.values()) < T:
#     cur, accum = dq.popleft()
#     if cur in check_dict:
#         check_dict[cur] = 1
#         case_list[cur] = accum

#     for i in range(5):
#         next_num = max(cur + cmd_list[i], 0)
#         next_accum = copy.deepcopy(accum)

#         if next_num not in visited:
#             next_accum[i] += 1
#             dq.append([next_num, next_accum])
#             visited[next_num] = 1

# for k in case_list:
#     for num in case_list[k]:
#         print(num, end=" ")
#     print()


### 2. Second Approach
for _ in range(T):
    n = int(sys.stdin.readline())

    h = n // 60
    r = n % 60 

    if r > 35:
        h += 1
        r = 60-r

        ten = r //10
        one = r % 10

        if one > 5:
            ten +=1 
            one = 10-one
        else:
            one *= -1
        addt = 0
        mint = ten
        addo = one if one > 0 else 0
        mino = -one if one < 0 else 0
    else:
        ten = r // 10
        one = r % 10

        if one > 5:
            ten += 1
            one = one-10
        addt = ten
        mint = 0
        addo = one if one > 0 else 0
        mino = -one if one < 0 else 0
    print(h, addt, mint, addo, mino)


explain = """
처음에는 BFS로 풀려고 했지만 시간초과가 발생하였다. 결국 60으로 나누어 생기는 나머지에 대해서만
다음 명령어들로 처리하면 되는게 핵심이였다. 이때 35와 5를 기준으로 생각하는 것이 중요했다.
35 보다 크다면 60을 더한다음에 10을 빼서 만드는게 더 적은 명령어가 든다. 반대로 35 이하이면
10을 더해서 만드는게 유리하다. 60에서 빼야 되는 수와 0부터 더해야 되는 수를 10으로 나누었을 때, 
나머지가 만약 5보다 크다면 전자는 10을 한번 더빼고 1을 더해서 만드는게 더 효율적이고 후자는 
10을 한번 더 더하고 1을 빼서 만드는게 더 효율적이다. 이에 대한 로직 처리를 해줘야 한다.
"""