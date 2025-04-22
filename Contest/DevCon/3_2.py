def solution(N, M, Command):
    answer = []
    cur_wLB = [0,0]
    cur_wRT = [N,N]
    cur_LB = [0,0]
    cur_RT = [N,N]
    for i in range(M):
        cmd = Command[i]
        cur_X = cur_RT[0]-cur_LB[0]
        cur_Y = cur_RT[1]-cur_LB[1]
        if cmd[0] == 1:
            cri = N/cmd[1]
            if cur_wRT[1] <= cur_RT[1]-cri*2:
                cur_RT[1] -= cri
            else:
                cur_wRT[1] = cur_RT[1]-cri*2
                cur_RT[1] -= cri
        elif cmd[0] == 2:
            cri = N / cmd[1]
            if cur_wLB[1] >= cur_LB[1]+cri*2:
                cur_LB[1] += cri
            else:
                cur_wLB[1] = cur_LB[1]+cri*2
                cur_LB[1] += cri
        elif cmd[0] == 3:
            cri = N / cmd[1]
            if cur_wLB[0] >= cur_LB[0]+cri*2:
                cur_LB[0] += cri
            else:
                cur_wLB[0] = cur_LB[0]+cri*2
                cur_LB[0] += cri
        elif cmd[0] == 4:
            cri = N / cmd[1]
            if cur_wRT[0] <= cur_RT[0]-cri*2:
                cur_RT[0] -= cri
            else:
                cur_wRT[0] = cur_RT[0]-cri*2
                cur_RT[0] -= cri
        #print(i+1, '번째', cur_LB, cur_RT)
    cur_X = cur_RT[0] - cur_LB[0]
    cur_Y = cur_RT[1] - cur_LB[1]
    w_area = (cur_wRT[0]-cur_wLB[0])*(cur_wRT[1]-cur_wLB[1])
    b_area = cur_X*cur_Y - w_area
    answer.append(int(b_area))
    answer.append(int(w_area))
    return answer

print(solution(4,2,[[1,4],[3,4]]))
print(solution(4,2,[[3,2],[3,4]]))