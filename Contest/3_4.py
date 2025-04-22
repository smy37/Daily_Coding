import math

def solution(N, M, Command):
    answer = 0
    diagonal = {}
    diagonal['ul'] = []
    diagonal['ur'] = []
    diagonal['dl'] = []
    diagonal['dr'] = []
    cur_LB = [0,0]
    cur_RT = [N,N]
    for i in range(M):
        cmd = Command[i]
        cur_X = cur_RT[0]-cur_LB[0]
        cur_Y = cur_RT[1]-cur_LB[1]
        cri = N / cmd[1]
        if cmd[0] == 1:
            cur_RT[1] -= cri
        elif cmd[0] == 2:
            cur_LB[1] += cri
        elif cmd[0] == 3:
            cur_LB[0] += cri
        elif cmd[0] == 4:
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
    if diagonal['ul'] != []:
        area -= (diagonal['ul'][2]**2)/2
    if diagonal['ur'] != []:
        area -= (diagonal['ur'][2]**2)/2
    if diagonal['dl'] != []:
        area -= (diagonal['dl'][2] ** 2) / 2
    if diagonal['dr'] != []:
        area -= (diagonal['dr'][2] ** 2) / 2
    answer = int(area*100)
    return answer

print(solution(4, 1, [[8,2]]))
print(solution(4, 3, [[2,4],[8,2],[6,4]]))