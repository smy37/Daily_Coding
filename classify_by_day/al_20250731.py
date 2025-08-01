import sys
from collections import deque


## 1. First Approach
# candi = sys.stdin.readline().strip()
# pw = sys.stdin.readline().strip()

# candi_dict = {}
# for idx, s in enumerate(candi):
#     if s not in candi_dict:
#         candi_dict[s] = deque()
#     candi_dict[s].append(idx+1)

# ori_length = len(candi)
# N = len(pw)

# answer = 0
# for i in range(N-1):
#     answer += ori_length**(i+1)%900528

# for idx, s in enumerate(pw):
#     candi_idx = max(candi_dict[s].popleft()-1, 0)
#     answer += candi_idx**(len(pw)-idx)
    
# print((answer+1)%900528)

## 2. Second Approach
answer = 0
MOD = 900528

str_candi = sys.stdin.readline().strip()
pw = sys.stdin.readline().strip()

str_candi_order = {}

for idx, s in enumerate(str_candi):
    str_candi_order[s] = idx

for length in range(1, len(pw)):
    answer = (answer + pow(len(str_candi),length, MOD))%MOD

for idx, s in enumerate(pw):
    cur_pw_idx = str_candi_order[s]
    answer = (answer + (pow(len(str_candi),(len(pw)-(idx+1)), MOD)*cur_pw_idx)%MOD)%MOD

print((answer+1)%MOD)

explain = """
문제의 요구사항을 명확히 파악 했어야 했던 문제. 처음에 주어지는 문자열 집합에서 각 문자를 중복으로 사용할 수 있었던
걸 놓쳐서 dictionary와 deque를 조합했던 방식으로 풀려고 했었다. 
그리고 ** 연산보다 pow 연산이 훨씬 더 속도가 빨랐고 중간중간 연산 마다 % MOD를 했어야 했다.
"""