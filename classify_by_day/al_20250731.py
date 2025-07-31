import sys
from collections import deque

candi = sys.stdin.readline().strip()
pw = sys.stdin.readline().strip()

candi_dict = {}
for idx, s in enumerate(candi):
    if s not in candi_dict:
        candi_dict[s] = deque()
    candi_dict[s].append(idx+1)

ori_length = len(candi)
N = len(pw)

answer = 0
for i in range(N-1):
    answer += ori_length**(i+1)%900528

for idx, s in enumerate(pw):
    candi_idx = max(candi_dict[s].popleft()-1, 0)
    answer += candi_idx**(len(pw)-idx)
    
print((answer+1)%900528)