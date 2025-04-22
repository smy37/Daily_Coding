def check_limit(A):
    limit = min(len(A), len(A[0]))
    for i in range(len(A[0])):
        temp = 0
        t_max = 0
        for j in range(len(A)):
            if A[j][i] == ".":
                temp +=1
            else:
                temp = 0
            t_max = max(temp, t_max)
        limit = min(limit, t_max)
    return limit

def check_move(s_x, s_y, s, A):
    for i in range(s):
        for j in range(s):
            if A[s_x+i][s_y+j] == "*":
                return False
    return True

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(N, M, A):
    answer = 0
    s = check_limit(A)
    for i in range(s, 0, -1):
        e_x = N-i
        e_y = M-i
        visited = {}
        q = []
        if check_move(0,0, i, A):

            q.append([0,0])
            visited[(0,0)] = 1
        else:
            continue
        while q:
            t = q.pop()

            if t == [e_x, e_y]:
                return i
            for j in range(4):
                n_x = t[0] + dx[j]
                n_y = t[1] + dy[j]

                if 0<= n_x <= e_x and 0<=n_y <= e_y and (n_x,n_y) not in visited and check_move(n_x,n_y,i,A):
                    q.append([n_x,n_y])
                    visited[(n_x,n_y)] = 1
    return 0

print(solution(3, 5, ["...**", ".....", "*...."]))