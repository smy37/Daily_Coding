def solution(N, A):
    answer = 0
    temp = 0
    flag = True

    cri = 0
    for i in range(len(A)-2):
        cri = min(A[i], A[i+1], A[i+2])
        if cri!= 0:
            temp += cri
            A[i] -= cri
            A[i+1] -= cri
            A[i+2] -= cri
            flag = True

    for i in range(len(A)-1):
        cri = min(A[i], A[i+1])
        if cri!= 0:
            temp += cri
            A[i] -= cri
            A[i+1] -= cri

    answer = sum(A) + temp
    return answer

print(solution(3, [3,4,4]))