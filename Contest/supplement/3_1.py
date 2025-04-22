def solution(N, A, Q, Query):
    answer = []
    sum_t = [0 for _ in range(N)]
    sum_t[0] = A[0]
    for i in range(1,N):
        sum_t[i] += sum_t[i-1] + A[i]
    for q in Query:
        if q[0] == 0:
            answer.append(sum_t[q[1]])
        else:
            answer.append(sum_t[q[1]]-sum_t[q[0]-1])

    return answer



print(solution(5, [1,2,3,4,5], 3, [[0,2],[1,4],[2,3]]))