def solution(M, A):
    answer = 0
    flag1 = False
    flag2 = False
    for i in range(M):
        if A[0][i] =="*" and A[1][i] == "*":
            flag1 = True
            break
        elif A[0][i] =="*" or A[1][i] == "*":
            flag2 = True
    if flag1 == True:
        answer = 0
    elif flag2 == True:
        answer = 1
    else:
        answer = 2
    return answer