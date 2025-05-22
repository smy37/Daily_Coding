def solution(N, M, Command):
    answer = []
    diagonal = {}
    diagonal['ul'] = []
    diagonal['ur'] = []
    diagonal['dl'] = []
    diagonal['dr'] = []
    cur_LB = [0,0]
    cur_RT = [N,N]
    cur_wLB = [0, 0]
    cur_wRT = [N, N]
    for i in range(M):
        cmd = Command[i]
        cur_X = cur_RT[0]-cur_LB[0]
        cur_Y = cur_RT[1]-cur_LB[1]
        cri = N // cmd[1]
        if cmd[0] == 1:
            if cur_wRT[1] <= cur_RT[1]-2*cri:
                cur_RT[1] -= cri
            else:
                cur_wRT[1] = cur_RT[1]-2*cri
                cur_RT[1] -= cri
        elif cmd[0] == 2:
            if cur_wLB[1] >= cur_LB[1]+2*cri:
                cur_LB[1] += cri
            else:
                cur_wLB[1] = cur_LB[1]+2*cri
                cur_LB[1] += cri
        elif cmd[0] == 3:
            if cur_wLB[0] >= cur_LB[0] + 2*cri:
                cur_LB[0] += cri
            else:
                cur_wLB[0] = cur_LB[0] + 2*cri
                cur_LB[0] += cri
        elif cmd[0] == 4:
            if cur_wRT[0] <= cur_RT[0] -2*cri:
                cur_RT[0] -= cri
            else:
                cur_wRT[0]= cur_RT[0] -2*cri
                cur_RT[0] -= cri
        elif cmd[0] == 5:
            diagonal['ul'] = [cur_LB[0]+cri, cur_RT[1]-cri, cri]
        elif cmd[0] == 6:
            diagonal['ur'] = [cur_RT[0] - cri, cur_RT[1] - cri, cri]
        elif cmd[0] == 7:
            diagonal['dl'] = [cur_LB[0] + cri, cur_LB[1] + cri, cri]
        elif cmd[0] == 8:
            diagonal['dr'] = [cur_RT[0] - cri, cur_LB[1] + cri, cri]
    cur_X = cur_RT[0] - cur_LB[0]
    cur_Y = cur_RT[1] - cur_LB[1]
    area = cur_X*cur_Y
    w_area = (cur_wRT[0]-cur_wLB[0])*(cur_wRT[1]-cur_wLB[1])
    # b_area = area-w_area
    # print(w_area, b_area, cur_wLB, cur_wRT, cur_LB, cur_RT)
    t_b_area = 0
    if diagonal['ul'] != []:
        t_b_area += (diagonal['ul'][2]**2)/2
        if diagonal['ul'][0] > cur_wLB[0] and diagonal['ul'][1] < cur_wRT[1]:
            wx = min(diagonal['ul'][0], cur_wRT[0])
            wy = max(diagonal['ul'][1], cur_wLB[1])
            t_w_area = (wx - cur_wLB[0])*( cur_wRT[1]- wy)
            w_area -= t_w_area
            # b_area += (t_w_area - t_b_area)
        # else:
        #     b_area -= t_b_area
        if diagonal['dr'] != []:
            if diagonal['dr'][0] < diagonal['ul'][0] and diagonal['dr'][1] > diagonal['ul'][1]:
                if (cur_wLB[0] <=diagonal['dr'][0]<=cur_wRT[0]) and (cur_wLB[1] <=diagonal['dr'][1]<=cur_wRT[1]):
                    w_area += (diagonal['ul'][0]-diagonal['dr'][0])*(diagonal['dr'][1] - diagonal['ul'][1])
    if diagonal['ur'] != []:
        t_b_area += (diagonal['ur'][2] ** 2) / 2
        if diagonal['ur'][0] < cur_wRT[0] and diagonal['ur'][1] < cur_wRT[1]:
            wx = max(diagonal['ur'][0], cur_wLB[0])
            wy = max(diagonal['ur'][1], cur_wLB[1])
            t_w_area = (cur_wRT[0]-wx) * (cur_wRT[1] - wy)
            w_area -= t_w_area
            # b_area += (t_w_area - t_b_area)
        # else:
        #     b_area -= t_b_area
        if diagonal['dl'] != []:
            if diagonal['ur'][0] < diagonal['dl'][0] and diagonal['ur'][1] < diagonal['dl'][1]:
                if (cur_wLB[0] <= diagonal['dl'][0] <= cur_wRT[0]) and (cur_wLB[1] <= diagonal['dl'][1] <= cur_wRT[1]):
                    w_area += (diagonal['ur'][0] - diagonal['dl'][0])*(diagonal['ur'][1] - diagonal['dl'][1])
    if diagonal['dl'] != []:
        t_b_area += (diagonal['dl'][2] ** 2) / 2
        if diagonal['dl'][0] > cur_wLB[0] and diagonal['dl'][1] > cur_wLB[1]:
            wx = min(diagonal['dl'][0], cur_wRT[0])
            wy = min(diagonal['dl'][1], cur_wRT[1])
            t_w_area = (wx-cur_wLB[0] ) * (wy-cur_wLB[1])
            w_area -= t_w_area
        #     b_area += (t_w_area - t_b_area)
        # else:
        #     b_area -= t_b_area
    if diagonal['dr'] != []:
        t_b_area += (diagonal['dr'][2] ** 2) / 2
        if diagonal['dr'][0] < cur_wRT[0] and diagonal['dr'][1] > cur_wLB[1]:
            wx = max(diagonal['dr'][0], cur_wLB[0])
            wy = min(diagonal['dr'][1], cur_wRT[1])
            t_w_area = (cur_wRT[0]-wx) * (wy - cur_wLB[1])
            w_area -= t_w_area
        #     b_area += (t_w_area - t_b_area)
        # else:
        #     b_area -= t_b_area
    w_area = max(w_area, 0)
    b_area = area - w_area- t_b_area
    answer = [int(b_area*100),int(w_area*100)]
    return answer

# print(solution(4, 2, [[5,2],[8,2]]))
# print(solution(4, 3, [[2,4],[8,2],[6,4]]))
# print(solution(8, 4, [[2,4],[2,4],[5,2],[6,4]]))
# print(solution(8, 4, [[1,4],[1,4],[5,4],[6,4]]))
# print(solution(8, 4, [[1,4],[2,4],[5,4],[6,4]]))
print(solution(8, 4, [[5,2],[6,2],[7,2],[8,4]]))
print(solution(8, 1, [[5,1]]))
