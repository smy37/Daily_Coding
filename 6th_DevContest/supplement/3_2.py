def solution(N, A, Q, Query):
    answer = []

    sum_t = [0 for _ in range(N)]
    if A[0] >= 0:
        sum_t[0] = A[0]
    else:
        sum_t[0] = 0
    for i in range(1, N):
        if A[i] >= 0:
            sum_t[i] += sum_t[i - 1] + A[i]
        else:
            sum_t[i] = sum_t[i - 1]
    for q in Query:
        if q[0] == 0:
            answer.append(sum_t[q[1]])
        else:
            answer.append(sum_t[q[1]] - sum_t[q[0] - 1])

    return answer


