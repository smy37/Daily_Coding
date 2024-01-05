def solution(N, A, Q, Query):
    answer = []

    sum_t_p = [0 for _ in range(N)]
    sum_t_m = [0 for _ in range(N)]
    if A[0] <= 0:
        sum_t_m[0] = A[0]
        sum_t_p[0] = 0
    else:
        sum_t_m[0] = 0
        sum_t_p[0] = A[0]
    for i in range(1, N):
        if A[i] <= 0:
            sum_t_m[i] += sum_t_m[i - 1] + A[i]
            sum_t_p[i] = sum_t_p[i - 1]
        else:
            sum_t_m[i] = sum_t_m[i - 1]
            sum_t_p[i] += sum_t_p[i - 1] + A[i]
    for q in Query:
        if q[0] == 1:
            if q[1] == 0:
                answer.append(sum_t_p[q[2]])
            else:
                answer.append(sum_t_p[q[2]] - sum_t_p[q[1] - 1])
        elif q[0] == 2:
            if q[1] == 0:
                answer.append(sum_t_m[q[2]])
            else:
                answer.append(sum_t_m[q[2]] - sum_t_m[q[1] - 1])
        elif q[0] == 3:
            idx = q[1]
            if A[idx] >=0:
                for i in range(idx, len(sum_t_p)):
                    if q[2] >=0:
                        sum_t_p[i] +=  q[2]-A[idx]
                    else:
                        sum_t_m[i] +=  q[2]
                        sum_t_p[i] -= A[idx]
            else:
                for i in range(idx, len(sum_t_p)):
                    if q[2] >=0:
                        sum_t_p[i] +=  q[2]
                        sum_t_m[i] -=  A[idx]
                    else:
                        sum_t_m[i] +=  q[2]-A[idx]
            A[idx] = q[2]
    return answer


print(solution(5, [20, -20, 20, -20, 20], 5, [[3,0,1],[2,0,3],[3,2,-20],[2,2,3],[1,0,4]]))