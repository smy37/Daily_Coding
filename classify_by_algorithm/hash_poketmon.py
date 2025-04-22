import sys


def solution(nums):
    answer = 0
    mon_dict = {}
    for i in nums:
        if i not in mon_dict:
            mon_dict[i] = 1
        else:
            mon_dict[i] +=1
    cri = int(len(nums)/2)
    if len(mon_dict) > cri:
        answer = cri
    else:
        answer = len(mon_dict)
    return answer