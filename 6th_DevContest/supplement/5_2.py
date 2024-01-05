def solution(N, A):
    answer = 0
    temp = 0
    flag = True
    while flag:
        flag = False
        cri = 0
        for i in range(len(A)-1):
            cri = min(A[i], A[i+1])
            if cri!= 0:
                temp += cri
                A[i] -= cri
                A[i+1] -= cri
                flag = True
    answer = sum(A) + temp
    return answer