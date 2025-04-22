import math

def cross(s, a, b):
    return (a[0]-s[0])*(b[1]-s[1])-(a[1]-s[1])*(b[0]-s[0])

def cal_angle(p1, p2):
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

def cal_dist(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2

def solution(N, D, M, S):
    answer = 0
    s_D = S+D
    s_D = sorted(s_D, key = lambda x : [x[1], x[0]])
    start = s_D[0]
    del s_D[0]
    s_D = sorted(s_D, key = lambda x : [cal_angle(start, x), cal_dist(start, x)])
    stack = [start]

    for p in s_D:
        while len(stack) > 1 and cross(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)
    for i in stack:
        if i not in D:
            answer += 1
    if len(stack) == 2:
        answer +=1
    return answer


# points = [[1,1], [3,1], [3,3], [5,3],[4,0]]
N = 2
# D = [[2,1], [10,1], [4,9], [8,12]]
D = [[1,0], [4,0]]
M = 2
# S = [[1,4],[12,1],[10,12]]
S = [[2,2], [3,2]]
print(solution(N, D, M, S))