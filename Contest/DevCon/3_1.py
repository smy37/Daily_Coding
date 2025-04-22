def solution(N, M, Command):
    answer = []
    cur_W = N**2
    cur_X = N
    cur_Y = N
    for i in range(M):
        cmd = Command[i]
        if cmd[0] in [1,2]:
            b_y = cur_Y / cmd[1]
            cur_Black = cur_X*b_y
            cur_W -= 2*cur_Black
        elif cmd[0] in [3,4]:
            b_x = cur_X / cmd[1]
            cur_Black = b_x*cur_Y
            cur_W -= 2*(cur_Black)
        answer.append(cur_Black, cur_W)
    return answer