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
    rounded = cur_X*2 + cur_Y*2
    if diagonal['ul'] != []:
        rounded -= 2*diagonal['ul'][2]
        rounded += math.sqrt(2)*diagonal['ul'][2]
    if diagonal['ur'] != []:
        rounded -= 2*diagonal['ur'][2]
        rounded += math.sqrt(2) * diagonal['ur'][2]
    if diagonal['dl'] != []:
        rounded -= 2*diagonal['dl'][2]
        rounded += math.sqrt(2) * diagonal['dl'][2]
    if diagonal['dr'] != []:
        rounded -= 2*diagonal['dr'][2]
        rounded += math.sqrt(2) * diagonal['dr'][2]
    answer = int(rounded*100)
    return answer

print(solution(4, 1, [[8,2]]))
print(solution(4, 3, [[2,4],[8,2],[6,4]]))