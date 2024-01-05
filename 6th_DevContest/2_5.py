import math
import copy
def ccw(ab, ac, ad):
    t1 = ab[0]*ac[1]-ab[1]*ac[0]
    t2 = ab[0]*ad[1]-ab[1]*ad[0]
    return t1*t2
def check_line_cross(AB, CD):
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
        return False
    if cri1<=0 and cri2 <=0:
        return True
    else:
        return False

def cross(s, a, b):
    return (a[0]-s[0])*(b[1]-s[1])-(a[1]-s[1])*(b[0]-s[0])

def cal_angle(p1, p2):
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

def cal_dist(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
def check_cross(i, j, hull,s_l):
    prei = hull[i-1]
    nexti = hull[(i+1)%len(hull)]
    prej = hull[j-1]
    nextj = hull[(j+1)%len(hull)]
    if i+1 == j:
        dxi = hull[i][0]-prei[0]
        dyi = hull[i][1]-prei[1]

        dxj = hull[j][0] - nextj[0]
        dyj = hull[j][1] - nextj[1]
        # if (prei not in s_l and nextj not in s_l) == False:
        #     return False
        if check_line_cross([[prei[0], prei[1]],[prei[0]+dxi*100, prei[1]+dyi*100]], [[nextj[0], nextj[1]],[nextj[0]+dxj*100, nextj[1]+dyj*100]]):
            return True
        return False
    else:
        dxi = hull[i][0] - prei[0]
        dyi = hull[i][1] - prei[1]

        dxj = hull[j][0] - nextj[0]
        dyj = hull[j][1] - nextj[1]
        if dxi == 0 and dxj == 0:
            return False
        elif dyi == 0 and dyj == 0:
            return False
        elif dxi!=0 and dxj!=0:
            if abs(dyi/dxi-dyj-dxj)<=10e-7:
                return False
        if (prei != nextj):
            if check_line_cross([[prei[0], prei[1]], [prei[0] + dxi * 1000, prei[1] + dyi * 1000]], \
                                [[nextj[0], nextj[1]], [nextj[0] + dxj * 1000, nextj[1] + dyj * 1000]]):
                return True
        dxi = hull[i][0] - nexti[0]
        dyi = hull[i][1] - nexti[1]

        dxj = hull[j][0] - prej[0]
        dyj = hull[j][1] - prej[1]

        if (nexti != prej):
            if check_line_cross([[nexti[0], nexti[1]], [nexti[0] + dxi * 1000, nexti[1] + dyi * 1000]], \
                                [[prej[0], prej[1]], [prej[0] + dxj * 1000, prej[1] + dyj * 1000]]):
                return True
        return False
def solution(N, D, M, S):
    answer = 0
    s_D = copy.deepcopy(S+D)
    s_D = sorted(s_D, key = lambda x : [x[1], x[0]])
    start = s_D[0]
    del s_D[0]
    s_D = sorted(s_D, key = lambda x : [cal_angle(start, x), cal_dist(start, x)])
    stack = [start]

    for p in s_D:
        while len(stack) > 1 and cross(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)
    sheep_l = []
    sheep = []
    malduck_cnt = 0
    idx = 0
    limit = 3
    for i in stack:
        if i not in D:
            answer += 1
            sheep_l.append(idx)
            sheep.append(i)
        else:
            malduck_cnt +=1
    if malduck_cnt >=1:
        limit =2
        idx +=1
    reduce_l = []
    for i in range(len(sheep_l)):
        for j in range(i+1, len(sheep_l)):
            idx1 = sheep_l[i]
            idx2 = sheep_l[j]
            if idx1 not in reduce_l and idx2 not in reduce_l:
                if check_cross(idx1, idx2, stack, sheep):
                    reduce_l.append(idx1)
                    reduce_l.append(idx2)
                    answer -=1
    print(answer)
    answer = min(answer, limit)
    return answer

N = 6
D = [[0,0],[1,1],[5,0],[5,3],[5,4],[0,3]]
M = 6
S = [[-3,0],[-1,-4],[3,-2],[3,0],[10,-1],[6,-5]]

print(solution(N,D,M,S))