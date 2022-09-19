import sys
from itertools import permutations as permu
k = 80
dungeons = [[80,20],[50,40],[30,10]]

def solution(k, dungeons):
    answer = 0
    nPr = permu(dungeons, len(dungeons))
    new_k = k
    for i in nPr:
        new_k = k
        temp = 0
        for j in i:
            if new_k >= j[0]:
                new_k -= j[1]
                temp +=1
            else:
                break
        answer = max(answer, temp)
    return answer

print(solution(k, dungeons))