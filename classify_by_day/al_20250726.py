import sys 
from collections import deque
import copy
N, K = map(int, sys.stdin.readline().split())
num_l = list(map(int, sys.stdin.readline().split()))
incline = sorted(num_l)
answer = -1

dq = deque()
dq.append([num_l, 0])
visited = {tuple(num_l): 1}

while dq:
    cur_num, num = dq.popleft()
    if cur_num == incline:
        answer = num
        break
    for i in range(N-K+1):
        next_num = copy.deepcopy(cur_num)
        for j in range(K//2):
            back = cur_num[i+K-1-j]
            next_num[i+K-1-j] = cur_num[i+j]
            next_num[i+j] = cur_num[i+K-1-j]
        if tuple(next_num) not in visited:
            visited[tuple(next_num)] = 1
            dq.append([next_num, num+1])

print(answer)

explain = """
현재 수에서 숫자를 뒤집힐 수 있는 경우를 수형도를 이용하여 구한다. 이때, 수형도로 탐색을
위해서 BFS를 사용하였다. 또한, 문자열 슬라이스보다는 index로 직접 바꾸는 방식으로 시간복잡도를
줄였다.
"""