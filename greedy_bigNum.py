import sys
from itertools import combinations



def solution(number, k):
    answer = ''
    stack = []
    idx = 0
    stack.append(number[0])
    while k>0 and idx < len(number)-1 and stack:
        while stack and k>0:
            if stack[-1] < number[idx+1]:
                k-=1
                stack.pop()
            else:
                break
        stack.append(number[idx + 1])
        idx+=1


    if len(stack) < len(number)-k and k >=0:
        stack += number[idx+1:]
    else:
        stack = stack[:-k]
    answer = stack

    return ''.join(answer)


print(solution("1231234",3))