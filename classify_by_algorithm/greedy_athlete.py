import sys

n = 5
lost = [2,4]
reserve = [1,3,5]

def solution(n, lost, reserve):
    answer = 0
    cloth_num = {}
    for i in range(1, n+1):
        cloth_num[i] = 1
    for j in lost:
        cloth_num[j] -=1
    for j in reserve:
        cloth_num[j] +=1

    for i in cloth_num:
        if cloth_num[i] == 2:
            if i-1 >=1 and cloth_num[i-1] == 0:
                cloth_num[i-1] +=1
            elif i+1 <= n and cloth_num[i+1] == 0:
                cloth_num[i+1] +=1
    for i in cloth_num:
        if cloth_num[i] !=0:
            answer +=1

    return answer

print(solution(n, lost, reserve))