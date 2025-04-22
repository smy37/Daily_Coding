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
def check_cross(i, j, hull):
    nexti = hull[(i+1)%len(hull)]
    prej = hull[j-1]

    dxi = nexti[0] - hull[i][0]
    dyi = nexti[1] - hull[i][1]

    dxj = prej[0] - hull[j][0]
    dyj = prej[1] - hull[j][1]
    if check_line_cross([[hull[i][0], hull[i][1]],[hull[i][0]+dxi*1000, hull[i][1]+dyi*1000]], \
                        [[hull[j][0], hull[j][1]],[hull[j][0]+dxj*1000, hull[j][1]+dyj*1000]]):
        return True
    return False

def check_special(s_l, m_l, stack): ## 기존 말뚝 2개를 잇고 꼭지점중 양인 것들이 모두 기존 말뚝 2개를 이은 직선의 위에 있거나 아래에 있는지 1차적으로 판단.
    for i in range(len(m_l)):
        for j in range(i+1, len(m_l)):
            n_ml =  [stack[m_l[i]]+[m_l[i]], stack[(m_l[j])]+[m_l[j]]]
            n_ml = sorted(n_ml, key= lambda x : [x[0], -x[1]], reverse= True)
            x_m1, y_m1 = n_ml[0][0], n_ml[0][1]
            x_m2, y_m2 = n_ml[1][0], n_ml[1][1]

            dx = x_m1-x_m2
            dy = y_m1-y_m2
            u_cnt = 0
            d_cnt = 0
            if dx == 0:
                for k in s_l:
                    if stack[k][0] >= x_m1:
                        u_cnt +=1
                    else:
                        d_cnt +=1
            elif dy == 0:
                for k in s_l:
                    if stack[k][1] >= y_m1:
                        u_cnt +=1
                    else:
                        d_cnt +=1
            else:
                m = dy/dx
                c = y_m1 - m*x_m1
                for k in s_l:
                    val = m*stack[k][0] + c
                    if val <= stack[k][1]:
                        u_cnt +=1
                    else:
                        d_cnt += 1
            if u_cnt != 0 and d_cnt != 0:
                continue
            elif d_cnt == 0:
                idx1 = n_ml[0][2]
                idx2 = n_ml[1][2]
                if check_cross(idx1, idx2, stack):  ## 모든 꼭지점(양)들이 말뚝을 이은 직선의 위에 있다면 두 말뚝에서 연장한 반직선이 만난다면 모든 양들을 하나의 말뚝을 추가함으로써 포함 가능케함
                    return True
            elif u_cnt == 0:
                idx2 = n_ml[0][2]
                idx1 = n_ml[1][2]
                if check_cross(idx1, idx2, stack): ## 모든 꼭지점(양)들이 말뚝을 이은 직선의 아래에 있다면 두 말뚝에서 연장한 반직선이 만난다면 모든 양들을 하나의 말뚝을 추가함으로써 포함 가능케함
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
    malduck_l = []
    malduck_cnt = 0
    sheep_cnt = 0
    idx = 0
    limit = 3
    for i in stack:
        if i not in D:
            sheep_cnt += 1
            sheep_l.append(idx)
        else:
            malduck_cnt +=1
            malduck_l.append(idx)
        idx += 1

    if malduck_cnt >=1: ## 컨벡스 훌로 구한 다각형의 꼭지점 중 하나라도 기존 말뚝이라면 2개의 말뚝을 추가하여 어떤 경우에도 포함하는 삼각형 구성 가능
        limit =2
    elif malduck_cnt == 0:  ## 컨벡스 훌로 구한 다각형의 꼭지점이 모두 양일 때는 말뚝 3개를 사용해서 큰 삼각형 만들어야함.
        limit = 3

    if sheep_cnt == 0:  ## 다각형의 꼭지점이 모두 원래 말뚝이라면 추가 필요 X
        answer = 0
    elif sheep_cnt == 1: ## 다각형의 꼭지점 중 하나만이 양이라면 하나의 말뚝 추가해야함
        answer = 1
    elif sheep_cnt >= 2:    ## 다각형의 꼭지점 중 2개 이상이 양이라면 경우에 따라서 1, 2, 3개의 말뚝을 추가해야함.
        if malduck_cnt ==  0:
            answer = limit  ## limit = 3
        elif malduck_cnt == 1:
            answer = limit  ## limit = 2
        elif malduck_cnt >=2: ## 기존 말뚝의 개수가 2개 이상 이라면 특정 상황에서만 1개의 말뚝 추가로 모든 양을 포함시킬 수 있음. 나머지 상황에서는 모두 2개의 말 뚝을 이용해서 큰삼각형 그림
            if check_special(sheep_l, malduck_l, stack):
                answer = 1
            else:
                answer = 2
    return answer

N = 6
D = [[0,0],[1,1],[5,0],[5,3],[5,4],[0,3]]
M = 6
S = [[-3,0],[-1,-4],[3,-2],[3,0],[10,-1],[6,-5]]

print(solution(N,D,M,S))

N = 6
D = [[0,1],[0,5],[-1,3]]
M = 3
S = [[4,2],[5,3],[3,4]]

print(solution(N,D,M,S))

N = 5
D = [[-3,8],[-2,9],[1,11],[4,10],[5,7]]
M = 3
S = [[0,1],[3,4],[-2,5]]

print(solution(N,D,M,S))