def ccw(ab, ac, ad):
    t1 = ab[0]*ac[1]-ab[1]*ac[0]
    t2 = ab[0]*ad[1]-ab[1]*ad[0]
    return t1*t2
def check_cross(AB, CD):
    AB = sorted(AB,  key = lambda x : [x[0],x[1]])
    CD = sorted(CD, key = lambda x : [x[0],x[1]])
    A = AB[0]
    B = AB[1]
    C = CD[0]
    D = CD[1]
    a_b = [B[0]-A[0], B[1]-A[1]]
    a_c = [C[0]-A[0], C[1]-A[1]]
    a_d = [D[0]-A[0], D[1]-A[1]]
    cri1 = ccw(a_b, a_c, a_d)
    c_d = [D[0]-C[0], D[1]-C[1]]
    c_a = [A[0]-C[0], A[1]-C[1]]
    c_b = [B[0]-C[0], B[1]-C[1]]
    cri2 = ccw(c_d, c_a, c_b)

    if cri1 ==0 and cri2 == 0:
        if ((B[0]<C[0] or (B[0]==C[0] and B[1]<C[1])) or ((D[0]<A[0]) or (D[0]==A[0] and D[1]<A[1]))) ==False:
            return True
        else:
            return False
    if cri1<=0 and cri2 <=0:
        return True
    else:
        return False

def check_start(S, P, N):
    px = (S[0]-P[0])
    py = (S[1]-P[1])
    nx = (S[0]-N[0])
    ny = (S[1]-N[1])
    if px ==0:
        if nx == 0:
            if py*ny > 0:

                return False
        return True
    if nx == 0:
        if px == 0:
            if py*ny > 0:

                return False
        return True
    if (py == 0 and ny == 0):
        if nx*ny >0:
            return False
        else:
            return True
    if abs(py / px - ny / nx) < 10e-7:
        print(abs(py / px - ny / nx))
        return False
    else:
        return True

def solution(N, D):
    answer = []
    cur_s = 1
    line_l = []
    line_l.append([D[0], D[1]])
    answer.append(1)
    answer.append(2)
    for i in range(2, N):
        Cur = D[cur_s]
        Next = D[i]
        Pre = line_l[-1][0]
        if check_start(Cur,Pre, Next) == False:
            continue
        else:
            if len(line_l) >=2:
                for j in range(len(line_l)-2,-1, -1):
                    if check_cross([Cur, Next], line_l[j]) == True:
                        break
                else:
                    line_l.append([Cur, Next])
                    cur_s = i
                    if i+1 not in answer:
                        answer.append(i + 1)
            else:
                line_l.append([Cur, Next])
                cur_s = i
                if i+1 not in answer:
                    answer.append(i+1)
    Cur = D[cur_s]
    Next = D[0]
    Pre = line_l[-1][0]

    if len(line_l) < 2:
        return [-1]
    elif len(line_l) == 2:
        if check_start(Cur, Pre, Next) == True:
            if cur_s+1 not in answer:
                answer.append(cur_s+1)
            return answer
        else:
            return [-1]
    if check_start(Cur, Pre, Next) == False:

        return [-1]
    else:

        for j in range(len(line_l) - 2, 0, -1):
            if check_cross([Cur, Next], line_l[j]) == True:
                return [-1]
        else:
            line_l.append([Cur, Next])
            cur_s = i
    answer = sorted(answer)
    return answer

# print(check_cross([[3, 3], [5, 6]],[[4, 1], [1, 1]]))
# print(check_cross([[2,8],[9,23]], [[1,10],[9,8]]))
# print(check_cross([[1,1],[5,5]], [[6,6],[1,5]]))
# print(check_cross([[1,1],[5,5]], [[5,5],[1,5]]))
# print(check_cross([[1,1],[5,5]], [[6,6],[9,9]]))
# print(check_cross([[1,1],[5,5]], [[5,5],[9,9]]))
# print(check_cross([[1,1],[5,5]], [[1,5],[5,1]]))
# print(check_cross([[-1,7],[-1,5]], [[-1,7],[-1,3]]))

# print(solution(10, [[4,1],[1,1],[3,3],[5,6],[8,4],[8,8], [10,10], [10,4], [9,4],[11,4]]))
# print(solution(5, [[1,4],[3,2],[6,6],[8,5],[5,0]]))
print(solution(6, [[0,0],[-2,0],[-2,10], [6,10],[6,0], [4,0]]))
# print(solution(3, [[1,1],[3,3],[6,5]]))