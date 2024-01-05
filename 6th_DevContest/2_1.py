def solution(N, D):
    answer = []
    idx_l = []
    max_l = 0
    for i in range(N-1):
        length = (D[i][0]-D[i+1][0])**2 + (D[i][1]-D[i+1][1])**2
        if length > max_l:
            idx_l = [i+1, i+2]
            max_l = length
        elif length == max_l:
            if i+1 not in idx_l:
                idx_l.append(i+1)
            if i+2 not in idx_l:
                idx_l.append(i+2)
            max_l = length
    length = (D[N-1][0]-D[0][0])**2 + (D[N-1][1]-D[0][1])**2

    if length > max_l:
        idx_l = [1,N]
    elif length == max_l:
        if 1 not in idx_l:
            idx_l.append(1)
        if N not in idx_l:
            idx_l.append(N)
    idx_l = sorted(idx_l)
    return idx_l

solution(5, [[1,4], [2,3], [6,7],[3,9],[3,7]]) ##[2,3]